from flask import render_template
from app import app
from app.socials.flikr import getFlickr
import sys

@app.route('/')
@app.route('/index')
def index():
  getFlickr()
  return render_template('index.htm')