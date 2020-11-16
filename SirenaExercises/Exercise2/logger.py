import os
from factory_logging_options import FactoryLoggingOptions
from log_error import LogError
from log_warning import LogWarning
from log_debug import LogDebug
from log_info import LogInfo
from displayer import Displayer

class Logging:

    __login_level = 0
    __logs = []

    def __init__(self):
        FactoryLoggingOptions().create_logging_options()

    def set_login_level(self, level):
        try:
            self.__login_level = int(os.environ[level.upper()])
            print("Level set to {}".format(level.upper()))
        except:
            print("The level you've entered is invalid or doesn't exist.")
            
    def error(self, file_name, function_name, comments = ""):
        self.__logs.append(LogError(file_name, function_name, comments))
        Displayer().showLogs(self.__logs, self.__login_level)

    def debug(self, file_name, function_name, comments = ""):
        self.__logs.append(LogDebug(file_name, function_name, comments))
        Displayer().showLogs(self.__logs, self.__login_level)

    def warning(self, file_name, function_name, comments = ""):
        self.__logs.append(LogWarning(file_name, function_name, comments))
        Displayer().showLogs(self.__logs, self.__login_level)

    def info(self, file_name, function_name, comments = ""):
        self.__logs.append(LogInfo(file_name, function_name, comments))
        Displayer().showLogs(self.__logs, self.__login_level)
    
    def get_all_logs(self):
        Displayer().showLogs(self.__logs, self.__login_level)
    
    def save_to_file(self, file_name):
        Displayer().save_to_file(file_name, self.__login_level, self.__logs)

    def delete_all_logs(self):
        print("Logs have been deleted.")
        self.__logs = []
