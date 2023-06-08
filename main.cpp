#include <iostream>
#include <fstream>
#include <string>
#include <sstream> 

using namespace std;

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

class Sistema {
private:
    string estado;
public:
	Sistema(const string& est){
		estado = est;
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
};

int main() {
	Sistema sistema;
	Administrador admin1("Rose","rose1",1,1);
    bool encontrado = sistema.buscarAdministrador(admin1);
    if (encontrado) {
        cout << "Bienvenido al ESTACIONAMIENTO MONO!"<<endl;
        
    } else {
        cout << "Credenciales incorrectas.\n";
    }
    return 0;
}


