from Viajero_Frecuente import ViajeroFrecuente
import csv

class lista:
    __lista=[]
    def __init__(self):
        self.__lista = []

    def test(self):
        archivo=open("viajeros.csv")
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            num_viajero = int(fila[0])
            dni = fila[1]
            nombre = fila[2]
            apellido = fila[3]
            millas_acum = int(fila[4])
            viajero = ViajeroFrecuente(num_viajero, dni, nombre, apellido, millas_acum)
            self.__lista.append(viajero)
        archivo.close()

    def numViajero(self):
        numero=int(input("Ingresar un numero de viajero frecuente: "))
        viaj=False
        for objeto in self.__lista:
            if  objeto.getNumero() == numero:
                viaj= objeto
        return viaj
    
    def almacenMemoria(self):
        print("Representacion del almacenamiento en memoria para la lista cargada con 4 viajeros.")
        for i in range(4):
            viajero= self.__lista[i]
            print(f"Numero: {viajero.getNumero()}\nNombre y Apellido: {viajero.getApellido()} {viajero.getNombre()}\nDNI: {viajero.getDNI()}\nMillas: {viajero.getMillas()}\n")
    
