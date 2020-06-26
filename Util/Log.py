#实现日志的功能
#配置文件Logger.conf放到Config下
import logging.config
import logging

logging.config.fileConfig(r"D:\test\keyword_driven_framework\Config\Logger.conf")
logger = logging.getLogger("example01")

def debug(message):#打印debug级别的日志方法
    logger.debug(message)

def warning(message):#打印warning级别的日志方法
    logger.warning(message)

def info(message):
    logger.info(message)

def error(message):
    logger.error(message)



if __name__ == "__main__":
    debug("Hi this is begin of debug log")
    info("i am typing info log")
    warning("yes,is warning log is me")
    error("这是一个error级别的日志")


