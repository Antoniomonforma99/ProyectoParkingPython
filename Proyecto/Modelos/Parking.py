class Parking(object):
    def __init__(self, listaVehiculos, numPlazas):
        self.__listaVehiculos = listaVehiculos
        self.__numPlazas = numPlazas

    @property
    def listaVehiculos(self):
        return self.__listaVehiculos

    @listaVehiculos.setter
    def listaVehiculos(self, listaVehiculos):
        self.__listaVehiculos = listaVehiculos

    @property
    def numPlazas(self):
        return self.__numPlazas

    @numPlazas.setter
    def numPlazas(self, numPlazas):
        self.__numPlazas = numPlazas