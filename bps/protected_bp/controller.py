from flask import render_template, redirect, url_for, flash
from app.db import mongo
from app.news_utils import fetch_news_by_query


def following():
    return render_template( "FollowingPage/index.html")

def forYou():
    topics = ['Mysore', 'India', 'World', 'Cricket']
    news_data = {topic: fetch_news_by_query(topic) for topic in topics}
    return render_template("ForYou/index.html", news_data=news_data)



def unauthorized_fallback(callback):
    flash("Login to Access This Page", "danger")
    return redirect(url_for('main.index'))