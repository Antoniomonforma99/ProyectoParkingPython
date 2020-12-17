class Vehiculo(object):
    def __init__(self, matricula, id, tipo, usuario, ticket):
        self.__matricula = matricula
        self.__id = id
        self.__tipo = tipo
        self.__usuario = usuario
        self.__ticket = ticket

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def ticket(self):
        return self.__usuario

    @ticket.setter
    def ticket(self, ticket):
        self.__ticket = ticket