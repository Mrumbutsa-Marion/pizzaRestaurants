from app import db
from datetime import datetime


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    address = db.Column(db.String(100))
    pizzas = db.relationship('Pizza', backref='restaurant_pizzas')

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    ingredients = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    restaurant = db.relationship('Restaurant', backref='restaurant_pizzas')

class Restaurant_pizzas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    price = db.Column(db.Integer,primary_key=True)
    pizza = db.relationship('Pizza', backref=('restaurant_pizzas'))
    restaurant = db.relationship('Restaurant', backref=('restaurants_pizzas'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
                                                              