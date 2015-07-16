'''
Created on 15 Jul 2015

@author: sfrullo
'''

'''This module defines the logging configuration.
Here are all the project's Logger modules configuration'''

import logging.config
from os import getenv


LOGDIR = '../../mahnobplayer/log/' if not getenv('LOG_CFG', None) else getenv('LOG_CFG', None)

DEBUG = True

LOGGING = {
    'version': 1,
    'formatters': {
        'info_format': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-10s %(levelname)-8s %(message)s'
        },
        'error_format':{
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-10s %(levelname)-8s %(processName)-8s %(funcName)-10s %(lineno)-5d %(message)s'
        },
        'debug_format':{
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-10s %(levelname)-8s %(funcName)-10s %(lineno)-5d %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'stream': 'ext://sys.stdout',
            'formatter': 'info_format'
        },
        'debug': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'stream': 'ext://sys.stdout',
            'formatter': 'debug_format'
        },         
        'info_file': {
            'class': 'logging.FileHandler',
            'filename': LOGDIR + 'info.log',
            'mode': 'w',
            'level': 'INFO',
            'formatter': 'info_format',
        },
        'errors': {
            'class': 'logging.FileHandler',
            'filename': LOGDIR + 'errors.log',
            'mode': 'w',
            'level': 'ERROR',
            'formatter': 'error_format',
        },
    },
    'loggers': {
        'player': {
            'handlers':['console', 'info_file', 'errors'],
        },
        'gui': {
            'handlers':['console', 'info_file', 'errors'],
        },
        'controller': {
            'handlers':['console', 'info_file', 'errors'],
        },
        'main': {
            'handlers':['console', 'info_file', 'errors'],
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'info_file', 'errors', 'debug'],
        'propagate': True,
    }, 
}        

logging.config.dictConfig(LOGGING)
