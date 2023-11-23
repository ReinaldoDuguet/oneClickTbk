from utils.rut import validarRut
import ipdb

class Tarjeta():

    #ahora definimos su constructor
    def __init__(self, username=None, email=None, response_url=None):
        self.username       = username
        self.email          = email
        self.response_url   = response_url

    def to_JSON(self):
        return{
            'username':self.username,
            'email':self.email,
            'response_url':self.response_url
        }
