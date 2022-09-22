from flask import jsonify,make_response
from flask_restful import Resource, reqparse
from feature import generate_data_set

import numpy as np
import pandas as pd
import sklearn
import warnings
warnings.filterwarnings('ignore')
from sklearn.ensemble import GradientBoostingClassifier
from ml import *
#from phishing import *




class Predict(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    def get(self):
        data = Predict.parser.parse_args()
        print('data:',data['url'])
        x = np.array(generate_data_set(str(data['url']))).reshape(1,30)
        print(x)
        y_pred =int(gbc.predict(x)[0])
        print("y_pred:",y_pred)
        #acc = round(float(gbc_accuracy*100),2)
        #print("ACCURACY:", acc)
        #1 is safe       
        #-1 is unsafe
        y_pro_phishing = gbc.predict_proba(x)[0,0]
        y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        # if(y_pred ==1 ):
        pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing*100)
        #print(pred)
        #event = json.loads(request.data)
        print(y_pro_non_phishing)
        acc=round(float(gbc_accuracy*100),2)
        print('accuracy:',acc)
        return make_response(jsonify({'prediction':y_pred, 'accuracy':acc}))

        