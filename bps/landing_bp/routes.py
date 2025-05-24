from . import landing_bp
from .Controllers import index

landing_bp.route('/')(index)