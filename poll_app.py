import json
import threading

from flask import Flask, request, render_template

app = Flask(__name__)
lock1 = threading.Lock()


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/poll", methods=['POST'])
def poll():
    with lock1:
        picked = request.form['fav_language']
        with open("results.json", "r+") as openfile:
            try:
                results_dict = json.load(openfile)
            except:
                results_dict = {'DJANGO': 0, 'FLASK': 0}
            if picked == "DJANGO":
                results_dict["DJANGO"] = results_dict["DJANGO"] + 1
            else:
                results_dict["FLASK"] = results_dict["FLASK"] + 1
            json_object = json.dumps(results_dict)
            openfile.write(json_object)
            # with open("results.json", "w") as outfile:
            #     outfile.write(json_object)

    return render_template('home.html', radio=request.form['fav_language'])


@app.route("/results")
def results():
    with open("results.json", "r") as openfile:
        results_dict = json.load(openfile)
    return render_template('results.html', results=results_dict)


if __name__ == "__main__":
    app.run()