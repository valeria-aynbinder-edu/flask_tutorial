from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return '<form action="/echo" method="POST"><input name="text"><input type="submit" value="Echo"></form>'

@app.route("/echo", methods=['POST'])
def echo():
    return "You said: " + request.form['text']
    # return "You said: " + request.form.get('text', "")


if __name__ == "__main__":
    app.run()

# note http://127.0.0.1:3000/echo -> not allowed
# curl --data '' http://127.0.0.1:3000/echo => triggers bad request (400)

# recommended:
#request.args.get('key', '') for GET
#request.form['key'] for POST with form