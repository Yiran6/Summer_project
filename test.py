from flask import Flask
from flask_googlemaps import GoogleMaps

app = Flask(__name__)

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyC1R-xRU98ksZ14PtBgbHIfIrkTrWsJ-64"

# Initialize the extension
GoogleMaps(app)
