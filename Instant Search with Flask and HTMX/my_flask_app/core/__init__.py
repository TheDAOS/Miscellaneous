from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig

# Create the Flask app instance
app = Flask(__name__)

# Load configuration from DevelopmentConfig
app.config.from_object(DevelopmentConfig)

# Initialize SQLAlchemy with the app instance
db = SQLAlchemy(app)

# Initialize Flask-Migrate with the app instance and database
migrate = Migrate(app, db)

# Import routes to register them with the app
from core import routes