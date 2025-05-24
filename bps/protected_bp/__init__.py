from flask import Blueprint

protected_bp = Blueprint('protected_bp', __name__)

from . import routes