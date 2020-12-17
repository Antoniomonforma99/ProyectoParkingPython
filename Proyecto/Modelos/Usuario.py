class Usuario(object):
    def __init__(self, nombre, id):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def id(self):
        return self.__id

    @nombre.setter
    def nombre(self, id):
        self.__id= id