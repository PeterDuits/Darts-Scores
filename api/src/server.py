from flask import Flask
from flask_cors import CORS
from src.routes import graphql
from src.routes import rest_v1

app = Flask(__name__)
CORS(app)

'''
Register all API blueprints
'''
app.register_blueprint(graphql.api, url_prefix='/graphql')
app.register_blueprint(rest_v1.api, url_prefix='/v1')
