from flask import jsonify
from flask_restful import Resource
from . import api
from app.db import mongo
from datetime import datetime

class Weather(Resource):
    def get(self):
        weather_db = mongo.cx['weather']

        res = weather_db.weather.find({"date": {"$gte": datetime.utcnow()}}).limit(4)
        output = []
        for data in res:
            data['_id'] = str(data['_id'])
            output.append(data)
        return jsonify(output)
    
api.add_resource(Weather, '/weather')
