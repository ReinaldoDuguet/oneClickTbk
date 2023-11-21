from flask import Flask
from config import config


#routes
from routes import oneClick

app = Flask(__name__)

def page_not_found(error):
    return '<h1>Ups! Pagina no encontrada</h1>',404


if __name__ == '__main__':
    app.config.from_object(config['development'])


    # Blueprints
    app.register_blueprint(oneClick.main, url_prefix='/oneClickTbk/') # PRIMER ENDPOINT, DEVUELVE A TODOS LOS CLIENTES EN TBK

    # Error Handlers
    app.register_error_handler(404,page_not_found)

    app.run()
