class Ticket:
    def __init__(self,idTicket,horaIngreso,horaSalida,fecha,vehiculo,monto,horasTotales):
        self.__idTicket = idTicket
        self.__horaIngreso = horaIngreso
        self.__horaSalida = horaSalida
        self.__fecha = fecha
        self.__vehiculo = vehiculo
        self.__monto = monto
        self.__horasTotales = horasTotales 