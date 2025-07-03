from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(200))
    unit_price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'
