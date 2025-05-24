from flask import Blueprint

world_bp = Blueprint('world_bp', __name__)  

from . import routes