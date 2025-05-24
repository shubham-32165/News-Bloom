from flask_wtf import FlaskForm
from wtforms import fields as f
from wtforms import validators as v
import re

def RegexValidation(form, field):
    message = "Must include uppercase, lowercase, digit and special character"
    v1 = not bool( re.fullmatch(r'^.*[0-9].*$', field.data) )
    v2 = not bool( re.fullmatch(r'^.*[A-Z].*$', field.data) )
    v3 = not bool( re.fullmatch(r'^.*[a-z].*$', field.data) )
    v4 = not bool( re.fullmatch(r'^.*[!@#$].*$', field.data) )
    if v1 or v2 or v3 or v4:
        raise v.ValidationError(message=message)

class SignUpForm(FlaskForm):
    username = f.StringField(
                'username',
                validators=[
                    v.DataRequired("*this is required field"),
                    v.Regexp(r'[A-Za-z0-9 ]+', message="Only alphanumeric values are allowed")
                ],
                render_kw={"placeholder": "Username"}
            )
    
    signUpEmail = f.EmailField(   
                'email',
                validators=[
                    v.DataRequired("*this is required field"),
                    v.Regexp(r'^[A-Za-z0-9]+@[A-Za-z0-9]+\.com$', message="Please provide valid email"),
                ],
                render_kw={"placeholder": "Email"}
            )
    
    signUpPassword = f.PasswordField(
                'Password',
                validators=[
                    v.DataRequired("*this is required field"),
                    v.Length(min=8, message="Password must be of 8 characters"),
                    v.Length(max=20, message="Password can upmost of 20 character"),
                    RegexValidation,
                    v.EqualTo('confirmPassword', message="Password must match")
                ],
                render_kw={"placeholder": "Password"}
            )
    
    confirmPassword = f.PasswordField(
                'Confirm Password',
                validators=[
                    v.DataRequired("*this is required field"),
                    v.Length(min=8, message="Password must be of 8 characters"),
                    v.Length(max=20, message="Password can upmost of 20 character"),
                    RegexValidation,
                    v.EqualTo('signUpPassword', message="Password must match")
                ],
                render_kw={"placeholder": "Confirm Password"}
            )
    submit = f.SubmitField('Sign Up')
    