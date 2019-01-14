from flask import render_template, jsonify

from app import app
from app.socials.flikr import getFlickr
from app.socials.twitter import getTweets
from app.socials.instagram import getInstagram
from app.news.news import getNews
import app.socials.foursquare as foursquare

@app.route('/')
@app.route('/index')
def index():
  return 'Home'

# URL: /news/SOME_SEARCH_PARAM
# Returns JSON off all news articles about the entered seach_param
#
# e.g /news/Stoke-On-Trent
# {
#   'status': 'ok'
#   'totalResults: 2394,
#   'articles': [
#     .
#     .
#   ]
# }
@app.route('/news/<string:search_param>')
def news(search_param):
  news = getNews(search_param)
  return jsonify(news)

# Routes for getting Social Media Data
# /social
#   /twitter/SOME_SEARCH_PARAM
#   /flikr/SOME_SEARCH_PARAM
#   /instagram/SOME_SEACH_PARAM
#   /foursquare/searchvenue/SOME_SEARCH_PARAM
@app.route('/social/twitter/<string:search_param>')
def twitter(search_param):
  tweets = getTweets(search_param)
  return jsonify(tweets)

@app.route('/social/flikr/<string:search_param>')
def flikr(search_param):
  flikr = getFlickr(search_param)
  return jsonify(flikr)

@app.route('/social/instagram/<string:search_param>')
def instagram(search_param):
  instagram = getInstagram(search_param)
  return jsonify(instagram)

@app.route('/social/foursquare/searchvenue/<string:search_param>')
def foursquareSearchVenue(search_param):
  venues = foursquare.venuSearch(search_param)
  return jsonify(venues)

@app.route('/social/foursquare/venuPhotos/<string:venu_id>')
def foursquareVenuPhotos(venu_id):
  venues = foursquare.venuPhotos(venu_id)
  return jsonify(venues)