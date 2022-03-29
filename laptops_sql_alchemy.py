from flask import Flask, jsonify, request


app = Flask(__name__)
app.config["DEBUG"] = True

from sqlalchemy import create_engine
engine = create_engine('postgresql://deeptalk:deeptalk@localhost/laptops', echo=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

from sqlalchemy.orm import declarative_base
Base = declarative_base()
# id, product_name, type_name, inches, resolution_w, resolution_h, cpu, ram_gb, mem_flash_gb, gpu, os, weight_kg, price_euro, stock_amnt, is_deleted, manufacturer_id, mem_hdd_gb, mem_hybrid_gb, mem_ssd_gb
from sqlalchemy import Column, Integer, String, Float, Boolean
class Laptop(Base):
    __tablename__ = 'laptops'
    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    type_name = Column(String)
    inches = Column(Float)
    resolution_w = Column(String)
    resolution_h = Column(String)
    cpu = Column(String)
    ram_gb = Column(Float)
    mem_flash_gb = Column(Float)
    gpu = Column(String)
    os = Column(String)
    weight_kg = Column(Float)
    price_euro = Column(Float)
    stock_amnt = Column(Integer)
    is_deleted = Column(Boolean)
    manufacturer_id = Column(Integer)
    mem_hdd_gb = Column(Float)
    mem_hybrid_gb = Column(Float)
    mem_ssd_gb = Column(Float)

    def __repr__(self):
        return f"Laptop: {self.product_name}"

import json
from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

@app.route('/laptops', methods=['GET'])
def laptops():
    session = Session()
    ret_list = session.query(Laptop).all()
    return json.dumps(ret_list, cls=AlchemyEncoder)
    # return jsonify(ret_list)

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