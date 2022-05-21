import random
from flask import Blueprint, current_app
from src.models.chiste import Chiste, db
import requests

app = Blueprint('chiste', __name__)

def aleatorio():
    url = random.choice([current_app.config['DAD_URL'], current_app.config['CHUCK_URL']])
    return url

def obtener_server(nombre):
    if nombre.lower() == "chuck":
        url = current_app.config['CHUCK_URL']
    elif nombre.lower() == "dad":
        url = current_app.config['DAD_URL']
    else:
        url = "No existe la url"
    return url

def respuesta_server(url):
    result = ""
    try:
        response = requests.request("GET", url, headers={'Accept': 'application/json'}).json()
    except:
        pass
    
    if url == current_app.config['DAD_URL']:
        result = response["attachments"][0]["text"]
    elif url == current_app.config['CHUCK_URL']:
        result = response["value"]
    else:
        result = url
    print(result)
    return result

def crear_chiste(texto):
    chiste = Chiste(chiste=texto)
    db.session.add(chiste)
    db.session.commit()
    return chiste

def borrar_chiste(number):
    chiste = Chiste.query.filter_by(id=number).first()
    db.session.delete(chiste)
    db.session.commit()
    return chiste

def actualizar_chiste(number, texto):
    chiste = Chiste.query.filter_by(id=number).first()
    chiste.chiste = texto
    db.session.commit()
    return chiste

