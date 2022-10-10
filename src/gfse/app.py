import argparse
import colorlog
import logging
import logging.config
import os

from gfse import api

app = api.create_app(os.getcwd())

def load_log(debug):
    log_config = {
        'version': 1,
        'root': { 'handlers': ['console'], 'level': 'DEBUG' if debug else 'INFO' },
	'handlers': {'console': {'class': 'logging.StreamHandler', 'formatter': 'color'}},
	'formatters': {'color': {'()':     'colorlog.ColoredFormatter', 
                                 'format': '%(asctime)s %(log_color)s%(levelname)-8s%(reset)s %(process)s %(name)s %(message)s'}}
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

def main(host, port, debug, use_reloader):
    load_log(debug)
    app.run(host=host, port=port, debug=debug, use_reloader=use_reloader)
    
if __name == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--host', default=default_host, help='APIn Host')
    parser.add_argument('-p', '--port', type=int default=default_port, help='API Port')
    parser.add_argument('-v', '--verbose', type=bool, default=default_debug, help='API debug')
    parser.add_argument('-r', '--use-reloader', type=bool, default=default_reloader, help='API use reloader')
    args = parser.parse_args()
    
    main(args.host, args.port, args.debug, args.use_reloader):
    
