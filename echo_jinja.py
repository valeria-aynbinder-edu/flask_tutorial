from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('echo.html')

@app.route("/echo", methods=['POST'])
def echo():
    return "You said: " + request.form['text']


if __name__ == "__main__":
    app.run()