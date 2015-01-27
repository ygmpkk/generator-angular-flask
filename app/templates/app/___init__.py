from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_oauthlib.provider import OAuth2Provider
from flask.ext.session import Session
from flask.ext.cache import Cache

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
db = SQLAlchemy(app)
oauth = OAuth2Provider(app)
Session(app)
cache = Cache(app)

<% _.each(entities, function (entity) { %>
from app.models import <%= entity.name %><% }); %>
from app.routes import index
<% _.each(entities, function (entity) { %>
from app.routes import <%= pluralize(entity.name) %><% }); %>
