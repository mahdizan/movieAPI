from flask import Flask
from pandas import read_csv

app = Flask(__name__)

@app.route('/')


def my_reco():
    
    return "hi"

