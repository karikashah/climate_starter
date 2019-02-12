# ---------------------- STEP 2: Climate APP

from flask import Flask, json, jsonify
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect

engine = create_engine("sqlite:///./Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__) # the name of the file & the object (double usage)

@app.route("/")
def home():
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

#    Return the JSON representation of your dictionary
@app.route('/api/v1.0/precipitation/')
def precipitation():
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
    last_year = dt.datetime.strptime(last_date, '%Y-%m-%d') - dt.timedelta(days=365)

    rain_results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= last_year).\
    order_by(Measurement.date).all()

    p_dict = dict(rain_results)
    print()
    print("Results for Precipitation")
    return jsonify(p_dict) 

#    Return a JSON-list of stations from the dataset.
@app.route('/api/v1.0/stations/')
def stations():
    station_list = session.query(Station.station)\
    .order_by(Station.station).all() 
    print()
    print("Station List:")   
    for row in station_list:
        print (row[0])
    return jsonify(station_list)

#    Return a JSON-list of Temperature Observations from the dataset.
@app.route('/api/v1.0/tobs/')
def tobs():
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
    last_year = dt.datetime.strptime(last_date, '%Y-%m-%d') - dt.timedelta(days=365)

    temp_obs = session.query(Measurement.tobs)\
        .filter(Measurement.date >= last_year)\
        .order_by(Measurement.date).all()
    print()
    print("Temperature Results for All Stations")
    return jsonify(temp_obs)

if __name__ == "__main__":
    app.run(debug=True)