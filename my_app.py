from flask import Flask
from pandas import read_csv

app = Flask(__name__)

@app.route('/')
def my_reco():
    df = read_csv(r'C:\Users\Mah\my_reco.csv', sep=',', encoding='utf8', low_memory=False)
    head = df.head()
    return head

