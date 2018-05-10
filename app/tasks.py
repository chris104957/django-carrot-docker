import logging

logger = logging.getLogger('carrot')


def hello_world(*args, **kwargs):
    logger.debug('hello')
    logger.info('hello')
    logger.warning('hello')
    logger.error('hello')
    logger.critical('hello')