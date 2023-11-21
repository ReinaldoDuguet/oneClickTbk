from flask import Blueprint,jsonify
import ipdb

from models.TarjetaModel import TarjetaModel


main = Blueprint('oneClickTbk',__name__) #el nombre que va en el primer argumento se usará cuando se declare el blueprint en app.py (oneClick.main,...)


@main.route('/')
def get_cards():
    try:
        tarjetas = TarjetaModel.get_tarjeta()
        return jsonify(tarjetas)
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}), 500
