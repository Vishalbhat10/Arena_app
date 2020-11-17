# This script initiates the Arena application's app controler and 
# configures the connection to database tables using GeoAlchemy2 and SQLAlchemy
#
#



import flask
app = flask.Flask(__name__)
conn_string = 'postgresql://postgres:abc123@localhost:5432/flaskgis7'
app.config['SQLALCHEMY_DATABASE_URI'] = conn_string	
app.config['SECRET_KEY'] = "SECRET_KEY"
import application.views
