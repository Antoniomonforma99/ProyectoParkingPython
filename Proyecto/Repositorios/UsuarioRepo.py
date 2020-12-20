
class UsuarioRepo(object):
    def __init__(self, listaUsuarios):
        self.__listaUsuarios = listaUsuarios

    @property
    def listaUsuarios(self):
        return self.__listaUsuarios

    @listaUsuarios.setter
    def listaUsuarios(self, listaUsuarios):
        self.__listaUsuarios = listaUsuarios

    def buscarPorVehiculo(self,vehiculo):
        resultado = 0
        for x in self.__listaUsuarios:
            if (self.__listaUsuarios[x].vehiculo == vehiculo):
                resultado = self.__listaUsuarios[x]
        return resultado


