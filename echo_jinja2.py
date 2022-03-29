from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('echo2.html')


@app.route("/echo", methods=['POST'])
def echo():
    return render_template('echo2.html', text=request.form['text'])


if __name__ == "__main__":
    app.run()


# https://jinja.palletsprojects.com/en/3.1.x/templates/