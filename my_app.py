from flask import Flask
from pandas import read_csv

app = Flask(__name__)

@app.route('/')


if os.environ.get('DATABASE_URL') is None:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

def my_reco():
    df = read_csv(r'C:\Users\Mah\my_reco.csv', sep=',', encoding='utf8', low_memory=False)
    head = df.head()
    return head

