import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine=create_engine('sqlite:///hawaii.sqlite')
#mapped the engine to the base
Base= automap_base()
Base.prepare(engine,reflect=True)

#FLASK SETUP
app=Flask(__name__)
Measurement= Base.classes.measurement
Station= Base.classes.station
#listing all available routes
@app.route('/')
def list_routes():
    return(
        f'Available Routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
    )
@app.route('/api/v1.0/precipitation')
def precip():
    session= Session(engine)
    results= session.query(Measurement.date,Measurement.prcp).all()
    session.close()
    

@app.route('/api/v1.0/stations')
def station_list():
    session= Session(engine)
    results= session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    all_precips=[]
    for date,precip in results:
        precip_dict={}
        precip_dict['date']= date 
        precip_dict['precipitation']=precips
        all_precips.append(precip_dict)
    return jsonify(all_precips)
    
@app.route('/api/v1.0/tobs')
    session=Session(engine)
    most_active=session.query(measurement)


@app.route('/api/v1.0/<start>')
    def start(start):
        end= ''
        return jsonify(date(start,end)
    

    

@app.route('/api/v1.0/<start>/<end>')
    def start_end(start,end):
        return jsonify(date(start,end)


if __name__=='__main__':
    app.run(debug=True)
print ('works')