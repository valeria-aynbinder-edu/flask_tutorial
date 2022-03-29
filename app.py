import json

from flask import Flask, request


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    print(request)
    return "Welcome to LaptopsApp!"


@app.route('/laptops', methods=['GET'])
def laptops():
    return "Laptops page"


@app.route('/laptops/<laptop_id>', methods=['GET'])
def laptop_details(laptop_id):
    return f"This will be the details of {laptop_id}"


@app.route('/laptop', methods=['POST'])
def add_laptop():
    data = json.loads(request.data)
    print(data)
    return


if __name__ == '__main__':
    app.run()


#running from terminal: FLASK_APP=app flask run --port 3000