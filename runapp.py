from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'Product'
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_qty = db.Column(db.Integer, nullable=False)
    def __init__(self,product_name,product_qty):
        self.product_name = product_name
        self.product_qty = product_qty

class Location(db.Model):
    __tablename__ = 'Location'
    location_id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(100))
    def __init__(self,location_name):
        self.location_name = location_name

class Movement(db.Model):
    __tablename__ = 'Movement'
    movement_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False) 
    timestamp = db.Column(db.String(100), default = datetime.now().strftime('%d-%m-%Y %I:%M %p'))
    product_name = db.Column(db.String(100), nullable=False)
    from_location = db.Column(db.String(100), nullable=False)
    to_location = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    def __init__(self, product_id, product_name, from_location, to_location,move_qty):
        self.product_id = product_id
        self.product_name = product_name
        self.from_location = from_location
        self.to_location = to_location
        self.move_qty = move_qty

def addProduct(product_name, product_qty):
    db.session.add(Product(product_name,product_qty))
    db.session.commit()
    res = Product.query.filter_by()
    for i in res:
        print(f'{i.product_id} ----- {i.product_name} ----- {i.product_qty}')
def addLocation(location_name):
    db.session.add(Location(location_name))
    db.session.commit()
def addMovement(product_name, from_location, to_location, move_qty):
    q = Product.query.filter(Product.product_name == product_name).first()
    product_id = q.product_id
    db.session.add(Movement(product_id, product_name, from_location, to_location, move_qty))
    db.session.commit()
def showTable():
    res = Movement.query.filter_by()
    for i in res:
        print(f'{i.movement_id} ----- {i.timestamp} ----- {i.from_location} ----- {i.to_location} ----- {i.qty}')
def UpdateProduct(existing_product_name, updated_product_name, updated_qty):
    q = Product.query.filter(Product.product_name == existing_product_name).first()
    q.product_name = updated_product_name
    q.product_qty = updated_qty
    db.session.commit()
def UpdateLocation(existing_location_name, updated_location_name):
    q = Location.query.filter(Location.location_name == existing_location_name).first()
    q.location_name = updated_location_name
    db.session.commit()
db.session.close()

############################################################### APP-ROUTE ##################################################################

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Add", methods=['POST','GET'])
def Add():
    if request.method == "POST":
        product_name = request.form["product_name"]
        product_qty = request.form["product_qty"]
        location_name = request.form["location_name"]
        if product_name != '' and product_qty != '':
            addProduct(product_name, product_qty)
        if location_name != '':
            addLocation(location_name)
        return redirect(url_for("home"))
    else:
        return render_template("Add.html")

@app.route("/Edit", methods=['POST','GET'])
def Edit():
    dropdown_product =[i.product_name for i in Product.query.filter_by()]
    dropdown_location =[i.location_name for i in Location.query.filter_by()]
    if request.method == "GET":
        return render_template("Edit.html", dropdown_update_product=dropdown_product, dropdown_update_location=dropdown_location,
                                dropdown_product=dropdown_product, dropdown_from_location=dropdown_location ,dropdown_to_location=dropdown_location)

    elif request.method == "POST":
        if request.form.get("btnupdate"):
            existing_product_name = request.form.get("dropdown_update_product")
            existing_location_name = request.form.get("dropdown_update_location")
            updated_product_name = request.form.get("updated_product_name")
            updated_location_name = request.form.get("updated_location_name")
            updated_qty = request.form.get("updated_qty")
            UpdateProduct(existing_product_name, updated_product_name, updated_qty)
            UpdateLocation(existing_location_name, updated_location_name)
            return redirect(url_for("Edit"))

        else:
            product_name = request.form["dropdown_product"]
            move_qty = request.form["move_qty"]
            from_location = request.form["dropdown_from_location"]
            to_location= request.form["dropdown_to_location"]
            addMovement(product_name, from_location, to_location, move_qty)          
            return redirect(url_for("home"))

@app.route("/View", methods=['POST','GET'])
def View():
    return render_template("View.html")

if __name__ == '__main__':
    app.run(debug=True)