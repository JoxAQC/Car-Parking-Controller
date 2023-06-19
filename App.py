import customtkinter
import os
from PIL import Image
from Sistema import Sistema

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("SpotGuard")
        self.geometry("700x450")

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

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

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

        # create fourth frame
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

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
        placa = "abc"
        if self.placa_entry.get() == placa:
            print("Hola uwu")
        else:
            self.placa_entry.configure(state="disabled")
            self.buscar_button.configure(state="disabled")
            self.name_entry.configure(state="normal")
            self.buscarCliente_button.configure(state="normal")

    def buscarPorNombre(self):
        nombre = "abc"
        if self.name_entry.get() == nombre:
            print("Hola uwu ", nombre)
        else:
            self.name_entry.configure(state="disabled")
            self.buscarCliente_button.configure(state="disabled")
            self.contact_entry.configure(state="normal")
            self.type_entry.configure(state="normal")
            self.registrar_button.configure(state="normal")

    def registrarNuevo(self):
        print("Hola nuevo :D")

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