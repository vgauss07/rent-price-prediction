from loguru import logger


# DEBUG - function, parameters level: what your code is in the context
# in fns and params.
# INFO - running order to the application
# WARNING - It is okay but needs your attention
# ERROR - something has gone wrong while running the application.
# CRITICAL - severe impact on application  running.
# logger.add('app.log', rotation='1 MB') # log file not more thann 1 MB
# logger.add('app.log', rotation='01:45', retention='1 MINUTE',
# compression='zip')
# set specific time to create log file: useful for creating daily log files

logger.add('info.log', level='INFO', diagnose=False)
logger.add('critical.log', level='CRITICAL')


def divide_by(a, b):
    logger.debug(f"Calculating with a = {a}, and b = {b}")
    logger.info("Executing divide by function")
    logger.warning("note: b=0 can lead to an error in the application")
    return a/b


try:
    res = divide_by(2, 0)
    print(res)
except ZeroDivisionError:
    logger.error("division by 0")

logger.info('Calculating a / b')
logger.debug('Division by 0!!')
logger.warning('Division by 0!!')
logger.error('Division by 0!!')
logger.critical('Division by 0!!')
