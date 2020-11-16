class Displayer:
    @staticmethod
    def showLogs(logs, level):
        for log in logs:
            printable = log.get_log(int(level))
            if(printable):
                print(printable)
        
    @staticmethod
    def save_to_file(file_name, level, logs):
        file = file_name + ".txt"
        print(file)
        file_object = open(file, 'w')
        for log in logs:
            line = log.get_log(int(level))
            if(line):
                file_object.write(line)

