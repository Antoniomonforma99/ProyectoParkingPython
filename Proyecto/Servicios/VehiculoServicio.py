class VehiculoServicio(object):
    def __init__(self, vehiculoRepo):
        self.__vehiculoRepo = vehiculoRepo

    @property
    def vehiculoRepo(self):
        return self.__vehiculoRepo

    @vehiculoRepo.setter
    def vehiculoRepo(self, vehiculoRepo):
        self.__vehiculoRepo = vehiculoRepo

    def agregarVehiculo(self, vehiculo):
        return self.__vehiculoRepo.agregarVehiculo(vehiculo)

    #todo
    #generarId(self)

    def buscarPorMatricula(self, matricula):
        return self.__vehiculoRepo.buscarPorMatricula(matricula)