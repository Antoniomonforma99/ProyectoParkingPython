from ..Repositorios import UsuarioAbonadoRepo
class UsuarioAbonadoServicio(object):
    def __init__(self, usuarioAbonadoRepo):
        self.__usuarioAbonadoRepo = usuarioAbonadoRepo

    @property
    def usuarioAbonadoRepo(self):
        return self.__usuarioAbonadoRepo

    @usuarioAbonadoRepo.setter
    def usuarioAbonadoRepo(self, usuarioAbonadoRepo):
        self.__usuarioAbonadoRepo = usuarioAbonadoRepo

    def agregarAbonado(self, usuarioAbonado):
        return self.__usuarioAbonadoRepo.agregarAbonado(usuarioAbonado)

    def buscarPorDni(self, dni):
        return self.__usuarioAbonadoRepo.buscarPorDni(dni)