from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    people = db.relationship('People', secondary='favorite_people', backref='user')
    planets = db.relationship('Planets', secondary='favorite_planets', backref='user')
    starships = db.relationship('Starships', secondary='favorite_starships', backref='user')

    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE

    def get_people(self):
        return list(map(lambda people: people.serialize(), self.people))
    
    def get_planets(self):
        return list(map(lambda planets: planets.serialize(), self.planets))
    
    def get_starships(self):
        return list(map(lambda starships: starships.serialize(), self.starships))

    def serialize(self):
        return {
            "id": self.id,
            "password": self.password,
            "email": self.email
        }

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    height = db.Column(db.String(100), unique=True, nullable=False)
    mass = db.Column(db.String(100),  unique=True, nullable=False)
    hair_color = db.Column(db.String(100),  unique=True, nullable=False)
    skin_color = db.Column(db.String(100),  unique=True, nullable=False)
    eye = db.Column(db.String(100),  unique=True, nullable=False)
    birth_year = db.Column(db.String(100),  unique=True, nullable=False)
    gender = db.Column(db.String(100),  unique=True, nullable=False)
 
    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height":self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "eye": self.eye,
            "birth_year": self.birth_year,
            "gender": self.gender
        }
   
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    rotation_period = db.Column(db.String(100), unique=True, nullable=False)
    orbital_period = db.Column(db.String(100), unique=True, nullable=False)
    diameter = db.Column(db.String(100), unique=True, nullable=False)
    climate = db.Column(db.String(100), unique=True, nullable=False)
    gravity = db.Column(db.String(100), unique=True, nullable=False) 
    terrain = db.Column(db.String(100), unique=True, nullable=False)
    surface_water = db.Column(db.String(100), unique=True, nullable=False)
    population = db.Column(db.String(100), unique=True, nullable=False)

    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE

    def serialize(self):
        return {
            "id": self.id,
            "model": self.model,
            "starship":self.starship,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed ": self.max_atmosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "mGLT": self.mGLT,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables
            
        }

class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), unique=True, nullable=False)
    starship_class = db.Column(db.String(100), unique=True, nullable=False)
    cost_in_credits = db.Column(db.String(100), unique=True, nullable=False)
    length = db.Column(db.String(100), unique=True, nullable=False)
    crew = db.Column(db.String(100), unique=True, nullable=False)
    passengers = db.Column(db.String(100), unique=True, nullable=False)
    max_atmosphering_speed = db.Column(db.String(100), unique=True, nullable=False)
    hyperdrive_rating = db.Column(db.String(100), unique=True, nullable=False)
    mGLT = db.Column(db.String(100), unique=True, nullable=False)
    cargo_capacity = db.Column(db.String(100), unique=True, nullable=False)
    consumables = db.Column(db.String(100), unique=True, nullable=False)

    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE
   
    def serialize(self):
        return {
            "id": self.id,
            "model": self.model,
            "starship":self.starship,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed ": self.max_atmosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "mGLT": self.mGLT,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables
            
        }


class Favorite_people(db.Model):
    __tablename__ = 'favorite_people'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id= db.Column(db.Integer, db.ForeignKey('people.id'))

    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id
        }

    rel_user = db.relationship("User")
    rel_people = db.relationship("People")


class Favorite_planets(db.Model):
    __tablename__ = 'favorite_planets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planets_id= db.Column(db.Integer, db.ForeignKey('planets.id'))
    
    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets_id": self.planets_id
        }
  
    rel_user = db.relationship("User")
    rel_planets = db.relationship("Planets")

class Favorite_starships(db.Model):
    __tablename__ = 'favorite_starships'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    starships_id= db.Column(db.Integer, db.ForeignKey('starships.id'))


    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "starships_id": self.starships_id
        }

    rel_user = db.relationship("User")
    rel_people = db.relationship("Starships")