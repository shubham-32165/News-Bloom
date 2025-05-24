from flask import jsonify, request, session
from flask_restful import Resource
from . import api
from app.db import mongo
from flask_jwt_extended import jwt_required

class following(Resource):
    def delete(self):

        data = request.get_json()
        name = data['name']
        category = data['category']

        db = mongo.cx['newChannels']

        if category == 'states':
            session['following'] = {
                'states': [ x for x in session['following'].get('states',[]) if name != x ],
                'countries': session['following'].get('countries',[]),
                'newschannels': session['following'].get('newschannels',[])
            }
        elif category == 'countries':
            session['following'] = {
                'countries': [ x for x in session['following'].get('countries',[]) if name != x ],
                'states': session['following'].get('states',[]),
                'newschannels': session['following'].get('newschannels',[])
            }
        elif category == 'newschannels':
            session['following'] = {
                'newschannels': [ x for x in session['following'].get('newschannels',[]) if name != x ],
                'countries': session['following'].get('countries',[]),
                'states': session['following'].get('states',[])
            }
        else:
            return {'message': 'bad request'}, 403
        
        db.follow.update_one( {'_id': session['_id']}, {'$pull': {f'following.{category}' : name} } )
        return {'message': 'done'}, 200
        
api.add_resource(following, '/following')