from .Usuario import Usuario
class UsuarioAbonado(Usuario):
    def __init__(self, nombre, id, abono, numPlaza, numTarjeta):
        super(nombre, id)
        self.__abono = abono
        self.__numPlaza = numPlaza
        self.__numTarjeta = numTarjeta

    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self,abono):
        self.__abono = abono

    @property
    def numPlaza(self):
        return self.__numPlaza

    @numPlaza.setter
    def numPlaza(self, numPlaza):
        self.__numPlaza = numPlaza

    @property
    def numTarjeta(self):
        return self.__numTarjeta

    @numTarjeta.setter
    def numTarjeta(self, numTarjeta):
        self.__numTarjeta = numTarjeta