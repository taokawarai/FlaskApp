from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
  if request.method == 'GET':
    return render_template("base.html")
  elif request.method == 'POST':
    weight = request.form["weight"]
    if weight:
      water = str(float(weight) * 35)
      return render_template('base.html', water = water)
    return render_template("base.html")