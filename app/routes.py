from app import app, db
from flask import request, jsonify, make_response
from app.models import Restaurant, Pizza

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



@app.route('/restaurants/<int:id>')
def get_restaurants_by_id(id):
    restaurants = Restaurant.query.get(id)
    if not restaurants:
        return jsonify({"error": "Restaurant not found"}), 404
    
    # Create a list that will store the pizza data inside the restaurants.pizzas
    pizzas = []
    for pizza in restaurants.pizzas:
        pizza_data = {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }
        pizzas.append(pizza_data)

    restaurant_data = {
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': pizzas
    }

    return jsonify(restaurant_data)
# Set up the application context
with app.app_context():
    restaurants = [
        Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue'),
        Restaurant(name='Pizza Hut', address='Westgate Mall, Mwanzi Road, Nrb 100'),
        Restaurant(name='Mcdonald Pizaa', address='Imaradaima Mall, Mombasa rd')
    ]

    # Check if the third restaurant already exists in the database
    restaurant = Restaurant.query.filter_by(name=restaurants[2].name).first()

    # If the third restaurant does not exist in the database, add it
    if restaurant is None:
        db.session.add(restaurants[2])
    else:
        # If the third restaurant already exists in the database, do nothing
        pass

    db.session.commit()

print('Database seeded successfully.')