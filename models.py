from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    categories = db.relationship('Category', backref='user')

    def __repr__(self):
        return '<User %>' % self.id


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(150), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipes = db.relationship('Recipe', backref='category')

    def __repr__(self):
        return '<Category %>' % self.id


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(150), unique=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    steps = db.relationship('Step', backref='recipe')
    ingredients = db.relationship('Ingredient', backref='recipe')

    def __repr__(self):
        return '<Recipe %>' % self.id


class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    instruction = db.Column(db.String(1000000), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

    def __repr__(self):
        return '<Step %>' % self.id


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

    def __repr__(self):
        return '<Ingredient %>' % self.id
