from flask import render_template, make_response, session
from app.db import mongo


def world():
    return render_template( "World_Route_Page/World.html")

def country(country):
    db = mongo.cx['newChannels']
    res = db.countries.find({'name': country}, {'name': 1, 'capital': 1})
    res = list(res)

    if not session.get('state', []):
        countries = list( db.countries.find({'name': country}, {'_id': 0, 'states': 1 }) )
        session['states'] = (countries if countries else [[]])[0].get('states', [])
        session['state'] = ( [res[0]['capital'], country] if res and res[0].get('capital', 'Capital') else ['Capital', country] )
    elif session.get('state', [None, None])[1] != country:
        countries = list( db.countries.find({'name': country}, {'_id': 0, 'states': 1 }) )
        session['states'] = (countries if countries else [[]])[0].get('states', [])
        session['state'] = ( [res[0]['capital'], country] if res and res[0].get('capital', 'Capital') else ['Capital', country] )
        
    session['country'] = country
    countries = db.countries.find({}, {'name':1, 'capital':1})
    # list pf objects [_id, name, capital]
    countries = list(countries)
    res = make_response(render_template( "World_Route_Page/Country.html", country = country, countries=countries ))
    return res

def locale(country, state):
    db = mongo.cx['newChannels']
    res = db.countries.find({'name': country})
    res = list(res)
    if res :
        res = res[0].get('states',[])
    
    session['state'] = [state, country]
    return render_template( "World_Route_Page/Locale.html", country = country, state = state, states = res )