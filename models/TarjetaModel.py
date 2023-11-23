from database.db import get_connection
from .entities.tarjeta import Tarjeta
from utils.rut import validarRut
import ipdb


class TarjetaModel():

    @classmethod
    def get_tarjetas(self):
        try:
            connection = get_connection()
            tarjetas = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * from cliente")
                resultset = cursor.fetchall()
                for row in resultset:
                    print(row[1])
                    tarjeta = Tarjeta(row[1],row[2],row[3])
                    if validarRut(row[1]):   # DE ESTE MODO SOLO TRAE LOS RUTs VALIDOS
                        tarjetas.append(tarjeta.to_JSON())
                    else:
                        pass
            connection.close()
            return tarjetas
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_tarjeta(self,username):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * from cliente WHERE username = %s",(username,))
                row = cursor.fetchone()
                tarjeta = None
                if row != None:
                    tarjeta = Tarjeta(row[1],row[2],row[3])
                    tarjeta = tarjeta.to_JSON()
            connection.close()

            return tarjeta
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_muchas_tarjetas(self,username):
        try:
            connection = get_connection()
            tarjetas = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * from cliente WHERE username = %s",(username,))
                resultset = cursor.fetchall()
                for row in resultset:
                    tarjeta = Tarjeta(row[1],row[2],row[3])
                    tarjetas.append(tarjeta.to_JSON())

            connection.close()
            return tarjetas
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def post_tarjeta(self,tarjeta):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO cliente (username,email,response_url)
                                VALUES (%s,%s,%s)""",(tarjeta.username,tarjeta.email,tarjeta.response_url))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return tarjeta
        except Exception as ex:
            raise Exception(ex)
