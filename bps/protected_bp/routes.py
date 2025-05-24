from . import protected_bp
from .controller import following, forYou, unauthorized_fallback
from flask_jwt_extended import jwt_required
from app.db import jwt

# unauthorized access via protected routes going to main(landing_bp).index ------> [HomePage]
jwt.unauthorized_loader(unauthorized_fallback)

protected_bp.route('/following')(jwt_required()(following))
protected_bp.route('/forYou')(jwt_required()(forYou))