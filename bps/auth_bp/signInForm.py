from flask_wtf import FlaskForm
from wtforms import fields as f
from wtforms import validators as v
import re

class SignInForm(FlaskForm):
    signInEmail = f.EmailField(   
                'email',
                validators=[
                    v.DataRequired("*this is required field"),
                    v.Regexp(r'^[A-Za-z0-9]+@[A-Za-z0-9]+\.com$', message="Please provide valid email"),
                ],
                render_kw={"placeholder": "Email"}
            )
    signInPassword = f.PasswordField(
                'password',
                validators=[
                    v.DataRequired("*this is required field")
                ],
                render_kw={"placeholder": "Password"}
            )
    submit = f.SubmitField('Sign In')