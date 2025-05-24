from dotenv import load_dotenv
from flask import Flask, render_template, request, session
from config import Config
from datetime import timedelta


from .db import mongo
from .db import mysql
from .db import bcrypt
from .db import jwt

from .bps.auth_bp import auth_bp
from .bps.landing_bp import landing_bp
from .bps.api_bp import api_bp
from .bps.protected_bp import protected_bp
from .bps.newsShowCase_bp import newsShowCase_bp
from .bps.world_bp import world_bp
from .bps.newsPage import newsPage_bp

def create_app():
    #loading the environement varaible to use it in differnt files(like; config.py)
    load_dotenv(dotenv_path='../')
    app = Flask(__name__)
    app.config.from_object(Config)
    app.url_map.strict_slashes = False
    app.permanent_session_lifetime = timedelta(minutes=30)

    # Initialize database here
    mongo.init_app(app)
    mysql.init_app(app)

    # Initialize the Flask app with bcyrpt
    bcrypt.init_app(app)

    #Intializing JWT tokens
    jwt.init_app(app)

    # BluePrints Registering
    app.register_blueprint(newsPage_bp, url_prefix='/info/')
    app.register_blueprint(api_bp, url_prefix='/api/')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(landing_bp, url_prefix = '/') 
    app.register_blueprint(protected_bp, url_prefix='/')
    app.register_blueprint(newsShowCase_bp, url_prefix='/newsShowCase')
    app.register_blueprint(world_bp, url_prefix='/world/')

    # creating templates
    import re
    @app.template_filter('regex_fullmatch')
    def regex_fullmatch(string, pattern):
        return bool(re.fullmatch(pattern, string))
    
    # missingPage errorhandler
    @app.errorhandler(404)
    def notFound(error):
        from  datetime import datetime
        return render_template('notFoundPage.html', today = datetime.now())
    
    @app.before_request
    def set_location():
        if not (session.get('state', False) and session.get('country', False)):
            db = mongo.cx['newChannels']
            countries = list( db.countries.find({'name': 'India'}, {'_id': 0, 'states': 1 }) )
            session['states'] = (countries if countries else [[]])[0].get('states', [])
            session['state']  = ['Karnataka', 'India']
            session['country'] = 'India'


    return app

