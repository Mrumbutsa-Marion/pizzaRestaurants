from app import app, db
from flask import request, jsonify, make_response
from app.models import Restaurant

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    #Fetch restaurants from the database
    restaurants = Restaurant.query.all()

    # Create a list that will store the restaurant data
    restaurant_list = []
    for restaurant in restaurants:
        restaurant_data = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
        restaurant_list.append(restaurant_data)

    return jsonify(restaurant_list)


# Seed the database

