from flask import render_template, request, redirect, url_for, session, jsonify, make_response
from flask_jwt_extended import create_access_token
from datetime import timedelta

from .signInForm import SignInForm
from .signUpForm import SignUpForm

from app.db import mysql
from app.db import bcrypt

from .utility import signIn, signUp

def SignIn_SignUp_Form():
    signInForm = SignInForm()
    signUpForm = SignUpForm()
    signUpOnLoad = False

    if request.method == "POST":
        if request.form.get('form-type') == 'signInForm':
           if signIn(signInForm):
                access_token = create_access_token(identity="Hello", expires_delta=timedelta(minutes=30))
                res = make_response(redirect( url_for("main.index") ))
                res.set_cookie("access_token", access_token, httponly= True, max_age= timedelta(minutes=30))
                return res
        else:
            signUpOnLoad = signUp(signUpForm)
    
    # GET method | validations failed | signed up successfully -> login
    return render_template("SignIn_SignUp/index.html", signInForm=signInForm, signUpForm=signUpForm, signUpOnLoad = signUpOnLoad)

def LogOut():
    state = session.get('state', 'Karnataka')
    country = session.get('country', 'India')
    states = session.get('states', [])
    session.clear()
    res = make_response(redirect( url_for("main.index") ))
    res.set_cookie("access_token", "", httponly=True, expires=0)
    session['state'] = state
    session['country'] = country
    session['states'] = states
    return res

def AuthMiddleware():
    if session.get('username', None):
        return jsonify({'statusCode': 200, 'message': 'authorized', 'userId': session['_id']})
    
    return jsonify({'statusCode': 401, 'message': 'authorized', 'userId': None})