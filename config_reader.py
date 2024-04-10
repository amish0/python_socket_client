import yaml

class ConfigReader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.read_config()

    def read_config(self):
        with open(self.config_path, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def get_config(self):
        return self.config
    
config_parm = ConfigReader("config.yaml")