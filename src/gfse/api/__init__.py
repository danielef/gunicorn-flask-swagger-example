import connexion
import colorlog
import logging
import logging.config
import time
from gfse.api import error_handler
from flask_cors import CORS as cors
from swagger_ui_bundle import swagger_ui_path

def load_log(debug):
    log_config = {
        'version': 1,
        'root': { 'handlers': ['console'], 'level': 'DEBUG' if debug else 'INFO' },
	'handlers': {'console': {'class': 'logging.StreamHandler', 'formatter': 'color'}},
	'formatters': {'color': {'()':     'colorlog.ColoredFormatter',
                                 'format': '%(asctime)s %(log_color)s%(levelname)-8s%(reset)s %(process)s %(name)s %(message)s'}},
        'loggers': {
            ''               : {'level': 'INFO', 'handlers': ['console']},
            'gunicorn.access': {'handlers': ['console']},
            'gunicorn.error' : {'handlers': ['console']},
            'gunicorn.glogging.Logger' : {'handlers': ['console']}
        }
    }

    logging.config.dictConfig(log_config)
    try:
        if isinstance(logging.getLogger().handlers[0].formatter, colorlog.ColoredFormatter):
            logging.getLogger().handlers[0].formatter.log_colors = {'DEBUG': 'cyan',
                                                                    'INFO': 'green',
                                                                    'WARNING': 'yellow',
                                                                    'ERROR': 'red',
                                                                    'CRITICAL': 'purple'}
    except Exception:
        pass

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        logging.info('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te-ts))
        return result
    return timed

def create_app(spec_dir):
    load_log(False)
    options = {"swagger_path": swagger_ui_path}
    app = connexion.App(__name__, specification_dir=spec_dir, options=options)
    cors(app.app)
    app.add_api("swagger.yaml", strict_validation=True, validate_responses=True)
    error_handler.register_error_handlers(app)
    return app

def dummy_api_key_validation(*_args, **_kwargs):
    """Dummy function for Connexion API key validation."""
    return {}
