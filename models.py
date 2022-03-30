import json

from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, DeclarativeMeta

Base = declarative_base()

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
