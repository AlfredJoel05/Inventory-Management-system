from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    product_qty = db.Column(db.Integer)
    def __init__(self,product_name,product_qty):
        self.product_name = product_name
        self.product_qty = product_qty
class Location(db.Model):
    location_id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(100))
    def __init__(self,location_name):
        self.product_name = location_name

class Movement(db.Model):
    movement_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default = datetime.now().strftime('%d-%m-%Y %I:%M %p'))
    from_location = db.Column(db.String(100))
    to_location = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    def __init__(self,from_location,to_location,quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.quantity = quantity

def addProduct(product_name, product_qty):
    db.session.add(Product(product_name,product_qty))
    db.session.commit()
    res = Product.query.filter_by()
    for i in res:
        print(f'{i.product_id} ----- {i.product_name} ----- {i.product_qty}')
def addLocation(location_name):
    db.session.add(Location(location_name))
def showTable(movement_table):
    res = Movement.query.filter_by()
    for i in res:
        print(f'{i.movement_id} ----- {i.timestamp} ----- {i.from_location} ----- {i.to_location} ----- {i.qty}')

####### APP-ROUTE #####

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Add", methods=['POST','GET'])
def Add():
    if request.method == "POST":
        product_name = request.form["product_name"]
        product_qty = request.form["product_qty"]
        location_name = request.form["location_name"]
        addProduct(product_name, product_qty)
        addLocation(location_name)
        return redirect(url_for("home"))
    else:
        return render_template("Add.html")

@app.route("/Edit", methods=['POST','GET'])
def Edit():
    if request.method == "GET":
        dropdown =[i.product_name for i in Product.query.filter_by()]
        return render_template("Edit.html", dropdown=dropdown)
    else:
        return render_template("Edit.html")

@app.route("/View", methods=['POST','GET'])
def View():
    return render_template("View.html")

if __name__ == '__main__':
    app.run(debug=True)