#importing required libraries

from flask import Flask, request, render_template, jsonify, make_response


from Resources.predict import Predict
from flask_restful import Api
# Gradient Boosting Classifier Model


app = Flask(__name__)
api = Api(app)

api.add_resource(Predict, '/predict')



if __name__ == "__main__":
    app.run(debug=True)