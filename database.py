# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# app = Flask(__name__)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
# db = SQLAlchemy(app)

# class Product(db.Model):
#     product_id = db.Column(db.Integer, primary_key=True)
#     product_name = db.Column(db.String(100),unique=True)
#     product_qty = db.Column(db.Integer)
#     def __init__(self,product_name,product_qty):
#         self.product_name = product_name
#         self.product_qty = product_qty
# class Location(db.Model):
#     location_id = db.Column(db.Integer, primary_key=True)
import sqlite3
import pandas as pd

conn = sqlite3.connect('inventory.db')
c = conn.cursor()

res = c.execute("SELECT * FROM Movement");
# df = pd.DataFrame(res, columns = ['Product_id','Product_Name','Product_QTY'])
# df = pd.DataFrame(res, columns = ['Location_id','Location_Name'])
df = pd.DataFrame(res, columns = ['movement_id','product_id', 'timestamp', 'product_name', 'from_location', 'to_location', 'move_qty'])
print(df)

#commit the changes to db			
conn.commit()
#close the connection
conn.close()
