from flask import redirect, url_for, session, flash
from app.db import mysql
from app.db import mongo
from app.db import bcrypt

def signIn(signInForm) -> bool: 
    if signInForm.validate_on_submit():
        con = mysql.connection
        cur = con.cursor()
        cur.execute(f"select * from users where email = '{signInForm.signInEmail.data}' ")

        # if email found in database
        if cur.rowcount != 0:
           # email found -> fetch record -> check password field with hash in db
            res = cur.fetchone()
            if bcrypt.check_password_hash(res['hashed_password'], signInForm.signInPassword.data) :
            # if email and password matched -> login
                print("Logged In successfully")
                session['_id'] = res['id']
                session['username'] = res['username']
                session['email'] = res['email']
                session['following'] = {'newschannels': [], 'states': [], 'countries': []}
                
                db = mongo.cx['newChannels']
                res = db.follow.find({'_id': res['id']})
                res = list(res)
                
                if res and res[0].get('following', None):
                    session['following'] = res[0]['following']

                print(session['following'])
                return True
       
            # if email not found or password does not match
            signInForm.signInEmail.errors = ['Either email or password is wrong']
            signInForm.signInPassword.errors = ['Either email or password is wrong']
        else:
            signInForm.signInEmail.errors = ['Email not registered with Us']
            
        return False

def signUp(signUpForm) -> bool:
    if signUpForm.validate_on_submit():
        con = mysql.connection
        cur = con.cursor()
        cur.execute(f" Select * from users where email = '{signUpForm.signUpEmail.data}' ")

        # if email already exists then generate errors
        if cur.rowcount != 0:
            signUpForm.signUpEmail.errors = ['Email already exists']
            print("Email already exists - Sign up")
        else:
            # successfully created
            flash("Account Created Successfully", "success")
            hashed_password = bcrypt.generate_password_hash(signUpForm.signUpPassword.data).decode('utf-8')
            cur.execute(f"insert into users(username, email, hashed_password) values ('{signUpForm.username.data}','{signUpForm.signUpEmail.data}','{hashed_password}')")
            con.commit()
            # Clearing the field
            signUpForm.signUpEmail.data = ''
            signUpForm.username.data = ''
            return False
    return True