import pandas as pd

import plotly.graph_objects as go

from flask import (
    Flask,
    render_template,
    jsonify
)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/Legalization.sqlite"

db = SQLAlchemy(app)

class Mjuse(db.Model):
    __tablename__ = 'mjuse'

    id = db.Column(db.Integer)
    state = db.Column(db.String, primary_key=True)
    abbr = db.Column(db.String)
    legalization_status89 = db.Column(db.Integer)
    legalization_status1617 = db.Column(db.Integer)
    Age1217_89 = db.Column(db.Float)
    Age1217_1617 = db.Column(db.Float)
    Age18_89 = db.Column(db.Float)
    Age18_1617 = db.Column(db.Float)
    
    def __repr__(self):
        return '<Legalization_Data %r>' % (self.name)

@app.before_first_request
def setup():
    db.create_all() 

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

@app.route("/use_data")
def use_data():
   
    # Query for the top 10 emoji data
    results = db.session.query(Mjuse.id, Mjuse.state, Mjuse.abbr, Mjuse.legalization_status89, Mjuse.legalization_status1617, Mjuse.Age1217_89, Mjuse.Age1217_1617, Mjuse.Age18_89, Mjuse.Age18_1617).all()
    df = pd.DataFrame(results, columns=['id', 'state', 'abbr', 'legalization_status89', 'legalization_status1617', 'Age1217_89', 'Age1217_1617', 'Age18_89', 'Age18_1617'])

    df.to_csv(r'data\data.csv')