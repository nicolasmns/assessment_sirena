import os 
from log_debug import LogDebug
from log_warning import LogWarning
from log_error import LogError
from log_info import LogInfo

class FactoryLoggingOptions:

    @staticmethod
    def create_logging_options():
        os.environ['DEBUG'] = '10'
        os.environ['WARNING'] = '30'
        os.environ['ERROR'] = '40'
        os.environ['INFO'] = '20'


        


