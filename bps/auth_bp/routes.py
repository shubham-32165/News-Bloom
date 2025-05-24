from . import auth_bp
from .Controllers import SignIn_SignUp_Form, LogOut, AuthMiddleware

# /auth/<signIn/LogOut/currentlyLoggedIn>
auth_bp.route('/signIn', methods=['GET','POST'])(SignIn_SignUp_Form)
auth_bp.route('/LogOut', methods=['GET','POST'])(LogOut)
auth_bp.route('/currentlyLoggedIn')(AuthMiddleware)