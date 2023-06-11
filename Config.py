import yaml
import traceback

class Config:
    def __init__(self):
        print("objec created")
        try:
            with open('properties.yml','r') as f:
                properties = yaml.load(f,Loader=yaml.FullLoader)
                print(properties)
                self.data_path = properties['settings']['data_path']
                self.data_file = properties['settings']['data_file']
                self.model_path = properties['model']['model_path']
                self.model_file = properties['model']['model_file']
                self.streaming_file = properties['settings']['streaming_file']
                self.kafka_host = properties['settings']['kafka_host']
                self.test_file = properties['settings']['test_file']
        except Exception as ex:
            traceback.print_exc();
    
    def modePath(self):
        return self.model_path + self.model_file

    def dataSourcePath(self):
        return self.data_path + self.data_file
    
    def testDataPath(self):
        return self.data_path + self.test_file
