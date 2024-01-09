from flask_smorest import Blueprint

bp = Blueprint('animes', __name__, description='Ops on Animes', url_prefix='/anime')

from . import routes