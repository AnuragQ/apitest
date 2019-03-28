from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:test123@localhost/IS_database'

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "hello"


@app.route('/post_location', methods=['POST'])
def post_location():

    key="IN/"+request.json['pin_code']
    place_name=request.json['place_name']
    admin_name1=request.json['admin_name1']
    latitude=request.json['latitude']
    longitude=request.json['longitude']
    accuracy=request.json['accuracy']
    location=Location(key,place_name,admin_name1,latitude,longitude,accuracy)
    db.session.add(location)
    db.session.commit()
    return "success"


class Location(db.Model):
    __tablename__ = 'Latlong'

    key = db.Column(db.String(9), primary_key=True)
    place_name = db.Column(db.String(50))
    admin_name1 = db.Column(db.String(50))
    latitude=db.Column(db.Float)
    longitude=db.Column(db.Float)
    accuracy=db.Column(db.Integer)
    

    accuracy=db.Column(db.Integer)
    accuracy=db.Column(db.Integer)
    def __init__(self, key, place_name, admin_name1,latitude,longitude,accuracy):
        self.key= key 
        self.place_name = place_name
        self.admin_name1 = admin_name1
        self.latitude = latitude
        self.longitude = longitude
        self.accuracy = accuracy
    def __repr__(self):
        return '<key {}>'.format(self.key)

if __name__ =="__main__":
    app.run()
    