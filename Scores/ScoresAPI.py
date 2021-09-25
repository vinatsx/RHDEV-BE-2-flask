# Score API here
from flask import Blueprint
import sys
from db import db
sys.path.append("../")

scores_api = Blueprint("scores", __name__)
