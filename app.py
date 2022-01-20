from flask import Flask, render_template, redirect

app =Flask(__name__)

# db = {connection goes here}


# home page
@app.route("/")
def index():
    return "This is the home page"

    # return render_template("index.html")

# main
if __name__ == "__main__":
    app.run(debug = True)
