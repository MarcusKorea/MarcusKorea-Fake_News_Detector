# Import the required libraries
from flask import Flask, render_template, redirect, request
#from joblib import load
import pickle

# Load the pipeline object
vectorizor = load("vectorizor.joblib")
model = load("logistic_Regression_Model.joblib")

#Loading vectoriser
vectorizor = pickle.load(open("vect.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))

# Start Flask
app =Flask(__name__)

# home page
@app.route("/",  methods=["GET","POST"])
def index():
    if request.method == "GET":
        return(render_template("index.html"))

    if request.method == "POST":
        article = request.form["Contents"]
        print(article)

        #prediction = pipeline.predict(article)[0]

    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    print("hohohohohoho")
    if request.method == 'POST':
        message = [str(x) for x in request.form.values()][0]
        data = [message]
        #print(message)
        print("***************************")
        vect = vectorizor.transform(data).toarray()
        print(vect.shape)
        prediction = model.predict(vect)
        print("**************PREDICTION***************",prediction)
    return render_template('index.html')

# main
if __name__ == "__main__":
    app.run(debug = True)
