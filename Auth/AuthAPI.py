# Score API here
from flask import Blueprint
import sys
from db import db
sys.path.append("../")

auth_api = Blueprint("auth", __name__)
