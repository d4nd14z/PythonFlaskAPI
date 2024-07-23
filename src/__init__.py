from flask import Flask
from .routes import AuthRoutes, IndexRoutes, LanguageRoutes

app = Flask(__name__)

def init_app(config): 
    app.config.from_object(config)
    app.register_blueprint(AuthRoutes.main, url_prefix='/auth')
    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(LanguageRoutes.main, url_prefix='/languages')
    return app