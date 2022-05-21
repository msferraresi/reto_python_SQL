from flask import Blueprint, g, jsonify
from src.controllers.matematica import Agregar, MinimoComunMultiplo
from flasgger import swag_from

app = Blueprint('matematica', __name__)

@app.route("/numbers/<lstNumeros>", methods = ['GET'])
@swag_from("docs/matematica/minimo_comun_multiplo.yaml")
def endpointLista(lstNumeros):
    return jsonify({"message":MinimoComunMultiplo(lstNumeros)})

@app.route("/number/<numero>", methods = ['GET'])
@swag_from("docs/matematica/agregar.yaml")
def enpoint(numero):
    return jsonify({"message":Agregar(numero)})