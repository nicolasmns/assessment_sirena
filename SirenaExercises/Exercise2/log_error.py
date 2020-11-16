from logging_options_interface import LoggingOptionsInterface

class LogError(LoggingOptionsInterface):
    __value = 40
    __log = None
    def __init__(self, file_name, function_name, comments):
        self.__log = '[{}][{}] {}'.format(file_name, function_name, comments)

    def get_log(self, current_value):
        if(self.__value >= current_value):
            return "[ERROR]{}".format(self.__log) + "\n"
        return None

