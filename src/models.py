from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    personajes_fav = db.relationship("FavoriteCharacters", backref = "user")
    planets_fav = db.relationship("FavoritePlanets", backref = "user")

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

        class Characters(db.Model):
            __tablename__ ='personajes'
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(250), nullable=False)
            description = db.Column(db.String(250), nullable=False)
            favorite_characters = db.relationship()
            def serialize(self):
                return{
                    "id": self.id,
                    "name": self.name,
                    "description": self.description,
                }


        class Planets(db.Model):
            __tablename__ = 'Planetas'
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(250), nullable=False)
            description = db.Column(db.String(250), nullable=False)
            favorite_planets_id = db.Column(db.Integer, db.ForeignKey('FavoritePlanets'))
            def serialize(self):
                return{
                    "id": self.id,
                    "name": self.name,
                    "description": self.description,

                }

        class FavoriteCharacters(db.Model):
            __tablename__ = 'favoritos'
            id = db.Column(db.Integer, primary_key=True)
            user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
            #character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
            Characters = db.relationship("Characters", backref ="favorite")
            
            def serialize(self):
                return{
                    "id": self.id,
                    "user_id": self.user_id,
                    "character_id": self.character_id,
                }


        class FavoritePlanets(db.Model):
            __tablename__ = 'planeta_favorito'
            id = db.Column(db.Integer, primary_key=True)
            user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
            #planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
            planet = db.relationship("Planets", backref = "favorite")
            
            def serialize(self):
                return{
                    "id": self.id,
                    "user_id": self.user_id,
                    "character_id": self.character_id,
                }
