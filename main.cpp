#include <iostream>
#include <fstream>
#include <string>
#include <sstream> 
#include <vector>

using namespace std;

class Vehiculo{
	
	private:
		int idVehiculo;
		string placa;
		int ubicacion;
		
	public:
		Vehiculo (int id, const string& plc, int ubi) {
        	idVehiculo = id;
        	placa = plc;    
        	ubicacion = ubi;
    	}			
		int getIdVehiculo() const{
			return idVehiculo;
		}
		void setIdVehiculo(int newIdVehiculo){
			idVehiculo = newIdVehiculo;
		}
		int getUbicacion() const{
			return ubicacion;
		}
		void setUbicacion(int newUbicacion){
			ubicacion = newUbicacion;
		}
		string getPlaca() const {
        	return placa;
    	}
    	void setPlaca(const string& newPlaca) {
     	   placa = newPlaca;
    	}
};

class Ticket{
	
	private:
		int idTicket;
		string horaIngreso;
		string horaSalida;
		string fecha;
		vector<Vehiculo> vehiculos;
		float  monto;
		float horasTotales;
		
	public:
		Ticket(int id, const string& ingreso, const string& salida, const string& fch,const vector<Vehiculo>& v, float mnt, float horas) {
	        idTicket = id;
	        horaIngreso = ingreso;
	        horaSalida = salida;
	        vehiculos = v;
	        fecha = fch;
	        monto = mnt;
	        horasTotales = horas;
    	}
    	const vector<Vehiculo>& getVehiculos() const {
        	return vehiculos;
    	}
		int getIdTicket() const{
			return idTicket;
		}
		void setIdTicket(int newidTicket){
			idTicket = newidTicket;
		}
		float getMonto() const{
			return monto;
		}
		void setMonto(float newMonto){
			monto = newMonto;
		}
		float getHorasTotales() const{
			return horasTotales;
		}
		void setHorasTotales(float newHorasTotales){
			horasTotales = newHorasTotales;
		}
		string getHoraIngreso() const {
        	return horaIngreso;
    	}
    	void setHoraIngreso(const string& newHoraIngreso) {
     	   horaIngreso = newHoraIngreso;
    	}
		string getHoraSalida() const {
        	return horaSalida;
    	}
    	void setHoraSalida(const string& newHoraSalida) {
     	   horaSalida = newHoraSalida;
    	}
		string getFecha() const {
        	return fecha;
    	}
    	void setFecha(const string& newFecha) {
     	   fecha = newFecha;
    	}
		void agregarVehiculo(const Vehiculo& vehiculo) {
        vehiculos.push_back(vehiculo);
    	}
};

class Cliente {
	
	private:
		int idCliente;
		string nombre;
		vector<Vehiculo> vehiculos;
		vector<Ticket> tickets;
		int prioridad;
	
	public:
		Cliente(int id, const string& nmb, const vector <Vehiculo>& v, const vector<Ticket>& t, int prior) {
	        idCliente = id;
	        nombre = nmb;
	        vehiculos = v;
	        tickets = t;
	        prioridad = prior;
    	}
		int getIdCliente() const{
			return idCliente;
		}
		void setIdCliente(int newidCliente){
			idCliente = newidCliente;
		}
		string getNombre() const {
        	return nombre;
    	}
    	void setNombre(const string& newNombre) {
     	   nombre = newNombre;
    	}
		int getPrioridad() const{
			return prioridad;
		}
		void setPrioridad(int newPrioridad){
			prioridad = newPrioridad;
		}
		void agregarTicket(const Ticket& ticket) {
        	tickets.push_back(ticket);
    	}
   		void agregarVehiculo(const Vehiculo& vehiculo) {
       		vehiculos.push_back(vehiculo);
   		}
   		const vector<Vehiculo>& getVehiculos() const {
        	return vehiculos;
    	}
    	const vector<Ticket>& getTickets() const {
       		return tickets;
    	}
};

class Administrador {
private:
    string usuario;
    string contrasenia;
    int llaveMaestra;
    int idAdministrador;
public:
    Administrador(const string& usr, const string& pass, int llave, int id) {
        usuario = usr;
        contrasenia = pass;
        llaveMaestra = llave;
        idAdministrador = id;
    }
    string getUsuario() const {
        return usuario;
    }
    void setUsuario(const string& value) {
        usuario = value;
    }
    string getContrasenia() const {
        return contrasenia;
    }
    void setContrasenia(const string& value) {
        contrasenia = value;
    }
    int getLlaveMaestra() const {
        return llaveMaestra;
    }
    void setLlaveMaestra(int value) {
        llaveMaestra = value;
    }
    int getIdAdministrador() const {
        return idAdministrador;
    }
    void setIdAdministrador(int value) {
        idAdministrador = value;
    }
};

struct NodoCliente {
    Cliente cliente;
    NodoCliente* anterior;
    NodoCliente* siguiente;

    NodoCliente(const Cliente& c) : cliente(c), anterior(NULL), siguiente(NULL) {}
};

class Sistema {
	
	private:
	    string estado;
	    NodoCliente* primerCliente;
   		NodoCliente* ultimoCliente;
	    
	public:
		Sistema(const string& est){
			estado = est;
			primerCliente = NULL;
			ultimoCliente = NULL;
		}
		Sistema() {
	        estado = "Activo"; // Definir el estado inicial como "activo"
	    }
	    void definirSistema() {
	        cout << "Ingrese el estado del sistema: ";
	        getline(cin, estado);
	    }
	    void crearEstacionamiento() {
	    int matriz[100][100]; // Utilizar un tamaño máximo predefinido
	    int n;
		cout << "Ingrese el tamanio del estacionamiento: ";
	    cin >> n;
	    for (int i = 0; i < n; i++) {
	        for (int j = 0; j < n; j++) {
	            matriz[i][j] = 0;
	        }
	    }
	    // Guardar la matriz en un archivo de texto
	    ofstream archivo("estacionamiento.txt");
	    if (archivo.is_open()) {
	        for (int i = 0; i < n; i++) {
	            for (int j = 0; j < n; j++) {
	                archivo << matriz[i][j] << " ";
	            }
	            archivo << endl; // Agregar salto de línea después de cada fila
	        }
	        archivo.close();
	        cout << "Se ha creado el archivo estacionamiento.txt.\n";
	    } else {
	        cout << "No se pudo abrir el archivo para guardar el estacionamiento.\n";
	    }
	}
		void verEstacionamiento() {
			cout<<endl;
		    ifstream archivo("estacionamiento.txt");
		    if (archivo.is_open()) {
		        string linea;
		        const int MAX_SIZE = 100; // Tamaño máximo de la matriz
		        int matriz[MAX_SIZE][MAX_SIZE];
		        int filas = 0;
		
		        // Leer la matriz del archivo línea por línea
		        while (getline(archivo, linea) && filas < MAX_SIZE) {
		            istringstream iss(linea);
		            int valor;
		            int columnas = 0;
		
		            // Leer los valores separados por espacios en cada línea
		            while (iss >> valor && columnas < MAX_SIZE) {
		                matriz[filas][columnas] = valor;
		                columnas++;
		            }
		
		            filas++;
		        }
		
		        archivo.close();
		
		        // Imprimir la matriz con etiquetas de fila
		        for (int i = 0; i < filas; i++) {
		            cout << "f" << i << " ";
		            for (int j = 0; j < filas; j++) {
		                cout << matriz[i][j] << " ";
		            }
		            cout << endl;
		        }
		    } else {
		        cout << "No se pudo abrir el archivo estacionamiento.txt.\n";
		    }
		}
		int designarUbicacion() {
		    ifstream archivo("estacionamiento.txt");
		    if (archivo.is_open()) {
		        string linea;
		        const int MAX_SIZE = 100; // Tamaño máximo de la matriz
		        int matriz[MAX_SIZE][MAX_SIZE];
		        int filas = 0;
		        // Leer la matriz del archivo línea por línea
		        while (getline(archivo, linea) && filas < MAX_SIZE) {
		            istringstream iss(linea);
		            int valor;
		            int columnas = 0;
		            // Leer los valores separados por espacios en cada línea
		            while (iss >> valor && columnas < MAX_SIZE) {
		                matriz[filas][columnas] = valor;
		                columnas++;
		            }
		            filas++;
		        }
		        archivo.close();
		        // Buscar la primera posición con valor 0 y actualizar a 1
		        for (int i = 0; i < filas; i++) {
		            for (int j = 0; j < filas; j++) {
		                if (matriz[i][j] == 0) {
		                    matriz[i][j] = 1;
		                    // Guardar la matriz actualizada en el archivo
		                    ofstream archivoSalida("estacionamiento.txt");
		                    if (archivoSalida.is_open()) {
		                        for (int k = 0; k < filas; k++) {
		                            for (int l = 0; l < filas; l++) {
		                                archivoSalida << matriz[k][l] << " ";
		                            }
		                            archivoSalida << endl;
		                        }
		                        archivoSalida.close();
		                    } else {
		                        cout << "No se pudo abrir el archivo para guardar el estacionamiento actualizado.\n";
		                    }
		                    return i * filas + j; // Calcular y retornar la posición en el arreglo
		                }
		            }
		        }
		        cout << "No se encontro ninguna posicion disponible en el estacionamiento.\n";
		    } else {
		        cout << "No se pudo abrir el archivo estacionamiento.txt.\n";
		    }
			
		    return -1; 
		}
		void limpiarEstacionamiento() {
		    ifstream archivo("estacionamiento.txt");
		    if (archivo.is_open()) {
		        string linea;
		        const int MAX_SIZE = 100; // Tamaño máximo de la matriz
		        int matriz[MAX_SIZE][MAX_SIZE];
		        int filas = 0;
		
		        // Leer la matriz del archivo línea por línea
		        while (getline(archivo, linea) && filas < MAX_SIZE) {
		            istringstream iss(linea);
		            int valor;
		            int columnas = 0;
		
		            // Leer los valores separados por espacios en cada línea
		            while (iss >> valor && columnas < MAX_SIZE) {
		                matriz[filas][columnas] = valor;
		                columnas++;
		            }
		
		            filas++;
		        }
		
		        archivo.close();
		
		        // Llenar la matriz con ceros (0's)
		        for (int i = 0; i < filas; i++) {
		            for (int j = 0; j < filas; j++) {
		                matriz[i][j] = 0;
		            }
		        }
		
		        // Guardar la matriz actualizada en el archivo
		        ofstream archivoSalida("estacionamiento.txt");
		        if (archivoSalida.is_open()) {
		            for (int i = 0; i < filas; i++) {
		                for (int j = 0; j < filas; j++) {
		                    archivoSalida << matriz[i][j] << " ";
		                }
		                archivoSalida << endl;
		            }
		            archivoSalida.close();
		            cout << "Se ha limpiado el estacionamiento. Todos los espacios estan disponibles.\n";
		        } else {
		            cout << "No se pudo abrir el archivo para guardar el estacionamiento limpiado.\n";
		        }
		    } else {
		        cout << "No se pudo abrir el archivo estacionamiento.txt.\n";
		    }
		}
		void liberarUbicacion(int posicion) {
		    ifstream archivo("estacionamiento.txt");
		    if (archivo.is_open()) {
		        string linea;
		        const int MAX_SIZE = 100; // Tamaño máximo de la matriz
		        int matriz[MAX_SIZE][MAX_SIZE];
		        int filas = 0;
		
		        // Leer la matriz del archivo línea por línea
		        while (getline(archivo, linea) && filas < MAX_SIZE) {
		            istringstream iss(linea);
		            int valor;
		            int columnas = 0;
		
		            // Leer los valores separados por espacios en cada línea
		            while (iss >> valor && columnas < MAX_SIZE) {
		                matriz[filas][columnas] = valor;
		                columnas++;
		            }
		
		            filas++;
		        }
		
		        archivo.close();
		
		        // Obtener la posición en el arreglo a partir de la posición recibida
		        int fila = posicion / filas;
		        int columna = posicion % filas;
		
		        // Establecer la posición como 0 en el arreglo
		        matriz[fila][columna] = 0;
		
		        // Guardar la matriz actualizada en el archivo
		        ofstream archivoSalida("estacionamiento.txt");
		        if (archivoSalida.is_open()) {
		            for (int i = 0; i < filas; i++) {
		                for (int j = 0; j < filas; j++) {
		                    archivoSalida << matriz[i][j] << " ";
		                }
		                archivoSalida << endl;
		            }
		            archivoSalida.close();
		            cout << "Se ha liberado la posicion " << posicion << " en el estacionamiento.\n";
		        } else {
		            cout << "No se pudo abrir el archivo para guardar el estacionamiento actualizado.\n";
		        }
		    } else {
		        cout << "No se pudo abrir el archivo estacionamiento.txt.\n";
		    }
		}
		void crearArchivoAdministradores() {
		    ofstream archivo("administradores.txt");
		    if (archivo.is_open()) {
		        // Escribir los datos de los administradores en el archivo
		        archivo << "Usuario: Rose" << endl;
		        archivo << "Contraseña: rose1" << endl;
		        archivo << "LlaveMaestra: 1" << endl;
		        archivo << "ID: 1" << endl;
		        archivo << endl;
		        archivo << "Usuario: Jennie" << endl;
		        archivo << "Contraseña: jennie2" << endl;
		        archivo << "LlaveMaestra: 2" << endl;
		        archivo << "ID: 2" << endl;
		
		        archivo.close();
		        cout << "Se ha creado el archivo administradores.txt.\n";
		    } else {
		        cout << "No se pudo crear el archivo administradores.txt.\n";
		    }
		} 
		bool buscarAdministrador(const Administrador& admin) {
	    ifstream archivo("administradores.txt");
	    if (archivo.is_open()) {
	        string linea;
	        while (getline(archivo, linea)) {
	            size_t separador = linea.find(":");
	            if (separador != string::npos) {
	                string clave = linea.substr(0, separador);
	                string valor = linea.substr(separador + 2); // +2 para omitir ": "
	
	                if (clave == "Usuario" && valor == admin.getUsuario()) {
	                    // Leer los atributos restantes del administrador
	                    getline(archivo, linea); // Obtener la línea de Contraseña
	                    separador = linea.find(":");
	                    if (separador != string::npos) {
	                        clave = linea.substr(0, separador);
	                        valor = linea.substr(separador + 2); // +2 para omitir ": "
	                        string contrasenia = valor;
	
	                        getline(archivo, linea); // Obtener la línea de LlaveMaestra
	                        separador = linea.find(":");
	                        if (separador != string::npos) {
	                            clave = linea.substr(0, separador);
	                            valor = linea.substr(separador + 2); // +2 para omitir ": "
	                            int llaveMaestra = 0;
	                            stringstream ss(valor);
	                            ss >> llaveMaestra;
	
	                            if (admin.getContrasenia() == contrasenia && admin.getLlaveMaestra() == llaveMaestra) {
	                                archivo.close();
	                                return true;
	                            }
	                        }
	                    }
	                }
	            }
	        }
	
	        archivo.close();
	    } else {
	        cout << "No se pudo abrir el archivo administradores.txt.\n";
	    }	
	    return false;
	}
		void registrarCliente(const Cliente& cliente) {
	        // Crear un nuevo nodo con el cliente
	        NodoCliente* nuevoNodo = new NodoCliente(cliente);
	
	        // Verificar si la lista está vacía
	        if (primerCliente == NULL) {
	            primerCliente = nuevoNodo;
	            ultimoCliente = nuevoNodo;
	        } else {
	            // Agregar el nuevo nodo al final de la lista
	            nuevoNodo->anterior = ultimoCliente;
	            ultimoCliente->siguiente = nuevoNodo;
	            ultimoCliente = nuevoNodo;
	        }
	
	        // Abrir el archivo en modo "append" para añadir el nuevo cliente
	        ofstream archivo("clientes.txt", ios::app);
	        if (archivo.is_open()) {
	            // Guardar los datos del cliente en el archivo
	            archivo << "Id de cliente: " << cliente.getIdCliente() << endl;
	            archivo << "Nombre: " << cliente.getNombre() << endl;
	
	            // Guardar los vehículos del cliente
	            const vector<Vehiculo>& vehiculos = cliente.getVehiculos();
	            archivo << "Vehiculos: " << endl;
	            for (size_t i = 0; i < vehiculos.size(); i++) {
	                archivo << "Id de vehiculo: " << vehiculos[i].getIdVehiculo() << endl;
	                archivo << "Placa: " << vehiculos[i].getPlaca() << endl;
	                archivo << "Ubicacion: " << vehiculos[i].getUbicacion() << endl;
	            }
	
	            // Guardar los tickets del cliente
	            const vector<Ticket>& tickets = cliente.getTickets();
	            archivo << "Tickets: " << endl;
	            for (size_t i = 0; i < tickets.size(); i++) {
	                archivo << "Id de ticket: " << tickets[i].getIdTicket() << endl;
	                archivo << "Hora de ingreso: " << tickets[i].getHoraIngreso() << endl;
	                archivo << "Hora de salida: " << tickets[i].getHoraSalida() << endl;
	                archivo << "Fecha: " << tickets[i].getFecha() << endl;
	                archivo << "Vehiculos del ticket: " << endl;
	                const vector<Vehiculo>& vehiculosTicket = tickets[i].getVehiculos();
	                for (size_t j = 0; j < vehiculosTicket.size(); j++) {
	                    archivo << "Id de vehiculo: " << vehiculosTicket[j].getIdVehiculo() << endl;
	                    archivo << "Placa: " << vehiculosTicket[j].getPlaca() << endl;
	                    archivo << "Ubicacion: " << vehiculosTicket[j].getUbicacion() << endl;
	                }
	                archivo << "Monto: " << tickets[i].getMonto() << endl;
	                archivo << "Horas totales: " << tickets[i].getHorasTotales() << endl;
	            }
	
	            archivo.close();
	            cout << "El cliente se ha registrado y se ha guardado en el archivo clientes.txt.\n";
	        } else {
	            cout << "No se pudo abrir el archivo para guardar el cliente.\n";
	        }
	    }
	    void verClientesRegistrados() {
		    // Abrir el archivo en modo lectura
		    ifstream archivo("clientes.txt");
		    if (archivo.is_open()) {
		        string linea;
		
		        // Leer el archivo línea por línea
		        while (getline(archivo, linea)) {
		            // Mostrar la línea por la salida estándar
		            cout << linea << endl;
		        }
		
		        archivo.close();
		    } else {
		        cout << "No se pudo abrir el archivo clientes.txt.\n";
		    }
		}
};

int main() {
	Sistema sistema;
	Administrador admin1("Rose","rose1",1,1);
    bool encontrado = sistema.buscarAdministrador(admin1);
    if (encontrado) {
        cout << "Bienvenido al ESTACIONAMIENTO MONO!"<<endl;
        
		vector<Vehiculo> vehiculos;
    	vehiculos.push_back(Vehiculo(1, "ABC123", 1));
    	vehiculos.push_back(Vehiculo(2, "DEF456", 2));
        
		vector<Ticket> tickets;
    	tickets.push_back(Ticket(1, "09:00", "18:00", "2023-06-01", vehiculos, 20.5, 9.0));
    	
    	Cliente cliente(1, "Juan", vehiculos, tickets, 1);
    	
    	//agregar mas vehiculos o tickets//
    	cliente.agregarVehiculo(Vehiculo(3, "GHI789", 3));
    	cliente.agregarTicket(Ticket(2, "10:00", "15:00", "2023-06-02", vehiculos, 15.0, 5.0));
    	
    	sistema.registrarCliente(cliente);
    	system("PAUSE");
    	
    	sistema.verClientesRegistrados();
    	
    	
    } else {
        cout << "Credenciales incorrectas.\n";
    }
    return 0;
}


