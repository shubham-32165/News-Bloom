from flask import Blueprint

landing_bp = Blueprint('main', __name__)

from . import routes