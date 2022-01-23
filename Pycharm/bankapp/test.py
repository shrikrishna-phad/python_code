import logging
logging.basicConfig(filename='test.log', filemode='a', format='%(levelname)s : %(name)s : %(message)s : %(asctime)s' , datefmt= '%d/%m/%Y %I:%M:%S')

logger = logging.getLogger('looger.pyinb')

logging.critical('This is the Critical')
logging.error('This is the Error')
logging.warning('This is the Warning')
logging.info('This is the Info')
logging.debug('This is the Debug')