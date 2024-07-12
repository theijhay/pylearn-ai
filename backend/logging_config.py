from logging.config import dictConfig
import logging

def setup_logging():
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
        },
        'handlers': {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            },
        },
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    }
    
    dictConfig(logging_config)

# Call the setup_logging function to configure logging when the module is imported
setup_logging()
