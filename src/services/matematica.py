from flask import Blueprint, g, jsonify
from src.controllers.matematica import Agregar, MinimoComunMultiplo

app = Blueprint('matematica', __name__)

@app.route("/numbers/<lstNumeros>", methods = ['GET'])
def endpointLista(lstNumeros):
    return jsonify({"message":MinimoComunMultiplo(lstNumeros)})

@app.route("/number/<numero>", methods = ['GET'])
def enpoint(numero):
    return jsonify({"message":Agregar(numero)})