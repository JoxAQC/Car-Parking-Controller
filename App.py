import customtkinter
from tkinter import ttk
import tkinter as tk
import os
from PIL import Image
from Sistema import Sistema
from Ticket import Ticket
from Vehiculo import Vehiculo
import numpy as np
from Cliente import Cliente

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

tarifas = [2.50, 4.50, 6.50]

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("SpotGuard")
        self.geometry("1000x500")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.historial_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "expediente.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "expediente_blanco.png")), size=(20, 20))
        self.add_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "agregar_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "agregar.png")), size=(20, 20))
        self.manage_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "gestionar_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "gestionar.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  SpotGuard", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Página principal",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Agregar vehículo",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Gestionar vehículos",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.manage_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Historial y reportes",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.historial_image, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="Estacionamiento Disponible", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.home_frame_large_image_label.grid(row=0, column=3, columnspan=15, padx=30, pady=(15, 15), sticky="nsew")

        self.mostrarEstacionamiento()

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        
        self.login_label = customtkinter.CTkLabel(self.second_frame, text="Registrar Vehículo",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, columnspan=2, padx=30, pady=(30, 15))

        self.placa_entry = customtkinter.CTkEntry(self.second_frame, width=100, placeholder_text="Placa")
        self.placa_entry.grid(row=1, column=0, padx=(30,15), pady=(0, 15), sticky="nsew")
        self.buscar_button = customtkinter.CTkButton(self.second_frame, text="Buscar Placa",  width=100, command=self.buscarPorPlaca)
        self.buscar_button.grid(row=1, column=1, padx=(15,30), pady=(0, 15), sticky="nsew")

        self.name_entry = customtkinter.CTkEntry(self.second_frame, width=200, placeholder_text="Nombre", state="disabled")
        self.name_entry.grid(row=2, column=0, padx=(30,15), pady=(0, 15), sticky="nsew")
        self.buscarCliente_button = customtkinter.CTkButton(self.second_frame, text="Buscar Cliente",  width=100, state="disabled", command=self.buscarPorNombre)
        self.buscarCliente_button.grid(row=2, column=1, padx=(15,30), pady=(0, 15), sticky="nsew")

        self.contact_entry = customtkinter.CTkEntry(self.second_frame, width=200, placeholder_text="Contacto", state="disabled")
        self.contact_entry.grid(row=3, column=0, columnspan=2, padx=30, pady=(0, 15), sticky="nsew")
        self.type_entry = customtkinter.CTkOptionMenu(self.second_frame, width=200, values=["Moto", "Auto", "Camioneta"], state="disabled", fg_color = "black")
        self.type_entry.grid(row=4, column=0, columnspan=2, padx=30, pady=(0, 15), sticky="nsew")
        self.registrar_button = customtkinter.CTkButton(self.second_frame, text="Registrar",  width=200, state="disabled", command=self.registrarNuevo)
        self.registrar_button.grid(row=5, column=0, columnspan=2, padx=30, pady=(15, 15))

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)
        
        self.reg_label = customtkinter.CTkLabel(self.third_frame, text="Retirar Vehículo",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.reg_label.grid(row=0, column=0, columnspan=2, padx=30, pady=(30, 15))

        self.placa_ret = customtkinter.CTkEntry(self.third_frame, width=300, placeholder_text="Ingrese la placa")
        self.placa_ret.grid(row=1, column=0, padx=(30,15), pady=(15, 15))

        self.ret = customtkinter.CTkButton(self.third_frame, text="Retirar",  width=200, command=self.show_selection)
        self.ret.grid(row=2, column=0, padx=15, pady=15)



        # create fourth frame
        self.fourth_frame = ttk.Treeview(self, columns=("col1","col2","col3","col4", "col5","col6", "col7"))
        # self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        # self.third_frame.grid_columnconfigure(0, weight=1)
        

        self.fourth_frame.column("#0",width=60, anchor="center")
        self.fourth_frame.column("col1",width=80, anchor="center")
        self.fourth_frame.column("col2",width=40, anchor="center")
        self.fourth_frame.column("col3",width=20, anchor="center")
        self.fourth_frame.column("col4",width=100, anchor="center")
        self.fourth_frame.column("col5",width=100, anchor="center")
        self.fourth_frame.column("col6",width=40, anchor="center")
        self.fourth_frame.column("col7",width=20, anchor="center")

        self.fourth_frame.heading("#0", text="ID", anchor="center")
        self.fourth_frame.heading("col1", text="Nombre", anchor="center")
        self.fourth_frame.heading("col2", text="Placa", anchor="center")
        self.fourth_frame.heading("col3", text="Ubicación", anchor="center")
        self.fourth_frame.heading("col4", text="Ingreso", anchor="center")
        self.fourth_frame.heading("col5", text="Salida", anchor="center")
        self.fourth_frame.heading("col6", text="Horas", anchor="center")
        self.fourth_frame.heading("col7", text="Monto", anchor="center")

        self.mostrarHistorial()

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")
    
    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")  

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def buscarPorPlaca(self):
        vehiculoEncontrado = Sistema.buscarPlaca(self.placa_entry.get())
        if vehiculoEncontrado:
            idTicket = Sistema.generarIdAleatorio()
            horaIngreso = Sistema.obtenerFechaHoraActual()
            horaSalida = ""
            fecha = Sistema.obtenerFechaActual()
            monto = 0
            horasTotales = 0
            ubicacion = int(Sistema.asignarUbicacion())
            print(ubicacion)
            vehiculo = Sistema.obtenerVehiculoPlaca(self.placa_entry.get())
            tipo = vehiculo.get_tipo()
            if tipo == "moto":
                monto = tarifas[0]  # Obtener el valor de la posición 0 del vector de tarifas
            elif tipo == "auto":
                monto = tarifas[1]  # Obtener el valor de la posición 1 del vector de tarifas
            elif tipo == "camioneta":
                monto = tarifas[2]  # Obtener el valor de la posición 2 del vector de tarifas
            nombreCliente = Sistema.obtenerNombreClientePorPlaca(self.placa_entry.get())
            vehiculoTicket = [vehiculo]
            cliente = Sistema.obtenerClientePorNombre(nombreCliente)
            ticketNuevo = Ticket(idTicket, horaIngreso, horaSalida, fecha, ubicacion,vehiculoTicket, monto, horasTotales)
            Sistema.generarTicket(cliente,vehiculo,ticketNuevo,ubicacion)
            self.mostrar_cuadro_emergente()
            self.reiniciar()
        else:
            self.placa_entry.configure(state="disabled")
            self.buscar_button.configure(state="disabled")
            self.name_entry.configure(state="normal")
            self.buscarCliente_button.configure(state="normal")

    def buscarPorNombre(self):
        clienteEncontrado = Sistema.buscarNombre(self.name_entry.get())
        if clienteEncontrado == True:
            self.type_entry.configure(state="normal")
            self.buscarCliente_button.configure(text="Registrar", command=self.registrarAuto) 
            self.mostrar_cuadro_emergente()
        else:
            self.name_entry.configure(state="disabled")
            self.buscarCliente_button.configure(state="disabled")
            self.contact_entry.configure(state="normal")
            self.type_entry.configure(state="normal")
            self.registrar_button.configure(state="normal")

    def registrarAuto(self):
        cliente = Sistema.obtenerClientePorNombre(self.name_entry.get())
        idVehiculo = Sistema.generarIdAleatorio()
        tipo = self.type_entry.get().lower()
        vehiculo = (Vehiculo(idVehiculo, self.placa_entry.get(), tipo))
        idTicket = Sistema.generarIdAleatorio()
        horaIngreso = Sistema.obtenerFechaHoraActual()
        horaSalida = ""
        fecha = Sistema.obtenerFechaActual()
        if tipo == "moto":
            monto = tarifas[0]  # Obtener el valor de la posición 0 del vector de tarifas
        elif tipo == "auto":
            monto = tarifas[1]  # Obtener el valor de la posición 1 del vector de tarifas
        elif tipo == "camioneta":
            monto = tarifas[2]  # Obtener el valor de la posición 2 del vector de tarifas
        horasTotales = 0
        ubicacion = int(Sistema.asignarUbicacion())
        ticketNuevo = Ticket(idTicket, horaIngreso, horaSalida, fecha, vehiculo,ubicacion, monto, horasTotales)
        Sistema.registrarVehiculo(cliente,vehiculo)
        Sistema.generarTicket(cliente,vehiculo,ticketNuevo,ubicacion)   
        self.mostrar_cuadro_emergente()
        self.reiniciar()

    def registrarNuevo(self):
        idCliente = Sistema.generarIdAleatorio()
        contacto = self.contact_entry.get()
        idVehiculo = Sistema.generarIdAleatorio()
        tipo = self.type_entry.get().lower()
        if tipo == "moto":
            monto = tarifas[0]  # Obtener el valor de la posición 0 del vector de tarifas
        elif tipo == "auto":
            monto = tarifas[1]  # Obtener el valor de la posición 1 del vector de tarifas
        elif tipo == "camioneta":
            monto = tarifas[2]  # Obtener el valor de la posición 2 del vector de tarifas
        vehiculo = (Vehiculo(idVehiculo, self.placa_entry.get(), tipo))
        idTicket = Sistema.generarIdAleatorio()
        horaIngreso = Sistema.obtenerFechaHoraActual()
        horaSalida = ""
        fecha = Sistema.obtenerFechaActual()
        horasTotales = 0
        ubicacion = int(Sistema.asignarUbicacion())
        ticketNuevo = Ticket(idTicket, horaIngreso, horaSalida, fecha, vehiculo,ubicacion, monto, horasTotales)
        cliente = Cliente(idCliente,self.name_entry.get(),contacto)
        Sistema.registrarCliente(cliente)
        Sistema.registrarVehiculo(cliente,vehiculo)
        Sistema.generarTicket(cliente,vehiculo,ticketNuevo,ubicacion)
        self.mostrar_cuadro_emergente()
        self.reiniciar()
            
    def show_selection(self):
        placa = self.placa_ret.get()
        ticket = Sistema.liberarVehiculo(placa)
        self.reiniciar()

        # Después de actualizar el ticket más reciente
        Sistema.imprimirTicket(ticket) 

    def mostrar_cuadro_emergente(self):
        cuadro_emergente = tk.Toplevel()
        cuadro_emergente.title("Mensaje")
        
        mensaje_label = tk.Label(cuadro_emergente, text="Correctamente registrado")
        mensaje_label.pack(padx=20, pady=20)

    def reiniciar(self):
        self.mostrarEstacionamiento()
        self.mostrarHistorial()
        self.placa_entry.delete(0, 'end')
        self.buscar_button.configure(state="normal")

        self.name_entry.delete(0, 'end')
        self.name_entry.configure(placeholder_text="Nombre", state="disabled")
        self.buscarCliente_button.configure(text="Buscar Cliente",state="disabled", command=self.buscarPorNombre)

        self.contact_entry.delete(0, 'end')
        self.contact_entry.configure(placeholder_text="Contacto", state="disabled")
        self.type_entry.configure(state="disabled")
        self.registrar_button.configure(state="disabled")
        self.placa_ret.delete(0, 'end')


    def mostrarEstacionamiento(self):
        estacionamiento=Sistema.devolverstacionamiento()
  
        for j, fila in enumerate(estacionamiento):
            i=0
            for valor in fila:
                i=i+1
                if valor==1:
                    self.home_frame_button = customtkinter.CTkButton(self.home_frame, text="", width=10, height=10,state="disabled", fg_color="red")
                    self.home_frame_button.grid(row=j+1, column=i, padx=15, pady=5.5)
                else:
                    self.home_frame_button = customtkinter.CTkButton(self.home_frame, text="", width=10, height=10,state="disabled")
                    self.home_frame_button.grid(row=j+1, column=i, padx=15, pady=5.5)

    def mostrarHistorial(self):
        self.datos2 = Sistema.recopilarHistorial()

        self.fourth_frame.heading("#0", text="ID", anchor="center")
        self.fourth_frame.heading("col1", text="Nombre", anchor="center")
        self.fourth_frame.heading("col2", text="Placa", anchor="center")
        self.fourth_frame.heading("col3", text="Ubicación", anchor="center")
        self.fourth_frame.heading("col4", text="Ingreso", anchor="center")
        self.fourth_frame.heading("col5", text="Salida", anchor="center")
        self.fourth_frame.heading("col6", text="Horas", anchor="center")
        self.fourth_frame.heading("col7", text="Monto", anchor="center")

        for element in self.datos2:
            self.fourth_frame.insert("","end",text=element[0], values=(element[1],element[5], element[6], element[2], element[3], element[7], element[6]))


ventanaIniciarSesion = customtkinter.CTk()

ventanaIniciarSesion.geometry("600x420")

def login():
    user = Sistema.iniciarSesion(entry1.get(), entry2.get(), entry3.get())
    if user is not None:
        ventanaIniciarSesion.destroy()
        app = App()
        app.mainloop()

# Ventana Iniciar Sesion
fr = customtkinter.CTkFrame(master=ventanaIniciarSesion)
fr.pack(pady=40, padx=120, fill="both", expand=True)

label = customtkinter.CTkLabel(master=fr, width=120, height=32, text="Iniciar Sesión", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=fr, width=240, height=32, placeholder_text="Usuario")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=fr, width=240, height=32, placeholder_text="Contraseña", show="*")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=fr, width=240, height=32, placeholder_text="Llave maestra", show="*")
entry3.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=fr, width=240, height=32, text="Iniciar Sesión", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=fr, text="Remember me")
checkbox.pack(pady=12, padx=10)


if __name__ == "__main__":
    ventanaIniciarSesion.mainloop()