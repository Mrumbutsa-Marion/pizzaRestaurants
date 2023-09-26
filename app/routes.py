from app import app, db
from flask import request, jsonify, make_response
from app.models import Restaurant, Pizza, Restaurant_pizzas


#!.) The /restaurants route returns a list of all the restaurants in the database
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
            'address': restaurant.address,
            'pizzas': get_pizzas(restaurant.pizzas)
        }
        restaurant_list.append(restaurant_data)

    return jsonify(restaurant_list)

#2.) The/pizzas route returns a list of all the pizzas in the database.
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    # Logic to fetch pizzas from the database
    pizzas = Pizza.query.all()

    # Create a list to store the pizza data
    pizza_list = []
    for pizza in pizzas:
        pizza_data = {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }
        pizza_list.append(pizza_data)

    return jsonify(pizza_list)

#3.) The /restaurants/<int:id> route returns an id of a single restaurant in the database.
app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurants_by_id(id):
    restaurant = Restaurant.query.get(id)
    restaurant_data = {
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': get_pizzas(restaurant.pizzas)
    }
    return jsonify(restaurant_data)

#4.) The /restaurant_pizzas creates a new RestaurantPizza that is associated with an existing Pizza and Restaurant route.
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data['price']
    pizza_id = data['pizza_id']
    restaurant_id = data['restaurant_id']

    # Create a new restaurant_pizza record
    restaurant_pizza = Restaurant_pizzas(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

    # Fetch the  pizza details requested
    pizza = Pizza.query.get(pizza_id)

    pizza_data = {
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    }

    return jsonify(pizza_data), 201





#Ading Istances 
with app.app_context():
      # Create the pizzas list
    pizzas = [
        Pizza( name ='Cheese',ingredients = 'Dough, Tomato Sauce, Cheese'),
        Pizza( name ='Chicken',ingredients = 'Dough, Tomato Sauce, Cheese, Pepperoni')
    ]
    pizza = Pizza.query.filter_by(name=pizzas[1].name).first()

    # Check if the pizza object is None
    if pizza is not None:
        # If the pizza object is not None, print the pizza's name
        db.session.add(pizzas[1])
    else:
        # If the pizza object is None, print a message saying that the pizza does not exist
        print('The pizza does not exist.')
        db.session.commit()

    # Create the restaurants list
    restaurants = [
        Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue'),
        Restaurant(name='Pizza Hut', address='Westgate Mall, Mwanzi Road, Nrb 100'),
        Restaurant(name='Mcdonald Pizaa', address='Imaradaima Mall, Mombasa rd'),
        Restaurant(id=1, name='My Restaurant', address='My Address')
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



