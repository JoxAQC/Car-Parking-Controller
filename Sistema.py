from Administrador import Administrador
from Cliente import Cliente
from Reporte import Reporte
from Ticket import Ticket
from Vehiculo import Vehiculo
import numpy as np
import datetime
import sqlite3 as sql
import random

nombreBD = "BDCarParking.db"

class Sistema:
    def __init__(self, estado):
        self.__estado = estado
        self.__tarifas = [2.50, 4.50, 6.50]

    def get_tarifas(self):
        return self.__tarifas

    # Setter para el atributo estado
    def set_estado(self, estado):
        self.__estado = estado

    def generarIdAleatorio(self):
    # Generar un número entero aleatorio de 7 dígitos
        idAleatorio = int(random.randint(1000000, 9999999))
        return idAleatorio
    
    def obtenerFechaHoraActual(self):
        # Obtener la fecha y hora actual
        fecha_hora_actual = datetime.datetime.now()
        # Formatear la fecha y hora en formato de cadena (dd/mm/aaaa HH:MM:SS)
        fecha_hora_actual_str = fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")
        return fecha_hora_actual_str
    
    def obtenerFechaActual(self):
        # Obtener la fecha actual
        fecha_actual = datetime.date.today()

        # Formatear la fecha en formato de cadena (dd/mm/aaaa)
        fecha_actual_str = fecha_actual.strftime("%d/%m/%Y")

        return fecha_actual_str
        
    def registrarCliente(self, cliente):
        conn = sql.connect(nombreBD)
        cursor = conn.cursor()
        # Insertar los datos del ticket en la tabla Tickets
        cursor.execute(
            "INSERT INTO Clientes (idCliente, nombre, contacto) VALUES (?, ?, ?)",
            (cliente.get_idCliente(),cliente.get_nombre(),cliente.get_contacto())
        )
        conn.commit()
        conn.close()

    def registrarVehiculo(self,cliente,vehiculo):
        conn = sql.connect(nombreBD)
        cursor = conn.cursor()
        # Insertar los datos del ticket en la tabla Tickets
        cursor.execute(
            "INSERT INTO Vehiculos (idVehiculo, nombreCliente, placa, tipo) VALUES (?, ?, ?, ?)",
            (vehiculo.get_idVehiculo(),cliente.get_nombre(),vehiculo.get_placa(),vehiculo.get_tipo())
        )
        conn.commit()
        conn.close()

    def crearEstacionamiento(self): #Matriz y FILA secuencial
        tamanioMatriz = int(input("Ingrese el tamanio del estacionamiento: "))
         # Crear una matriz nxn llena de ceros
        estacionamiento = np.zeros((tamanioMatriz, tamanioMatriz), dtype=int)
        # Guardar la matriz en un archivo
        np.savetxt('estacionamiento.txt', estacionamiento, fmt='%d')
        

    from datetime import datetime

    def liberarVehiculo(self, placa):
        tickets = self.obtenerTicketsPorPlaca(placa)

        if tickets:
            ticket_mas_reciente = max(tickets, key=lambda ticket: ticket.get_horaIngreso())

            for ticket in tickets:
                if ticket == ticket_mas_reciente:
                    # Actualizar horaSalida
                    hora_salida = self.obtenerFechaHoraActual()
                    ticket.set_horaSalida(hora_salida)

                    # Calcular horasTotales
                    hora_ingreso = ticket.get_horaIngreso()
                    tiempo_ingreso = datetime.datetime.strptime(hora_ingreso, "%d/%m/%Y %H:%M:%S")

                    # Obtener la fecha y hora actual
                    tiempo_salida = datetime.datetime.now()

                    # Calcular la diferencia de tiempo
                    diferencia_tiempo = tiempo_salida - tiempo_ingreso

                    # Calcular las horas totales
                    horas_totales = diferencia_tiempo.total_seconds() // 3600
                    ticket.set_horasTotales(horas_totales)

                    # Actualizar monto
                    monto_actualizado = ticket.get_monto() * horas_totales
                    ticket.set_monto(monto_actualizado)

                    # Actualizar el ticket en la base de datos
                    conn = sql.connect(nombreBD)
                    cursor = conn.cursor()
                    query = "UPDATE Tickets SET horaSalida=?, horasTotales=?, monto=? WHERE idTicket=?"
                    cursor.execute(query, (ticket.get_horaSalida(), ticket.get_horasTotales(), ticket.get_monto(), ticket.get_idTicket()))
                    conn.commit()
                    conn.close()

        pass

    def generarReporteDiario(self):
        pass

    def verReportes(self):
        pass

    def asignarUbicacion(self):
        # Cargar la matriz de estacionamiento desde el archivo
        estacionamiento = np.loadtxt('estacionamiento.txt', dtype=int)
        # Obtener las dimensiones de la matriz
        n = estacionamiento.shape[0]
        # Buscar una posición vacía en la matriz
        for i in range(n):
            for j in range(n):
                if estacionamiento[i][j] == 0:
                    # Marcar la posición como ocupada (1)
                    estacionamiento[i][j] = 1
                    # Guardar la matriz actualizada en el archivo
                    np.savetxt('estacionamiento.txt', estacionamiento, fmt='%d')
                    # Calcular la ubicación como un número entero único
                    ubicacion = i * n + j
                    # Retornar la ubicación ocupada encontrada
                    return ubicacion

    def liberarUbicacion(ubicacion):
        # Cargar la matriz de estacionamiento desde el archivo
        estacionamiento = np.loadtxt('estacionamiento.txt', dtype=int)
        # Obtener las dimensiones de la matriz
        n = estacionamiento.shape[0]
        # Calcular las coordenadas de la ubicación a liberar
        fila = ubicacion // n
        columna = ubicacion % n
        # Marcar la posición como vacía (0)
        estacionamiento[fila][columna] = 0
        # Guardar la matriz actualizada en el archivo
        np.savetxt('estacionamiento.txt', estacionamiento, fmt='%d')

    def verEstacionamiento(self):
        # Verificar la existencia del archivo de estacionamiento
        try:
            estacionamiento = np.loadtxt('estacionamiento.txt', dtype=int)
        except IOError:
            print("No se encontro el archivo de estacionamiento.")
            return
        # Obtener las dimensiones de la matriz de estacionamiento
        filas, columnas = estacionamiento.shape
        # Etiquetas para las filas y columnas
        etiquetas_filas = ['f' + str(i) for i in range(filas)]
        
        # Imprimir la matriz de estacionamiento
        print("Estacionamiento:")
        print(" ", end="")
        print()
        for i, fila in enumerate(estacionamiento):
            print(etiquetas_filas[i], end=": ")
            for valor in fila:
                print(valor, end=" ")
            print()

    def validarAdministrador(self,administrador):
        usuario = administrador.get_usuario()
        contrasenia = administrador.get_contrasenia()
        llaveMaestra = administrador.get_llaveMaestra()
        conn = sql.connect(nombreBD)
        cursor = conn.cursor()
        query = "SELECT * FROM Administradores WHERE usuario=? AND contrasenia=? AND llaveMaestra=?"
        cursor.execute(query, (usuario, contrasenia, llaveMaestra))
        resultado = cursor.fetchone()
        conn.close()
        if resultado is not None:
            return True
        else:
            return False

    def validarEspacioEstacionamiento(self):
        pass
    
    def limpiarEstacionamiento(self):
        # Verificar la existencia del archivo de estacionamiento
        try:
            estacionamiento = np.loadtxt('estacionamiento.txt', dtype=int)
        except IOError:
            print("No se encontró el archivo de estacionamiento.")
            return
        # Llenar la matriz de estacionamiento con ceros
        estacionamiento.fill(0)
        # Guardar la matriz actualizada en el archivo
        np.savetxt('estacionamiento.txt', estacionamiento, fmt='%d')
    
    def imprimirClientes(self):
        pass

    def obtenerVehiculoPlaca(self,placaBuscada):
        conn = sql.connect(nombreBD)
        cursor = conn.cursor()
        # Consulta para buscar un vehículo por placa
        query = "SELECT * FROM Vehiculos WHERE placa=?"
        cursor.execute(query, (placaBuscada,))
        resultado = cursor.fetchone()
        conn.close()
        if resultado is not None:
            idVehiculo = resultado[0]
            tipo = resultado[3]
            vehiculo = Vehiculo(idVehiculo,placaBuscada,tipo)
            return vehiculo
        else:
            return None

    def obtenerTicketsPorPlaca(self, placa):
        conn = sql.connect(nombreBD)
        cursor = conn.cursor()
        # Consulta para buscar tickets por placa
        query = "SELECT * FROM Tickets WHERE placaVehiculo=?"
        cursor.execute(query, (placa,))
        resultados = cursor.fetchall()
        conn.close()
        tickets = []
        if resultados:
            for resultado in resultados:
                idTicket = resultado[0]
                horaIngreso = resultado[2]
                horaSalida = resultado[3]
                fecha = resultado[4]
                ubicacion = resultado[6]
                monto = resultado[7]
                horasTotales = resultado[8]
                vehiculo = self.obtenerVehiculoPlaca(placa)  # Obtener el vehículo asociado al ticket
                ticket = Ticket(idTicket, horaIngreso, horaSalida, fecha, ubicacion, vehiculo, monto, horasTotales)
                tickets.append(ticket)

        return tickets  

    def obtenerClientePorNombre(self, nombreCliente):
        conn = sql.connect(nombreBD)
        cursor = conn.cursor()
        # Consultar los datos del cliente por su nombre en la tabla Clientes
        cursor.execute("SELECT idCliente, contacto FROM Clientes WHERE nombre = ?", (nombreCliente,))
        resultado = cursor.fetchone()
        conn.close()
        if resultado:
            idCliente, contacto = resultado
            # Crear un objeto Cliente con los datos obtenidos
            cliente = Cliente(idCliente, nombreCliente, contacto)
            return cliente
        return None
        
    def buscarPlaca(self,placaBuscada):
        conn = sql.connect(nombreBD)
        cursor = conn.cursor()
        # Consulta para buscar un vehículo por placa
        query = "SELECT * FROM Vehiculos WHERE placa=?"
        cursor.execute(query, (placaBuscada,))
        resultado = cursor.fetchone()
        conn.close()
        if resultado is not None:
            return True
        else:
            return False

    def buscarNombre(self,nombre):
        conn = sql.connect(nombreBD)
        cursor = conn.cursor()
        # Consulta para buscar un cliente por nombre
        query = "SELECT * FROM Clientes WHERE nombre=?"
        cursor.execute(query, (nombre,))
        resultado = cursor.fetchone()
        conn.close()
        if resultado is not None:
            return True
        else:
            return False
        
    def generarTicket(self, cliente, vehiculo, ticket,ubicacion):
        conn = sql.connect(nombreBD)
        cursor = conn.cursor()
        # Insertar los datos del ticket en la tabla Tickets
        cursor.execute(
            "INSERT INTO Tickets (idTicket, nombreCliente, horaIngreso, horaSalida, fecha, placaVehiculo, ubicacion, monto, horasTotales) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (ticket.get_idTicket(), cliente.get_nombre(), ticket.get_horaIngreso(), ticket.get_horaSalida(), ticket.get_fecha(), vehiculo.get_placa(), ubicacion, ticket.get_monto(), ticket.get_horasTotales())
        )
        conn.commit()
        conn.close()
  
    def obtenerNombreClientePorPlaca(self, placaVehiculo):
        conn = sql.connect(nombreBD)
        cursor = conn.cursor()

        # Consultar el nombre del cliente por la placa del vehículo en la tabla Vehiculos
        cursor.execute("SELECT nombreCliente FROM Vehiculos WHERE placa = ?", (placaVehiculo,))
        resultado = cursor.fetchone()

        conn.close()

        if resultado:
            nombreCliente = resultado[0]
            return nombreCliente

        return None

def main():
    print("Iniciar Sesion")
    sistema = Sistema("Activo")
    tarifas = sistema.get_tarifas() 
    #usuario = input("Usuario: ")
    #contrasenia = input("Contrasenia: ")
    #llaveMaestra = int(input("Llave Maestra: "))
    admin = Administrador("Rose","rose1",1)
    if sistema.validarAdministrador(admin):
        print("Bienvenido al ESTACIONAMIENTO MONO!")
        opcion = None
        while opcion != 0:
            print("----- Menu -----")
            print("1. Ingresar Vehiculo")
            print("2. Liberar Vehiculo")
            print("3. Ver Estacionamiento Disponible")
            print("4. Ver Reportes")
            print("5. Crear Estacionamiento")
            print("6. Limpiar Estacionamiento")
            print("0. Salir")
            opcion = int(input("Ingrese una opcion: "))
            
            if opcion == 1:
                placaBuscada = input("Ingrese la placa del vehiculo: ")
                vehiculoEncontrado = sistema.buscarPlaca(placaBuscada)
                if vehiculoEncontrado == True:
                    #El cliente ya esta en la base de datos
                    idTicket = sistema.generarIdAleatorio()
                    horaIngreso = sistema.obtenerFechaHoraActual()
                    horaSalida = ""
                    fecha = sistema.obtenerFechaActual()
                    monto = 0
                    horasTotales = 0
                    ubicacion = int(sistema.asignarUbicacion())
                    print(ubicacion)
                    vehiculo = sistema.obtenerVehiculoPlaca(placaBuscada)
                    tipo = vehiculo.get_tipo()
                    if tipo == "moto":
                        monto = tarifas[0]  # Obtener el valor de la posición 0 del vector de tarifas
                    elif tipo == "auto":
                        monto = tarifas[1]  # Obtener el valor de la posición 1 del vector de tarifas
                    elif tipo == "camioneta":
                        monto = tarifas[2]  # Obtener el valor de la posición 2 del vector de tarifas
                    nombreCliente = sistema.obtenerNombreClientePorPlaca(placaBuscada)
                    vehiculoTicket = [vehiculo]
                    cliente = sistema.obtenerClientePorNombre(nombreCliente)
                    ticketNuevo = Ticket(idTicket, horaIngreso, horaSalida, fecha, ubicacion,vehiculoTicket, monto, horasTotales)
                    sistema.generarTicket(cliente,vehiculo,ticketNuevo,ubicacion)
                else:
                    clienteBuscado = input("Ingrese nombre del cliente: ")
                    clienteEncontrado = sistema.buscarNombre(clienteBuscado)
                    if clienteEncontrado == True:
                        cliente = sistema.obtenerClientePorNombre(clienteBuscado)
                        idVehiculo = sistema.generarIdAleatorio()
                        tipo = input("Ingrese el tipo de vehiculo: ")
                        vehiculo = (Vehiculo(idVehiculo, placaBuscada, tipo))
                        idTicket = sistema.generarIdAleatorio()
                        horaIngreso = sistema.obtenerFechaHoraActual()
                        horaSalida = ""
                        fecha = sistema.obtenerFechaActual()
                        if tipo == "moto":
                            monto = tarifas[0]  # Obtener el valor de la posición 0 del vector de tarifas
                        elif tipo == "auto":
                            monto = tarifas[1]  # Obtener el valor de la posición 1 del vector de tarifas
                        elif tipo == "camioneta":
                            monto = tarifas[2]  # Obtener el valor de la posición 2 del vector de tarifas
                        horasTotales = 0
                        ubicacion = int(sistema.asignarUbicacion())
                        ticketNuevo = Ticket(idTicket, horaIngreso, horaSalida, fecha, vehiculo,ubicacion, monto, horasTotales)
                        sistema.registrarVehiculo(cliente,vehiculo)
                        sistema.generarTicket(cliente,vehiculo,ticketNuevo,ubicacion)
                    else:
                        idCliente = sistema.generarIdAleatorio()
                        contacto = input("Ingrese contacto: ")
                        idVehiculo = sistema.generarIdAleatorio()
                        tipo = input("Ingrese el tipo de vehiculo: ").lower()
                        if tipo == "moto":
                            monto = tarifas[0]  # Obtener el valor de la posición 0 del vector de tarifas
                        elif tipo == "auto":
                            monto = tarifas[1]  # Obtener el valor de la posición 1 del vector de tarifas
                        elif tipo == "camioneta":
                            monto = tarifas[2]  # Obtener el valor de la posición 2 del vector de tarifas
                        vehiculo = (Vehiculo(idVehiculo, placaBuscada, tipo))
                        idTicket = sistema.generarIdAleatorio()
                        horaIngreso = sistema.obtenerFechaHoraActual()
                        horaSalida = ""
                        fecha = sistema.obtenerFechaActual()
                        horasTotales = 0
                        ubicacion = int(sistema.asignarUbicacion())
                        ticketNuevo = Ticket(idTicket, horaIngreso, horaSalida, fecha, vehiculo,ubicacion, monto, horasTotales)
                        cliente = Cliente(idCliente,clienteBuscado,contacto)
                        sistema.registrarCliente(cliente)
                        sistema.registrarVehiculo(cliente,vehiculo)
                        sistema.generarTicket(cliente,vehiculo,ticketNuevo,ubicacion)

            elif opcion == 2:
                placaBuscada = input("Ingrese la placa del vehiculo: ")
                sistema.liberarVehiculo(placaBuscada)
                pass
            elif opcion == 3:
                sistema.verEstacionamiento()
            elif opcion == 4:
                pass
            elif opcion == 5:
                sistema.crearEstacionamiento()
            elif opcion == 6:
                sistema.limpiarEstacionamiento()
            elif opcion == 0:
                print("Saliendo del programa...")
            else:
                print("Opcion invalida. Por favor, seleccione una opcion valida.")
            print()
    else:
        print("Credenciales incorrectas.")

if __name__ == "__main__":
    main()