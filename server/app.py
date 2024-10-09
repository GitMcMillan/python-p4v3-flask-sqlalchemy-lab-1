# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
#add a view that takes one parameter, an integer that represents an id. The route should have the form /earthquakes/<int:id>.
@app.route('/earthquakes/<int:id>')
def get_by_id(id):
    #check for id
    earthquake = Earthquake.query.filter(Earthquake.id == id).first()
    #if it exists return it as an object body
    if earthquake:
        body = {'id': earthquake.id,
            'magnitude': earthquake.magnitude,
            'location': earthquake.location,
            'year': earthquake.year
            }
        status = 200
    # if not, return an error message body    
    else:
        body = {'message': f'Earthquake {id} not found.'}
        status = 404
    #return the respons body
    return make_response(body, status)


# /earthquakes/magnitude/<float:magnitude>.
@app.route('/earthquakes/magnitude/<float:magnitude>')
#takes one parameter, a float that represents magnitude.
def earthquake_magnitude(magnitude):
 # The view should query the database to get all earthquakes having a magnitude greater than or equal to the parameter value
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    magnitudes = []
    for earthquake in earthquakes:
        magnitude_dict = {
            'id': earthquake.id,
            'location': earthquake.location,
            'magnitude': earthquake.magnitude,
            "year": earthquake.year
        }
        magnitudes.append(magnitude_dict) 
    
    
    
    body = {'count': len(magnitudes),
            'quakes': magnitudes
        }
    status = 200
    
    return make_response(body, status)

 

# , and return a JSON response containing the count of matching rows along with a list containing the data for each row.





if __name__ == '__main__':
    app.run(port=5554, debug=True)
