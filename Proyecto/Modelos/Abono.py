class Abono(object):
    def __init__(self,usuarioAbonado, pin, tarifa, fechaInicio, fechaFin):
        self.__usuarioAbonado = usuarioAbonado
        self.__pin = pin
        self.__tarifa = tarifa
        self.__fechaInicio = fechaInicio
        self.fechaFin = fechaFin

    @property
    def usuarioAbonado(self):
        return self.__usuarioAbonado

    @usuarioAbonado.setter
    def usuarioAbonado(self, usuarioAbonado):
        self.__usuarioAbonado = usuarioAbonado

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, tarifa):
        self.__tarifa = tarifa

    @property
    def fechaInicio(self):
        return self.__fechaInicio

    @fechaInicio.setter
    def fechaInicio(self, fechaInicio):
        self.__fechaInicio = fechaInicio

    @property
    def fechaFin(self):
        return self.__fechaFin

    @fechaFin.setter
    def fechaFin(self, fechaFin):
        self.__fechaFin = fechaFin