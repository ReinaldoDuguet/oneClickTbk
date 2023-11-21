from database.db import get_connection
from .entities.tarjeta import Tarjeta


class TarjetaModel():

    @classmethod
    def get_tarjeta(self):
        try:
            connection = get_connection()
            tarjetas = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, username, email, response_url from cliente ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    tarjeta = Tarjeta(row[0],row[1],row[2],row[3])
                    tarjetas.append(tarjeta.to_JSON())

            connection.close()
            return tarjetas
        except Exception as ex:
            raise Exception(ex)
