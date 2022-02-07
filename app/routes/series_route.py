from flask import Blueprint
from app.controllers import series_controller

bp = Blueprint('series', __name__)

bp.get('')(series_controller.series)

bp.get('/<int:serie_id>')(series_controller.select_by_id)

bp.post('')(series_controller.create)

