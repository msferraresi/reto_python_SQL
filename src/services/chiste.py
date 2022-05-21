from flask import Blueprint, jsonify, request
from src.controllers.chiste import aleatorio, obtener_server, respuesta_server, crear_chiste, borrar_chiste, actualizar_chiste

app = Blueprint('chiste', __name__)

@app.route("/chiste", methods=['GET'])
def AleatorioChiste():
    url = aleatorio()
    return jsonify({"message":respuesta_server(url)})

@app.route("/chiste/<server>", methods=['GET'])
def ServerChiste(server):
    url = obtener_server(server.strip())
    return jsonify({"message":respuesta_server(url)})

@app.route("/chiste", methods=['POST'])
def PostChiste():
    try:
        texto = request.json['texto']
        crear_chiste(texto)
        return jsonify({"message": "Chiste creado"})
    except Exception as e:
        return jsonify({"message":str(e)})

@app.route("/chiste", methods=['PUT'])
def PutChiste():
    try:
        number = request.json['number']
        texto = request.json['texto']
        actualizar_chiste(number, texto)
        return jsonify({"message": "Chiste actualizado"})
    except Exception as e:
        return jsonify({"message":str(e)})

@app.route("/chiste", methods=['DELETE'])
def DeleteChiste():
    try:
        number = request.json['number']
        borrar_chiste(number)
        return jsonify({"message": "Chiste borrado"})
    except Exception as e:
        return jsonify({"message":str(e)})
