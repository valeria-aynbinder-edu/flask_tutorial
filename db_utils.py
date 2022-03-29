#!/usr/bin/python
import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="laptops",
    user="deeptalk",
    password="deeptalk")


# from sqlalchemy import create_engine
# engine = create_engine('postgresql://deeptalk:deeptalk@localhost/weather', echo=True)


