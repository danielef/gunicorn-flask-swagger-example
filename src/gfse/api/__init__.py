import connexion
from gfse.api import error_handler
from flask_cors import CORS as cors
from swagger_ui_bundle import swagger_ui_path

def create_app(spec_dir):
    options = {"swagger_path": swagger_ui_path}
    app = connexion.App(__name__, specification_dir=spec_dir, options=options)
    cors(app.app)
    app.add_api("swagger.yaml", strict_validation=True, validate_responses=True)
    error_handler.register_error_handlers(app)
    return app

def dummy_api_key_validation(*_args, **_kwargs):
    """Dummy function for Connexion API key validation."""
    return {}
