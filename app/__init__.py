from flask import Flask
from flask_cors import CORS
#from flask_pymongo import PyMongo

#mongo = PyMongo()
def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["MONGO_URI"] = "mongodb://localhost:27017/yourdbname" 

    #mongo.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
