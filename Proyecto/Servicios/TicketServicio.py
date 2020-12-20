class TicketServicio(object):
    def __init__(self, ticketRepo):
        self.__ticketRepo = ticketRepo

    @property
    def ticketRepo(self):
        return self.__ticketRepo

    @ticketRepo.setter
    def ticketRepo(self, ticketRepo):
        self.__ticketRepo = ticketRepo

    def imprimirTicketDeposito(self, ticket):
        return self.__ticketRepo.imprimirTicketLlegada(ticket)

    def imprimirTicketSalida(self, ticket):
        return self.__ticketRepo.imprimirTicketSalida(ticket)
