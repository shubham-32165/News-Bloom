from flask import render_template
from app.db import mongo

def newsShowCase():
    return render_template( "NewsShowCasePage/index.html" )

def channelList(channelName):
    db = mongo.cx['newChannels']
    res = db.newschannel.find({'name': channelName}, {'name': 1})
    res = list(res)
    if res:
        res = str(res[0]['_id'])
    else:
        res = '68136dbd5b7a16770d7f56d5'
    
    print(res)

    return render_template("NewsShowCasePage/channel.html", channelName = channelName, channelId = res)