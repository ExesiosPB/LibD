from flask import render_template, jsonify
from app import app
from app.socials.flikr import getFlickr

@app.route('/')
@app.route('/index')
def index():
  flikrData = getFlickr()
  return jsonify(flikrData)