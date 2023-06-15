import sqlite3 as sql

nombreBD = "BDCarParking.db"

def createDB():
    conn = sql.connect(nombreBD)
    conn.commit()
    conn.close()

def createTableVehiculos():
    conn=sql.connect(nombreBD)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Vehiculos(
         idVehiculo integer,
         nombreCliente text,
         placa text,
         tipo text
        )"""   
    )
    conn.commit()
    conn.close()

def insertRowVehiculos(idVehiculo,nombreCliente,placa,tipo):
    conn = sql.connect(nombreBD)
    cursor = conn.cursor()
    instruction = f"INSERT INTO Vehiculos VALUES ({idVehiculo},'{nombreCliente}','{placa}','{tipo}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def createTableClientes():
    conn=sql.connect(nombreBD)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Clientes(
         idCliente integer,
         nombre text,
         contacto text
        )"""   
    )
    conn.commit()
    conn.close()

def insertRowClientes(idCliente,nombre,contacto):
    conn = sql.connect(nombreBD)
    cursor = conn.cursor()
    instruction = f"INSERT INTO Clientes VALUES ({idCliente},'{nombre}','{contacto}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def createTableAdministradores():
    conn=sql.connect(nombreBD)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Administradores(
         usuario text,
         contrasenia text,
         llaveMaestra integer
        )"""   
    )
    conn.commit()
    conn.close()

def insertRowAdministradores(usuario,contrasenia,llaveMaestra):
    conn = sql.connect(nombreBD)
    cursor = conn.cursor()
    instruction = f"INSERT INTO Administradores VALUES ('{usuario}','{contrasenia}',{llaveMaestra})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def createTableTickets():
    conn=sql.connect(nombreBD)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Tickets(
         idTicket integer,
         nombreCliente text,
         horaIngreso text,
         horaSalida text,
         fecha text,
         placaVehiculo text,
         ubicacion integer,
         monto real,
         horasTotales real
        )"""   
    )
    conn.commit()
    conn.close()

def insertRowTickets(idTicket,nombreCliente,horaIngreso,horaSalida,fecha,placaVehiculo,ubicacion,monto,horasTotales):
    conn = sql.connect(nombreBD)
    cursor = conn.cursor()
    instruction = f"INSERT INTO Tickets VALUES ({idTicket},'{nombreCliente}','{horaIngreso}','{horaSalida}','{fecha}','{placaVehiculo}',{ubicacion},{monto},{horasTotales})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


def limpiarTable(tabla):
    conn = sql.connect(nombreBD)
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM   {}
        """.format(tabla)
    )
    conn.commit()
    conn.close()

#createDB()
#createTableClientes()
#createTableTickets()
#createTableVehiculos()
#createTableAdministradores()
#insertRowAdministradores("Rose","rose1",1)
#insertRowAdministradores("Jennie","jennie1",2)
#insertRowClientes(1234567,"Camila Cabello","camila@gmail.com")
#insertRowVehiculos(789456,"Camila Cabello","ABC123","Camioneta")
#insertRowTickets(3698527,"Camila Cabello","15:04:05","16:06:16","15-06-2023","ABC123",0,12,1)