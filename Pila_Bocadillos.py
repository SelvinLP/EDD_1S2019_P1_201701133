class Bloque():
    #Definiendo el constructor
    def __init__(self):
        self.Posicion_X = ""
        self.Posicion_Y = ""

    def Dar_Valor(self, Valores):
        if len(Valores)==2:
            self.Posicion_X    	=Valores[0]
            self.Posicion_Y  	=Valores[1]

class Pila_Bocadillo:
    def __init__(self):
        self.Bocadillos_xy=[]

    def Vacio(self):
        return self.Bocadillos_xy==[]

    def Insertar(self, valor):
        self.items.append(valor)

    def Eliminar(self):
        #usare un try por si no queda nada en la pila
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila se encuentra vacia")

    def Obtener_Tamaño(self):
        return len(self.Bocadillos_xy)

    def Mostrar_Pila(self):
        return self.Bocadillos_xy[len(self.Bocadillos_xy) - 1]


