from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Metadata helps Flask-Migrate track schema changes
metadata = MetaData()

# Create the SQLAlchemy instance
db = SQLAlchemy(metadata=metadata)


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Pet {self.name} ({self.species})>"
