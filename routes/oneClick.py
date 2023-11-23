from flask import Blueprint,jsonify, request
import ipdb
from decouple import config

#entities
from models.entities.tarjeta import Tarjeta
#modelo(s)
from models.TarjetaModel import TarjetaModel


main = Blueprint('oneClickTbk',__name__) #el nombre que va en el primer argumento se usará cuando se declare el blueprint en app.py (oneClick.main,...)


@main.route('/')
def get_cards():
    try:
        tarjetas = TarjetaModel.get_tarjetas()
        return jsonify(tarjetas)
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}), 500

@main.route('/<username>')
def get_card(username):
    try:
        tarjeta = TarjetaModel.get_tarjeta(username)
        if tarjeta != None:
            return jsonify(tarjeta)
        else:
            return jsonify({}), 400
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}), 500

@main.route('cards/<username>')
def get_too_cards(username):
    try:
        print(f"ID: {TBK_API_KEY_ID}")
        tarjetas = TarjetaModel.get_muchas_tarjetas(username)
        return jsonify(tarjetas)
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}), 500


@main.route('/suscribe', methods=['POST'])
def post_card():
    TBK_API_KEY_ID     = config('Tbk-Api-Key-Id')
    TBK_API_KEY_SECRET = config('Tbk-Api-Key-Secret')
    TBK_URL_SUSCRIBE   = config('url_suscribe')
    try:
        username     = request.json['username']
        email        = request.json['email']
        response_url = request.json['response_url']
        tarjeta = Tarjeta(username,email,response_url)

        affected_rows = TarjetaModel.post_tarjeta(tarjeta)

        return jsonify({"msje":"se ha insertado el valor en bbdd"})

    except Exception as ex:
        return jsonify({'mensaje':str(ex)}), 500
