from flask_pymongo import PyMongo
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

mongo = PyMongo()
mysql = MySQL()
bcrypt = Bcrypt()
jwt = JWTManager()