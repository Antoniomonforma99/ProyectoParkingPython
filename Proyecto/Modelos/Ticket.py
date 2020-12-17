class Ticket(object):
    def __init__(self, fechaEntrada, fechaSalida, precio, matricula, id, pin, plaza):
        self.__fechaEntrada = fechaEntrada
        self.__fechaSalida = fechaSalida
        self.__precio = precio
        self.__matricula = matricula
        self.__id = id
        self.__pin = pin
        self.__plaza = plaza

    @property
    def fechaEntrada(self):
        return self.__fechaEntrada

    @fechaEntrada.setter
    def fechaEntrada(self, fechaEntrada):
        self.__fechaEntrada = fechaEntrada

    @property
    def fechaSalida(self):
        return self.__fechaSalida

    @fechaSalida.setter
    def fechaSalida(self, fechaSalida):
        self.__fechaSalida = fechaSalida

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

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
    def pin(self):
        return self.__pin

    @pin.setter
    def id(self, pin):
        self.__pin = pin

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza