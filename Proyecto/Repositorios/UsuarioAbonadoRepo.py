class UsuarioAbonadoRepo(object):
    def __init__(self, listaAbonados):
        self.__listaAbonados = listaAbonados

    @property
    def listaAbonados(self):
        return self.__listaAbonados

    @listaAbonados.setter
    def listaAbonados(self, listaAbonados):
        self.__listaAbonados = listaAbonados
