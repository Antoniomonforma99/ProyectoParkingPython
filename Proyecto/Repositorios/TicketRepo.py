from ..Modelos import Ticket
from datetime import datetime

class Ticketrepo(object):
    def __init__(self, listaTickets):
        self.__listaTickets = listaTickets

    @property
    def listaTickets(self):
        return self.__listaTickets

    @listaTickets.setter
    def listaTickets(self, listaTickets):
        self.__listaTickets = listaTickets

    def generarPin(self):
        pin = Math

    def generarPlaza(self):
        plaza = Math
    #TODO


    def generarTicket(self, vehiculo):
        plaza = self.generarPlaza
        nuevoTicket = Ticket(vehiculo.matricula, datetime, vehiculo.id, plaza)
        self.__listaTickets.append(nuevoTicket)
        return nuevoTicket

    def imprimirTicketLlegada(self,ticket):
        ticket.pin = self.generarPin()
        print()
        print("Vehículo con matrícula "+ticket.matricula)
        print("Fecha llegada: " +ticket.fechaEntrada)
        print("Su pin es "+ticket.pin)
        print("Su número de plaza es "+ticket.plaza)

    def imprimirTicketSalida(self, ticket):
        ticket.fechaEntrada = datetime
        print()
        print("Vehículo con matrícula "+ticket.matricula)
        print("Fecha llegada: " +ticket.fechaEntrada)
        print("Fecha llegada: " +ticket.fechaSalida)
        print("El precio es de "+ticket.precio +" euros")
        print("Su número de plaza es "+ticket.plaza)

    def buscarPorPin(self, pin):
        for x in self.__listaTickets:
            if(self.__listaTickets[x] == pin):
                return self.__listaTickets[x]

    def buscarPorMatricula(self, matricula):
        for x in self.__listaTickets:
            if(self.__listaTickets[x].matricula == matricula):
                return self.__listaTickets[x]

    def agregarTicket(self, ticket):
        return self.__listaTickets.append(ticket)

