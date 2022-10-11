import argparse
import os

from gfse import api

app = api.create_app(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config"),
                     os.environ.get('API_LOGFILE', None))

def main(host, port, debug, use_reloader):
    app.run(host=host, port=port, debug=debug, use_reloader=use_reloader)
    
if __name__ == '__main__':
    default_host               = os.environ.get('API_HOST', '0.0.0.0')
    default_port               = os.environ.get('API_PORT', 8888)
    default_debug              = os.environ.get('API_DEBUG', False)
    default_reloader           = os.environ.get('API_RELOADER', False)

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--host', default=default_host, help='APIn Host')
    parser.add_argument('-p', '--port', type=int, default=default_port, help='API Port')
    parser.add_argument('-v', '--verbose', action='store_true', default=default_debug, help='API debug')
    parser.add_argument('-r', '--use-reloader', action='store_true', default=default_reloader, help='API use reloader')
    args = parser.parse_args()
    
    main(args.host, args.port, args.verbose, args.use_reloader)
    
