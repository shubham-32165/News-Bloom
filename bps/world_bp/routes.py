from . import world_bp
from .Controllers import country,world,locale

world_bp.route('/')(world)
world_bp.route('/<country>')(country)
world_bp.route('/<country>/<state>')(locale)