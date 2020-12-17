from .Usuario import Usuario

class UsuarioAdministrador(Usuario):
    def __init__(self, nombre, id, clave):
        super(nombre, id)
        self.__clave = clave

    @property
    def clave(self):
        return self.__clave

    @clave.setter
    def clave(self, clave):
        self.__clave = clave