import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

class RestApi:
    def __init__(self) :
        pass
    def keterangNama(self):
        return {
            'Pembuat' : "Dzaky Faishalariq",
            'Tema' : "Klasifikasi Bunga Iris"
        }
    def modelKlasifikasiBungaIris(self,sepalLength,sepalWidth, petalLength,petalWidth):
        sL,sW,pL,pW = float(sepalLength), float(sepalWidth), float(petalLength), float(petalWidth)
        model = load_model('modelKlasifikasi/modelIris.h5')
        nilaiprediksi = model.predict([[sL,sW,pL,pW]])
        nilaiprediksi = np.argmax(nilaiprediksi)
        print(nilaiprediksi)
        nilaiprediksi = int(nilaiprediksi)
        return nilaiprediksi