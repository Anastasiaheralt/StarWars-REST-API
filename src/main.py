"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Starships, Favorite_people, Favorite_planets, Favorite_starships
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#User
@app.route('/user', methods=['GET'])
def get_user():
    User = User.query.all()
    User = list(map(lambda x: x.serialize(),User))
    return jsonify(User), 200

#GET User
@app.route("/user/<int:user_id>/favorite", methods=['GET'])
def get_user_favorite(user_id):
    user = User.query.get(user_id)
    people = user.get_people()
    planets = user.get_planets()
    starships = user.get_starships()

    return jsonify({
        "people": people,
        "planets": planets,
        "starships": starships
    }), 200

#POST User
@app.route("/user", methods=['POST'])
def create_user():
    user = User()
    user.email = request.json.get('email')
    user.password = request.json.get('password')
    user.save()
    
    return jsonify(user.serialize()), 201

@app.route("/user/<int:user_id>/favorite_planets", methods=['POST'])
def create_favorite_planets(user_id):
    favorite_planets = FavoritePlanets()
    favorite_planets.user_id = user_id
    favorite_planets.planets_id = request.json.get('planets_id')
    favorite_planets.save()
    
    return jsonify(favorite_planets.serialize()), 201

@app.route("/user/<int:user_id>/favorite_starships", methods=['POST'])
def create_favorite_starships(user_id):
    favorite_starships = FavoriteStarships()
    favorite_starships.user_id = user_id
    favorite_starships.starships_id = request.json.get('starships_id')
    favorite_starships.save()
    
    return jsonify(favorite_starships.serialize()), 201


@app.route("/user/<int:user_id>/favorite_people/<int:favorite_people_id>", methods=['DELETE'])
def delete_favorite_people(user_id, favorite_people_id):
     favorite_people = FavoritePeople.query.get(favorite_people_id)
     favorite_people.delete()

     return jsonify(favorite_people.serialize()), 201

@app.route("/user/<int:user_id>/favorite_planets/<int:favorite_planets_id>", methods=['DELETE'])
def delete_favorite_planets(user_id, favorite_planets_id):
    favorite_planets = FavoritePlanets.query.get(favorite_planets_id)
    favorite_planets.delete()

    return jsonify(favorite_planets.serialize()), 201

@app.route("/user/<int:user_id>/favorite_starships/<int:favorite_starships_id>", methods=['DELETE'])
def delete_favorite_starships(user_id, favorite_starships_id):
    favorite_starships = FavoriteStarships.query.get(favorite_starships_id)
    favorite_starships.delete()

    return jsonify(favorite_starships.serialize()), 201

#People
@app.route('/people', methods=['GET'])
def get_people():
    all_Peoples = People.query.all()
    all_Peoples = list(map(lambda x: x.serialize(), all_Peoples))
    return jsonify(all_Peoples), 200

@app.route('/people/<int:id>', methods=['GET'])
def people_id(id):
    People_id = People.query.get(id)
    return jsonify(People_id.serialize())

@app.route("/user/<int:user_id>/favorite_people", methods=['POST'])
def create_favorite_people(user_id):
    favorite_people = FavoritePeople()
    favorite_people.user_id = user_id
    favorite_people.people_id = request.json.get('people_id')
    favorite_people.save()
    db.session.add(favorite)
    db.session.commit()

    return jsonify(favorite_people.serialize()), 201

@app.route("/people", methods=['POST'])
def createPeople():
    people = Person()
    people.name = request.json.get('name')
    people.height = request.json.get('height')
    people.mass = request.json.get('mass')
    people.hair_color = request.json.get('hair_color')
    people.skin_color = request.json.get('skin_color')
    people.eye = request.json.get('eye')
    people.birth_year = request.json.get('birth_year')
    people.gender = request.json.get('gender')
    people.save()
    
    return jsonify(people.serialize()), 201


#Planets
@app.route('/planets', methods=['GET'])
def get_planets():
    all_Planets = Planets.query.all()
    all_Planets = list(map(lambda x: x.serialize(), all_Planets))
    return jsonify(all_Planets), 200

@app.route('/planets/<int:id>', methods=['GET'])
def planets_id(id):
    Planets_id = Planets.query.get(id)
    return jsonify(Planets_id.serialize())

@app.route("/planets", methods=['POST'])
def createPlanets():
    planets = Planets()
    planets.name = request.json.get('name')
    planets.rotation_period = request.json.get('rotation_period')
    planets.orbital_period = request.json.get('orbital_period')
    planets.diameter = request.json.get('diameter')
    planets.climate = request.json.get('climate')
    planets.gravity = request.json.get('gravity')
    planets.terrain = request.json.get('terrain')
    planets.surface_water = request.json.get('surface_water')
    planets.population = request.json.get('population')
    planets.save()
    
    return jsonify(planets.serialize()), 201


@app.route('/starships', methods=['GET'])
def get_starships():
    all_Starships = Starships.query.all()
    all_Starships = list(map(lambda x: x.serialize(), all_Starships))
    return jsonify(all_Starships), 200

@app.route('/starships/<int:id>', methods=['GET'])
def starships_id(id):
    Starships_id = Starships.query.get(id)
    return jsonify(Starships_id.serialize())

@app.route("/starships", methods=['POST'])
def createStarships():
    starships = Starships()
    starships.model = request.json.get('name')
    starships.starship_class = request.json.get('starship_class')
    starships.cost_in_credits = request.json.get('cost_in_credits')
    starships.length = request.json.get('length')
    starships.crew = request.json.get('crew')
    starships.passengers= request.json.get('passengers')
    starships.max_atmosphering_speed = request.json.get('max_atmosphering_speed')
    starships.hyperdrive_rating = request.json.get('hyperdrive_rating')
    starships.mGLT  = request.json.get('mGLT')
    starships.cargo_capacity = request.json.get('cargo_capacity')
    starships.consumables  = request.json.get('consumables')
    starships.save()
    
    return jsonify(starships.serialize()), 201



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
   

        



