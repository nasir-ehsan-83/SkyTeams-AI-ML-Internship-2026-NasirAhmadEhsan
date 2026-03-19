import logging

logging.basicConfig(filename = 'error.log', level = int(logging.ERROR))

def logging_error(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as error:
        logging.error(str(error))
        return None