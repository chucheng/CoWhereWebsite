import os, binascii
import logging

def sixCharRandom():
    return binascii.b2a_hex(os.urandom(3))

def tenCharRandom():
    return binascii.b2a_hex(os.urandom(5))

def getPrettyLogger(log_filename, module_name):
    logger = logging.getLogger(module_name)
    ch = logging.StreamHandler()
    fh = logging.FileHandler(log_filename)
    formatter = logging.Formatter('%(asctime)s\t%(levelname)s\t%(name)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)    
    return logger

def getSimpleJson(key, value):
    return '{{"{0}":"{1}"}}\n'.format(key, value)