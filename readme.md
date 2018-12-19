# LibD

## What is LibD

LibD is Exesios PB data scraper library.

A RESTful API where requests with parameters can be passed to the library, it returns responses based on data scraped from sources

## Install

- Requires Python 3+

- Setup python VE `python -m venv venv`
- Run VE `source venv/bin/activate`
  - For Windows `venv\Scripts\activate`
- Then install python modules `pip install -r requirements.txt`
- Set FLASK_APP env variable `export FLASK_APP=libd.py`
  - For windows `set FLASK_APP=libd.py`
- Then run `python -m flask run`

Runs the application at `http://localhost:5000/`