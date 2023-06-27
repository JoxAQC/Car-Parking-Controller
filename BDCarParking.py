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

#limpiarTable("Clientes")
#limpiarTable("Tickets")
#limpiarTable("Vehiculos")
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
#insertRowTickets(3698527,"Camila Cabello","15:04:05","16:06:16","15-01-2023","ABC123",0,12,1)
#insertRowTickets(1234567,"Juan Perez","09:30:00","10:45:30","22-01-2023","XYZ789",1,25,3)
#insertRowTickets(9876543,"Maria Gomez","12:15:10","14:30:45","05-01-2023","DEF456",0,8,2)
#insertRowTickets(2468135,"Pedro Rodriguez","17:45:20","18:20:55","11-01-2023","GHI987",1,50,5)
insertRowTickets(123456,"John Doe","01/01/2023 08:30:00","01/01/2023 10:45:00","01/01/2023","ABC123",0,15,1)
insertRowTickets(789012,"Jane Smith","05/01/2023 13:15:00","05/01/2023 14:30:00","05/01/2023","DEF456",0,20,1)
insertRowTickets(345678,"Michael Johnson","10/01/2023 09:00:00","10/01/2023 10:30:00","10/01/2023","GHI789",0,12,1)
insertRowTickets(901234,"Emily Davis","15/01/2023 16:45:00","15/01/2023 17:15:00","15/01/2023","JKL012",0,18,1)
insertRowTickets(567890,"David Wilson","20/01/2023 11:30:00","20/01/2023 12:45:00","20/01/2023","MNO345",0,25,2)
insertRowTickets(234567,"Sarah Johnson","25/01/2023 14:00:00","25/01/2023 15:30:00","25/01/2023","PQR678",0,10,2)
insertRowTickets(890123,"Michael Davis","01/02/2023 09:30:00","01/02/2023 11:00:00","01/02/2023","STU901",0,22,1)
insertRowTickets(456789,"Emily Wilson","05/02/2023 13:45:00","05/02/2023 15:00:00","05/02/2023","VWX234",0,16,1)
insertRowTickets(234567,"David Johnson","10/02/2023 10:00:00","10/02/2023 11:30:00","10/02/2023","YZA567",0,19,1)
insertRowTickets(901234,"Sarah Smith","15/02/2023 15:30:00","15/02/2023 16:45:00","15/02/2023","BCD890",0,14,2)
insertRowTickets(567890,"John Wilson","20/02/2023 12:15:00","20/02/2023 13:30:00","20/02/2023","EFG123",0,21,2)
insertRowTickets(123456,"Jane Johnson","25/02/2023 16:00:00","25/02/2023 17:30:00","25/02/2023","HIJ456",0,11,1)
insertRowTickets(789012,"Michael Davis","01/03/2023 09:15:00","01/03/2023 10:30:00","01/03/2023","KLM789",0,23,1)
insertRowTickets(345678,"Emily Smith","05/03/2023 14:45:00","05/03/2023 16:00:00","05/03/2023","NOP012",0,17,1)
insertRowTickets(901234,"David Wilson","10/03/2023 10:30:00","10/03/2023 11:45:00","10/03/2023","QRS345",0,13,2)
insertRowTickets(567890,"Sarah Johnson","15/03/2023 15:00:00","15/03/2023 16:15:00","15/03/2023","TUV678",0,26,2)
insertRowTickets(234567,"John Doe","20/03/2023 11:45:00","20/03/2023 13:00:00","20/03/2023","WXY901",0,18,1)
insertRowTickets(890123,"Jane Smith","25/03/2023 15:30:00","25/03/2023 16:45:00","25/03/2023","ZAB234",0,15,1)
insertRowTickets(456789,"Michael Johnson","01/04/2023 10:15:00","01/04/2023 11:30:00","01/04/2023","CDE567",0,20,1)
insertRowTickets(234567,"Emily Davis","05/04/2023 14:30:00","05/04/2023 15:45:00","05/04/2023","FGH890",0,16,2)
insertRowTickets(901234,"David Wilson","10/04/2023 11:00:00","10/04/2023 12:15:00","10/04/2023","IJK123",0,24,2)
insertRowTickets(567890,"Sarah Johnson","15/04/2023 16:45:00","15/04/2023 18:00:00","15/04/2023","LMN456",0,19,1)
insertRowTickets(234567,"John Doe","20/04/2023 12:30:00","20/04/2023 13:45:00","20/04/2023","OPQ789",0,14,1)
insertRowTickets(890123,"Jane Smith","25/04/2023 16:15:00","25/04/2023 17:30:00","25/04/2023","RST012",0,22,2)
insertRowTickets(456789,"Michael Johnson","01/05/2023 10:45:00","01/05/2023 12:00:00","01/05/2023","UVW345",0,18,2)
insertRowTickets(234567,"Emily Davis","05/05/2023 15:00:00","05/05/2023 16:15:00","05/05/2023","XYZ678",0,25,1)
insertRowTickets(901234,"David Wilson","10/05/2023 11:30:00","10/05/2023 12:45:00","10/05/2023","ABC901",0,13,1)
insertRowTickets(567890,"Sarah Johnson","15/05/2023 16:15:00","15/05/2023 17:30:00","15/05/2023","DEF234",0,21,2)
insertRowTickets(234567,"John Doe","20/05/2023 12:45:00","20/05/2023 14:00:00","20/05/2023","GHI567",0,16,2)
insertRowTickets(890123,"Jane Smith","25/05/2023 16:30:00","25/05/2023 17:45:00","25/05/2023","JKL890",0,12,1)
insertRowTickets(456789,"Michael Johnson","01/06/2023 11:00:00","01/06/2023 12:15:00","01/06/2023","MNO123",0,23,1)
insertRowTickets(234567,"Emily Davis","05/06/2023 15:15:00","05/06/2023 16:30:00","05/06/2023","PQR456",0,17,2)
insertRowTickets(901234,"David Wilson","10/06/2023 11:30:00","10/06/2023 12:45:00","10/06/2023","STU789",0,19,2)
insertRowTickets(567890,"Sarah Johnson","15/06/2023 16:45:00","15/06/2023 18:00:00","15/06/2023","VWX012",0,14,1)
insertRowTickets(234567,"John Doe","20/06/2023 13:00:00","20/06/2023 14:15:00","20/06/2023","YZA345",0,20,1)
insertRowTickets(890123,"Jane Smith","25/06/2023 17:30:00","25/06/2023 18:45:00","25/06/2023","BCD678",0,15,2)
