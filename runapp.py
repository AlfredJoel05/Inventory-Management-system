from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_qty = db.Column(db.Integer, nullable=False)
    def __init__(self,product_name,product_qty):
        self.product_name = product_name
        self.product_qty = product_qty
class Location(db.Model):
    location_id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(100))
    def __init__(self,location_name):
        self.location_name = location_name

class Movement(db.Model):
    movement_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default = datetime.now().strftime('%d-%m-%Y %I:%M %p'))
    from_location = db.Column(db.String(100), nullable=False)
    # prod_id = relationship("product_id", back_populates="Product")
    to_location = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
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
    db.session.commit()
def showTable(movement_table):
    res = Movement.query.filter_by()
    for i in res:
        print(f'{i.movement_id} ----- {i.timestamp} ----- {i.from_location} ----- {i.to_location} ----- {i.qty}')
def UpdateProduct(existing_product_name, updated_product_name):
    q = Product.query.filter(Product.product_name == existing_product_name).first()
    q.product_name = updated_product_name
    print(q.product_name)
    db.session.commit()

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
            existing_product_name = request.form["dropdown_update_product"]
            existing_location_name = request.form["dropdown_update_location"]
            updated_product_name = request.form["updated_product_name"]
            updated_location_name = request.form["updated_location_name"]
            UpdateProduct(existing_product_name, updated_product_name)
            return redirect(url_for("Edit"))

        else:
            product_name = request.form["dropdown_product"]
            move_qty = request.form["move_qty"]
            from_location = request.form["dropdown_from_location"]
            to_location= request.form["dropdown_to_location"]
            print(product_name, from_location, to_location, move_qty)
            return redirect(url_for("home"))

@app.route("/View", methods=['POST','GET'])
def View():
    return render_template("View.html")

if __name__ == '__main__':
    app.run(debug=True)