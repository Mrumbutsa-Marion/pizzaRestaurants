from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///pizzas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db=SQLAlchemy(app)

def create_app(): 

    db.init_app(app)

    
    # add routes
    from app import routes

    return app


   