from flask import Flask,Response,jsonify,request
from flask_cors import CORS
from waitress import serve
import web_sockets_ht200 as web_sockets_ht200
controlador_ht200 = web_sockets_ht200.MySocketHT200()


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return "<h1>API DE CENTRALIZACION<h1>"
   

@app.route('/rest/getTimeHT200', methods=['GET'])
def getTimeHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getTime(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)
   

@app.route('/rest/getFasesHT200', methods=['GET'])
def getFasesHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getFases(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)

@app.route('/rest/getSecuenciaHT200', methods=['GET'])
def getSecuenciaHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getSecuencia(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)


@app.route('/rest/getSplitHT200',methods=['GET'])
def getSplitHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getSplit(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)


@app.route('/rest/getPatternHT200',methods=['GET'])
def getPatternHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getPattern(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)



@app.route('/rest/getPlanesHT200',methods=['GET'])
def getPlanesHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getPlanes(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)

@app.route('/rest/getAccionHT200',methods=['GET'])
def getAccionHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getAccion(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)

@app.route('/rest/getScneduleHT200',methods=['GET'])
def getScneduleHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getScnedule(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)


@app.route('/rest/getDeviceInfoHT200',methods=['GET'])
def getDeviceInfoHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getDeviceInfo(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)


@app.route('/rest/getBasicInfoHT200',methods=['GET'])
def getBasicInfoHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getBasicInfo(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)


@app.route('/rest/getUnitHT200',methods=['GET'])
def getUnitHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getUnitHT200(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)



@app.route('/rest/getChannelHT200',methods=['GET'])
def getChannelHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getChannel(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)



@app.route('/rest/getCoordHT200',methods=['GET'])
def getCoordHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getCoord(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)

@app.route('/rest/getOverlapHT200',methods=['GET'])
def getOverlapHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getOverlap(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)

@app.route('/rest/getErroresControlador',methods=['GET'])
def getErroresControlador():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getErroresControlador(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)

@app.route('/rest/getWorkStateHT200',methods=['GET'])
def getWorkStateHT200():
    args = request.args
    ip = args.get('ip')
    result = controlador_ht200.getWorkState(ip)
    if result == False:
        return "Controller is not accesible", 503
    return jsonify(result)


'''
Funciones  de Escritura API HT200
'''

@app.route('/rest/setUnitHT200', methods=['POST'])
def setUnitHT200():
    args = request.args
    json_data = request.get_json(force=True) 
    ip = args.get('ip')
    result = controlador_ht200.setUnitHT200(json_data['trama'],ip)
    return jsonify(result)

@app.route('/rest/setFasesHT200', methods=['POST'])
def setFasesHT200():
    args = request.args
    json_data = request.get_json(force=True) 
    ip = args.get('ip')
    result = controlador_ht200.setFases(json_data['trama'],ip)
    if result == False:
        return "Controller is not accesible", 503
    return "Dato Recibido",200


@app.route('/rest/setSecuenciasHT200', methods=['POST'])
def setSecuencias():
    args = request.args
    json_data = request.get_json(force=True) 
    ip = args.get('ip')
    result = controlador_ht200.setSecuencias(json_data['trama'],ip)
    if result == False:
        return "Controller is not accesible", 503
    return "Dato Recibido",200


@app.route('/rest/setSplitHT200', methods=['POST'])
def setSplitHT200():
    args = request.args
    json_data = request.get_json(force=True) 
    ip = args.get('ip')
    result = controlador_ht200.setSplit(json_data['trama'],ip)
    if result == False:
        return "Controller is not accesible", 503
    return "Dato Recibido",200


@app.route('/rest/setPatternHT200', methods=['POST'])
def setPatternHT200():
    args = request.args
    json_data = request.get_json(force=True) 
    ip = args.get('ip')
    result = controlador_ht200.setPattern(json_data['trama'],ip)
    if result == False:
        return "Controller is not accesible", 503
    return "Dato Recibido",200

@app.route('/rest/setActionHT200', methods=['POST'])
def setActionHT200():
    args = request.args
    json_data = request.get_json(force=True) 
    ip = args.get('ip')
    result = controlador_ht200.setAction(json_data['trama'],ip)
    if result == False:
        return "Controller is not accesible", 503
    return "Dato Recibido",200

@app.route('/rest/setPlanHT200', methods=['POST'])
def setPlanHT200():
    args = request.args
    json_data = request.get_json(force=True) 
    ip = args.get('ip')
    result = controlador_ht200.setPlan(json_data['trama'],ip)
    if result == False:
        return "Controller is not accesible", 503
    return "Dato Recibido",200

@app.route('/rest/setHorariosHT200', methods=['POST'])
def setHorariosHT200():
    args = request.args
    json_data = request.get_json(force=True) 
    ip = args.get('ip')
    result = controlador_ht200.setHorarios(json_data['trama'],ip)
    if result == False:
        return "Controller is not accesible", 503
    return "Dato Recibido",200

@app.route('/rest/setChannelHT200', methods=['POST'])
def setChannelHT200():
    args = request.args
    json_data = request.get_json(force=True) 
    ip = args.get('ip')
    result = controlador_ht200.setChannel(json_data['trama'],ip)
    if result == False:
        return "Controller is not accesible", 503
    return "Dato Recibido",200



@app.route('/rest/setBasicPlan', methods=['POST'])
def setBasicPlan():
    args = request.args
    json_data = request.get_json(force=True) 
    ip = args.get('ip')
    result = controlador_ht200.setBasicPlan(json_data,ip)
    if result == False:
        return "Controller is not accesible", 503
    return "Dato Recibido",200

mode = "dev"
if __name__ == '__main__':
    if mode == "dev":
        app.run(host='0.0.0.0', port=4000, debug=True)
    else:
        serve(app, host='0.0.0.0', port=4000, threads=4)

