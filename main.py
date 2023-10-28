from flask import Flask,request, jsonify
from modelKlasifikasi.resAPI import RestApi
app = Flask(__name__)

resApi = RestApi()
@app.route('/',methods=['GET'])
def menuUtama():
    try:
        identitas = resApi.keterangNama()
        return jsonify(identitas), 202
    except Exception as e:
        return jsonify({
            'succes':False,
            'error':str(e)
        }), 404 
@app.route('/klasifikasiIRIS',methods=['POST'])
def klasifikasi():
    request_data = request.get_json()
    try:
        sL = request_data['sL']
        sW = request_data['sW']
        pL = request_data['pL']
        pW = request_data['pW']
        nilai = resApi.modelKlasifikasiBungaIris(sL,sW,pL,pW)
        return jsonify({
            "predikis" : nilai
        }),202
    except Exception as e:
        return jsonify({
            'succes':False,
            'error':str(e)
        }), 404 

if __name__ == "__main__":
    app.run(debug=False)