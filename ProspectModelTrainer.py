import pandas as pd
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import pickle

from Config import  Config
# getting the setting form Config
confObj = Config()

def file_reader():
    csv_file_path = confObj.dataSourcePath()
    print(csv_file_path)
    train = pd.read_csv(csv_file_path,encoding="UTF-8")
    train.drop(['gcardId','IsInternationalApplicant','County','ResidentDesignation','MaritalStatus','PrefCommunicationType','relCode'],axis = 1, inplace = True)
    #Feature variable
    X = train.drop(['status'],axis=1) 
    #Target variable
    y = train[['status']].values.ravel()
    return X,y

def model_training(X,y):
    categorical_freatures = X.select_dtypes(include ="object").columns
    integer_features = X.select_dtypes(exclude = "object").columns
    print("Categorical features:" + categorical_freatures)
    print("numerical features:" + integer_features)

    for c in categorical_freatures:
        lbl = LabelEncoder()
        lbl.fit(list(X[c].values))
        X[c] = lbl.transform(list(X[c].values))
    
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
    
    X = preprocessor.fit_transform(X)
    
    X_train, X_valid, y_train, y_valid = train_test_split(X,y,test_size=0.30,random_state=42,shuffle=False)
    
    Gbost = GradientBoostingClassifier(n_estimators=3000,learning_rate=0.05, max_depth=4,max_features='sqrt',
                                       min_samples_leaf= 15,min_samples_split=10,loss='log_loss',random_state=5 )
    
    Gbost.fit(X_train,y_train)

    # Test our test sample data.
    csv_test_file_path = confObj.testDataPath()
    test = pd.read_csv(csv_test_file_path,encoding='UTF-8')
    
    test.drop(['gcardId','IsInternationalApplicant','County','ResidentDesignation','MaritalStatus','PrefCommunicationType','relCode'],axis = 1, inplace = True)
    X_test = test.drop(['status'],axis=1) 
  #  y_test = test[['status']].values.ravel()
    for c in categorical_freatures:
        lbl = LabelEncoder()
        lbl.fit(list(test[c].values))
        test[c] = lbl.transform(list(test[c].values))
    
    X_test = preprocessor.fit_transform(test)

    prediction = Gbost.predict(X_test)

    print(prediction)

    model_obj_path = confObj.modelPath()

    # pickle our model that we can use if for predictions 
    pickle.dump(Gbost,open(model_obj_path,'wb+'))
    print("Model Dumped")


if __name__ =='__main__':
    x_feature,y_target = file_reader()
    model_training(x_feature,y_target)


