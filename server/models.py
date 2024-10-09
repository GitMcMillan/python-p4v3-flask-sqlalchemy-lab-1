from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here

class Earthquake(db.Model, SerializerMixin):
#a string named __tablename__ assigned to the value "earthquakes".
  __tablename__ = "earthquakes"
  # a column named id to store an int that is the primary key.
  id = db.Column(db.Integer, primary_key=True)
  # a column named magnitude to store a float.
  magnitude = db.Column(db.Float)
  # a column named location to store a string.
  location = db.Column(db.String)
  # A column named year to store an int.
  year = db.Column(db.Integer)

  def __repr__(self):
    return f'<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>'
