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
