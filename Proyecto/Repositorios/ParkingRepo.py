from datetime import datetime
class ParkingRepo(object):
    def __init__(self, parking, vehiculoRepo, ticketRepo, UsuarioAbonadoRepo):
        self.__parking = parking
        self.__vehiculoRepo = vehiculoRepo
        self.__ticketRepo = ticketRepo
        self.__UsuarioAbonadoRepo = UsuarioAbonadoRepo

    @property
    def parking(self):
        return self.__parking

    @parking.setter
    def parking(self, parking):
        self.__parking = parking

    @property
    def vehiculoRepo(self):
        return self.__vehiculoRepo

    @vehiculoRepo.setter
    def vehiculoRepo(self, vehiculoRepo):
        self.__vehiculoRepo = vehiculoRepo

    @property
    def ticketRepo(self):
        return self.__ticketRepo

    @ticketRepo.setter
    def ticketRepo(self, ticketRepo):
        self.__ticketRepo = ticketRepo

    @property
    def UsuarioAbonadoRepo(self):
        return self.__UsuarioAbonadoRepo

    @UsuarioAbonadoRepo.setter
    def UsuarioAbonadoRepo(self, UsuarioAbonadoRepo):
        self.__UsuarioAbonadoRepo = UsuarioAbonadoRepo

    def precioEstancia(self, matricula, pin):
        vehiculo = self.__vehiculoRepo.bucarPorMatricula(matricula)
        ticket = self.__ticketRepo.buscarPorPin(pin)
        ticket.fechaSalida = datetime.now()
        minutosTotales = (ticket.fechaSalida - ticket.fechaEntrada).minute
        print("Ha estado en el parking " +minutosTotales +" minutos")
        if(vehiculo.tipo == "Turismo"):
            ticket.precio = minutosTotales * 0.12
        elif(vehiculo.tipo == "Motocilceta"):
            ticket.precio = minutosTotales * 0.08
        elif(vehiculo.tipo == "Personas de movilidad reducida"):
            ticket.precio = minutosTotales * 0.10

        return ticket.precio

    def plazasDisponibles(self):
        contadorTicket = 0
        contadorAbonados = 0

        for Ticket in self.__ticketRepo.listaTickets:
            contadorTicket+=1

        for UsuarioAbonado in self.__UsuarioAbonadoRepo.listaAbonados:
            contadorAbonados+=1

        ocupadas = contadorTicket + contadorAbonados
        libres = self.__parking.numPlazas - ocupadas

        if (ocupadas < libres):
            print("Quedan "+libres +" plazas libres")
            return True
        else:
            return False


    #TODO




