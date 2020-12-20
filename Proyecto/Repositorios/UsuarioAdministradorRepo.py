
class UsuarioAbonadoRepo(object):

    def __init__(self, listaAdmin):
        self.__listaAdmin = listaAdmin

    @property
    def listaAdmin(self):
        return self.__listaAdmin

    @listaAdmin.setter
    def listaAdmin(self, listaAdmin):
        self.__listaAdmin = listaAdmin

    def buscarPorClave(self, clave):
        for x in self.__listaAdmin:
            if (self.__listaAdmin[x].clave == clave):
                resultado = self.__listaAdmin[x]
        return resultado

    def agregarAdministrador(self, admin):
        return self.__listaAdmin.append(admin)