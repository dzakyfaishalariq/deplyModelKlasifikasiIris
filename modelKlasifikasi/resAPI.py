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
        dataHasil = {}
        nilaiprediksi = model.predict([[sL,sW,pL,pW]])
        dataHasil['akurasi'] = float(np.max(nilaiprediksi))
        nilaiprediksi = np.argmax(nilaiprediksi)
        nilaiprediksi = int(nilaiprediksi)
        dataHasil['predikisIndex'] = nilaiprediksi
        if nilaiprediksi == 0:
            dataHasil['class'] = "Iris Setosa"
        elif nilaiprediksi == 1:
            dataHasil['class'] = "Iris Versicolor"
        elif nilaiprediksi == 2:
            dataHasil['class'] = "Iris Verginica"
        dataHasil['inisial'] = {
            0 : "Iris Setosa",
            1 : "Iris Versicolor",
            2 : "Iris Verginica"
        }
        return dataHasil