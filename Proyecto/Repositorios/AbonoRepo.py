from ..Modelos import Abono
class AbonoRepo(object):
    def __init__(self, listaAbonos):
        self.__listaAbonos = listaAbonos
    @property
    def listaAbonos(self):
        return

    @listaAbonos.setter
    def listaAbonos(self, listaAbonos):
        self.__listaAbonos = listaAbonos

    def agregarAbono(self,abono):
        return self.__listaAbonos.append(abono)

    def buscarPorPin(self, pin):

        for x in self.__listaAbonos:
            if Abono.pin==pin:
                resultado = Abono

        return resultado
