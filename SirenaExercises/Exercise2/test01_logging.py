import unittest
from logger import Logging

class Test_Logging(unittest.TestCase):

    def test_setLoginLevelToError(self):
        logger = Logging()
        logger.set_login_level("ERROR")
        print(logger.get_login_level() + "\n")
        self.assertIn("ERROR",logger.get_login_level())
    
    def test_setLoginLevelToDebug(self):
        self.__logger.set_login_level("ERROR")
        self.assertIn("WARNING",self.__logger.get_login_level())

    def test_setLoginLevelToInfo(self):
        self.__logger.set_login_level("ERROR")
        self.assertIn("ERROR",self.__logger.get_login_level())

    def test_setLoginLevelToWarning(self):
        self.__logger.set_login_level("ERROR")
        self.assertIn("ERROR",self.__logger.get_login_level())

if __name__ == "__main__":
    unittest.main()
