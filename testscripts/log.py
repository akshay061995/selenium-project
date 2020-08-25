import logging

logging.basicConfig(filename="C://pycharm//log files//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.DEBUG)

logging.debug("this is a debug message")
logging.info("this is a info message")
logging.warning("this is a warning message")
logging.error("this is a error message")
logging.critical("this is a critical message")
