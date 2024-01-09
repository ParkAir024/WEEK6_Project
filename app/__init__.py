from flask import Flask
from flask_smorest import Api
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

from resources.user import bp as user_bp
api.register_blueprint(user_bp)

from resources.anime import bp as anime_bp
api.register_blueprint(anime_bp)