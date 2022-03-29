from flask import Flask, request, render_template
from werkzeug.exceptions import abort

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404


@app.route("/")
def home():
    return render_template('echo2_static.html')

@app.route("/user/<int:id>")
def user(id):
    if id not in (1, 5):
        abort(404)
    return f"User {id} page"


@app.route("/echo", methods=['POST'])
def echo():
    return render_template('echo2_static.html', text=request.form['text'])


if __name__ == "__main__":
    app.run()
