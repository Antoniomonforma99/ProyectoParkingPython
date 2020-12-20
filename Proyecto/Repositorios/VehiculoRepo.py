class Vehiculo(object):
    def __init__(self, listaVehiculos):
        self.__listaVehiculos = listaVehiculos

    @property
    def listaVehiculos(self):
        return self.__listaVehiculos

    @listaVehiculos.setter
    def listaVehiculos(self, listaVehiculos):
        self.__listaVehiculos = listaVehiculos

    def buscarPorMatricula(self, matricula):
        for x in self.__listaVehiculos:
            if(self.__listaVehiculos[x].matricula == matricula):
                resultado = self.__listaVehiculos[x]
        return resultado

    def buscarPorId(self, id):
        for x in self.__listaVehiculos:
            if(self.__listaVehiculos[x].id == id):
                resultado = self.__listaVehiculos[x]
        return resultado

    def agregarVehiculo(self,vehiculo):
        self.__listaVehiculos.append(vehiculo)

    def eliminarVehiculos(self, vehiculo):
        resultado = self.buscarPorMatricula(vehiculo.matricula)
        return self.__listaVehiculos.pop(resultado)