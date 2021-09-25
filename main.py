from Scores.ScoresAPI import scores_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import db


# Write your flask code here

app = Flask(__name__)

app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(scores_api, url_prefix="/users")


if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)
