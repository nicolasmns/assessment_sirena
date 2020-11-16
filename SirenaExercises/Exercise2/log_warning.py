from logging_options_interface import LoggingOptionsInterface

class LogWarning(LoggingOptionsInterface):
    __value = 30
    __log = None
    def __init__(self, file_name, function_name, comments):
        self.__log = '[{}][{}] {}'.format(file_name, function_name, comments)

    def get_log(self, current_value):
        if(self.__value >= current_value):
            return "[WARNING]{}".format(self.__log) + "\n"
        return None
