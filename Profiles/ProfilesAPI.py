# Profile API here
from flask import Blueprint
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)
