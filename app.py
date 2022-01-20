# Import the required libraries
from flask import Flask, render_template, redirect
from joblib import load

# Load the pipeline object
pipeline = load("logistic_Regression_Model.joblib")

# Start Flask
app =Flask(__name__)

# home page
@app.route("/",  methods=["GET","POST"])
def index():
    if flask.request.method == "GET":
        return(flask.render_template("index.html"))

    if flask.request.method == "POST":
        article = flask.request.form["Contents"]

        prediction = pipeline.predict(article)[0]

    return render_template("index.html",result=prediction)

# main
if __name__ == "__main__":
    app.run(debug = True)
