from flask import Blueprint
from flask import render_template
from app.db import mongo

newsPage_bp = Blueprint('newsPage_bp', __name__)  

@newsPage_bp.route('/<channelname>/<articleId>')
def newsPage(channelname, articleId):
    articleId = int(articleId)
    db = mongo.cx['newChannels']
    res = db.newschannel.find( { 'name': channelname }, { "articles" : { '$slice': [articleId, 1] } } )
    res = list(res)
    
    # [] -> {} transformation
    if res :
        res = res[0]
    return render_template( 'newsPage.html', article = res )