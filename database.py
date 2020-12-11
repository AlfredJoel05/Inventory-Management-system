from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

def DB():
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
    DB.db.session.add(DB.Product(product_name,product_qty))
    DB.db.session.commit()
    res = DB.db.Product.query.fetchall()
    for i in res:
        print(f'{i.product_id} ----- {i.product_name} ----- {i.product_qty}')
def addLocation(location_name):
    DB.db.session.add(DB.Location(location_name))
def showTable(movement_table):
    res = DB.Movement.query.fetchall()
    for i in res:
        print(f'{i.movement_id} ----- {i.timestamp} ----- {i.from_location} ----- {i.to_location} ----- {i.qty}')


