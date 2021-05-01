"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(arr):
    db.app = arr
    db.init_app(arr)

class Cupcake(db.Model):
    """Model for Cupcake Model"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    flavor = db.Column(db.Text,nullable=False)

    size = db.Column(db.Text,nullable=False)

    rating = db.Column(db.Float,nullable=False)

    image = db.Column(db.Text,default="https://tinyurl.com/demo-cupcake")

    def __repr__(self):
        return f"cupcake id {self.id}"

    def serialize(self):
        return {
            "id": self.id,
            "flavor" : self.flavor,
            "size":self.size,
            "rating":self.rating,
            "image": self.image
        }
