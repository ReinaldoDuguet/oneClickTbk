class Data_1():
    #definimos la forma de la respuesta a la inscripcion
    def __init__(self, token, url_webpay) -> None:
        self.token = token
        self.url_webpay = url_webpay

    def to_JSON(self):
        return {
            'token': self.token,
            'url_webpay': self.url_webpay
        }