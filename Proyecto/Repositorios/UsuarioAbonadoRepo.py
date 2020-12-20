
class UsuarioAbonadoRepo(object):
    def __init__(self, listaAbonados):
        self.__listaAbonados = listaAbonados

    @property
    def listaAbonados(self):
        return self.__listaAbonados

    @listaAbonados.setter
    def listaAbonados(self, listaAbonados):
        self.__listaAbonados = listaAbonados

    def agregarAbonado(self, usuarioAbonado):
        return self.__listaAbonados.append(usuarioAbonado)

    def buscarPorDni(self, dni):
        for x in self.__listaAbonados:
            if (self.__listaAbonados[x].dni == dni):
                devolver = self.__listaAbonados[x]

        return devolver
    def buscarPorNumPlaza(self, numPlaza):
        for x in self.__listaAbonados:
            if (self.__listaAbonados[x].numPlaza == numPlaza):
                devolver = self.__listaAbonados[x]

        return devolver