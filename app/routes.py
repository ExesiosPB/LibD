from flask import render_template, jsonify
from app import app
from app.socials.flikr import getFlickr
from app.news.news import getNews

@app.route('/')
@app.route('/index')
def index():
  flikrData = getFlickr()
  return jsonify(flikrData)

@app.route('/news')
def news():
  news = getNews()
  return jsonify(news)