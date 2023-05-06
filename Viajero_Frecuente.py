class ViajeroFrecuente:
    __num_viajero= int
    __dni= ""
    __nombre=""
    __apellido=""
    __millas_acum=int
    
    def __init__(self, num, dni,nombre, apellido, millas):
        self.__num_viajero= num
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum = millas

    def getMillas(self):
        return self.__millas_acum

    def acumularMillas(self, millas_reco):
        self.__millas_acum+=millas_reco
        return self.__millas_acum

    def canjearMillas(self, millas_canjear):
        if millas_canjear <= self.__millas_acum:
            self.__millas_acum-=millas_canjear
            return self.__millas_acum
    
    def getNumero(self):
        return self.__num_viajero
    
    def getNombre(self):
        return self.__nombre
    
    def getDNI(self):
        return self.__dni
    
    def getApellido(self):
        return self.__apellido