import json
import pickle
from flask import Flask, Response ,jsonify, request
from sklearn.calibration import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.discriminant_analysis import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from Prospect import Prospect
from Config import Config
import pandas as pd
from flask_cors import CORS
from Predict import Predict

confObj = Config()
predictObj = Predict(0)
load_model = pickle.load(open(confObj.modelPath(),'rb'))
app = Flask(__name__)
CORS(app)

@app.route('/healthcheck')
def HealthCheck():
    return "WebServer is up and running!"

@app.route('/Predict', methods=['GET','POST'])
def prospectPredict():

    request_data = request.get_json()
    prospectObj = Prospect(request_data['gcardId'],
                            request_data['relCode'],
                            request_data['phoneType1'],request_data['phoneType2'],
                            request_data['city'],request_data['state'],request_data['zip'],request_data['countryCode'],request_data['jobTypeID'],request_data['rentOwnFlag'],
                            request_data['DOB'],request_data['Gender'],request_data['CriminalQuestion'],request_data['BrokenLease'],request_data['Evicted']
                            ,request_data['SuedForDamage'],request_data['SuedForRent'],request_data['MaritalStatus'],request_data['ResidentDesignation'],request_data['IsInternationalApplicant']
                            ,request_data['PrefCommunicationType'],request_data['County'],request_data['status'],request_data['trfsrcName'],request_data['gcardPreferedFloorplanGroupId'],request_data['gcardOccupantCount'])
    
    
    df = pd.DataFrame(prospectObj.__dict__,index=[0])
    df.drop(['gcardId','IsInternationalApplicant','County','ResidentDesignation','MaritalStatus','PrefCommunicationType','relCode'],axis = 1, inplace = True)
    X_test = df.drop(['status'],axis=1) 
    categorical_freatures = X_test.select_dtypes(include ="object").columns
    integer_features = X_test.select_dtypes(exclude = "object").columns

    print("Categorical features:" + categorical_freatures)
    print("numerical features:" + integer_features)

    for c in categorical_freatures:
        lbl = LabelEncoder()
        lbl.fit(list(df[c].values))
        df[c] = lbl.transform(list(df[c].values))
    
    integer_transformer = Pipeline(steps = [
        ('imputer',SimpleImputer(strategy= 'mean')),
        ('scaler',StandardScaler())])

    categorical_transformer = Pipeline(steps =[
        ('imputer',SimpleImputer(strategy= 'most_frequent'))
    ])
    
    preprocessor = ColumnTransformer(
        transformers= [
            ('ints', integer_transformer,integer_features),
            ('cat', categorical_transformer,categorical_freatures)])
    
    X_test = preprocessor.fit_transform(df)

    predict_Lease_Status = load_model.predict(X_test)
    json_object = json.loads('{"Predict": '+ str(predict_Lease_Status[0]) + '}')
    return jsonify(json_object)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')