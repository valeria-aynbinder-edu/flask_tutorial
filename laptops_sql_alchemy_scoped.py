# https://flask-sqlalchemy-session.readthedocs.io/en/v1.1/
import flask
from flask import Flask, jsonify, request
import json
from flask_sqlalchemy_session import flask_scoped_session


from models import Laptop, AlchemyEncoder

app = Flask(__name__)
app.config["DEBUG"] = True


from sqlalchemy import create_engine
engine = create_engine('postgresql://deeptalk:deeptalk@localhost/laptops', echo=True)

from sqlalchemy.orm import sessionmaker
session_factory = sessionmaker(bind=engine)

session = flask_scoped_session(session_factory, app)

# id, product_name, type_name, inches, resolution_w, resolution_h, cpu, ram_gb, mem_flash_gb, gpu, os, weight_kg, price_euro, stock_amnt, is_deleted, manufacturer_id, mem_hdd_gb, mem_hybrid_gb, mem_ssd_gb



@app.route('/laptops', methods=['GET'])
def laptops():
    ret_list = session.query(Laptop).all()
    return json.dumps(ret_list, cls=AlchemyEncoder)


@app.route('/laptops/<laptop_id>', methods=['GET'])
def laptop_details(laptop_id):
    return f"This will be the details of {laptop_id}"

@app.route('/laptops', methods=['POST'])
def add_laptop():
    pass

# dataclasses?
# https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json

# scoped session
# https://flask-sqlalchemy-session.readthedocs.io/en/v1.1/