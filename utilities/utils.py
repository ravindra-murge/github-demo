import inspect
import logging


class Utils:
    def assert_text(self,list,value):
        for itme in list:
            assert itme.text == value

    def custom_logger(self,loglevel=logging.DEBUG):
        # set class/method name from where its called
        logger_name = inspect.stack()[1][3]
#        create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)

#         create console handler or file handler and set the loglevel
        filehandler = logging.FileHandler("automation.log")
        # create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s')
        # add formatter to console or file handler
        filehandler.setFormatter(formatter)
        # add console handler to logger
        logger.addHandler(filehandler)
        return logger
