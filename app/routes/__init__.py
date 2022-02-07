from flask import Flask, Blueprint

from app.routes.series_route import bp as bp_register_route

bp_api = Blueprint("api", __name__, url_prefix="/series")


def init_app(app: Flask):
    
    bp_api.register_blueprint(bp_register_route)
    
    app.register_blueprint(bp_api)