from flask import Flask, render_template, request, redirect, url_for
import database as db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Add", methods=['POST','GET'])
def Add():
    if request.method == "POST":
        Product_name = request.form["Product_name"]
        Location_name = request.form["Location_name"]
        return redirect(url_for("home"))
    else:
        return render_template("Add.html")

@app.route("/Edit", methods=['POST','GET'])
def Edit():
    return render_template("Edit.html")

@app.route("/View", methods=['POST','GET'])
def View():
    return render_template("View.html")

if __name__ == '__main__':
    app.run(debug=True)