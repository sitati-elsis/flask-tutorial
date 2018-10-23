from flask import Flask

# flask object
app = Flask(__name__)

# the import is put at the bottom because of circular dependency
from app import routes

