import json

import flask
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True

# Connect to an existing database
conn = psycopg2.connect(
    host="localhost",
    database="laptops",
    user="deeptalk",
    password="deeptalk")

@app.route('/laptops', methods=['GET'])
def laptops():
    # Open a cursor to perform database operations
    cur = conn.cursor()
    cur.execute('SELECT * FROM laptops')

    column_names = [desc[0] for desc in cur.description]
    print(column_names)
    results = cur.fetchall()

    cur.close()

    print(f"Results type: {type(results[:5])}")
    print(f"Results: {results[:-1]}")

    ret_list = []
    for res in results:
        res_dict = {}

        for col, res_field in zip(column_names, res):
            res_dict[col] = res_field

        ret_list.append(res_dict)
        # Can we move this line after res_dict = {} ?

    # return results

    # return jsonify(results)
    return jsonify(ret_list)

@app.route('/laptops/<laptop_id>', methods=['GET'])
def laptop_details(laptop_id):
    return f"This will be the details of {laptop_id}"

@app.route('/laptops', methods=['POST'])
def add_laptop():
    # record = json.loads(request.data)
    cur = conn.cursor()
    cur.execute("INSERT INTO laptops (id, product_name, type_name, inches, resolution_w, resolution_h, cpu, ram_gb, mem_flash_gb, gpu, os, weight_kg, price_euro, stock_amnt, is_deleted, manufacturer_id, mem_hdd_gb, mem_hybrid_gb, mem_ssd_gb) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (10000, 'MacBook Pro111', 'Ultrabook', 15.4, 2880, 1800, 'Intel Core i7 2.7GHz', 6, None, 'AMD Radeon Pro 455', 'macOS', 1.83, 2537.45, 4, False, 4, None, None, None))
    conn.commit()
    cur.close()

