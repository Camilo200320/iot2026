import pickle

import numpy as np

with open('RFDiabetesv132.pkl','rb') as file:
    RF_model2 = pickle.load(file)

    labels = ['sano','Diabetes']

def diabetes_prediction(data):

    xin = np.array([
        data.pregnancies,
        data.glucose,
        data.bloodpressure,
        data.skinthickess,
        data.insulin,
        data.bmi,
        data.diabetespedigreefunction,
        data.age
    ]).reshape(1,8)
    prediction = RF_model2.prediction(xin)
    print("xin shape", xin.shape)
    return labels[prediction[0]]

