from datetime import datetime

class AbonoServicio(object):
    def __init__(self, abonoRepo):
        self.__abonoRepo = abonoRepo

    @property
    def abonoRepo(self):
        return self.__abonoRepo

    @abonoRepo.setter
    def abonoRepo(self, abonoRepo):
        self.__abonoRepo = abonoRepo

    #todo
   # def generarPin(self):
   #
   #     return pin

    def agregarAbono(self,abono):
        return self.__abonoRepo.agregarAbono(abono)

    def buscarPorPin(self, pin):
        return self.__abonoRepo.buscarPorPin(pin)


    #todo
    #def generarFechaCancelacion(self, abono):
