from flask import Flask

app = Flask(__name__)

from resources.anime import routes
from resources.user import routes