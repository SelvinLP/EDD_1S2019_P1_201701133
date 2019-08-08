from idlelib.idle_test.test_config_key import ValidationTest
import os

class Bloque():
    #Definiendo el constructor
    def __init__(self,valorx,valory):
        self.Posicion_X = valorx
        self.Posicion_Y = valory
        self.siguiente=None


class Pila_Bocadillo:
    ContarDocumentos=0
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacio(self):
        return self.primero is None

    def Tamaño(self):
        return self.size

    def Insertar(self, Valorx,Valory):
        nuevaLista = Bloque(Valorx, Valory)
        if self.vacio():
            self.primero = self.ultimo = nuevaLista
        else:
            aux = self.ultimo
            self.ultimo = nuevaLista
            aux.siguiente = nuevaLista
        self.size += 1

    def Iniciar_Nuevo(self):
        self.primero=None
        self.ultimo=None
        self.size=0

    def Eliminar(self):
        aux=self.primero
        if(self.primero is None):
            print("No se puede eliminar no se encuentra nada en la pila")
        else:
            if(self.size==1):
                self.primero=None
            else:
                while (aux is not None):
                    tem = aux.siguiente
                    tem = tem.siguiente
                    if (tem is None):
                        print("Se Elimino ", aux.siguiente.Posicion_X, "  ", aux.siguiente.Posicion_Y)
                        aux.siguiente = None
                        self.ultimo = aux
                    aux = aux.siguiente
            self.size-=1
    def Imprimir(self):
        aux = self.primero
        cont = 0
        while aux is not None:
            print("No.", cont, "Posicion", aux.Posicion_X, "  ", aux.Posicion_Y)
            aux = aux.siguiente
            cont += 1
    def Graficar(self):
        CadenaImprimir="digraph Pila { "+'\n'
        CadenaImprimir=CadenaImprimir+' size="9,9"'+'\n'
        CadenaImprimir=CadenaImprimir+'node[shape=record,style=filled] '+'\n'
        CadenaImprimir=CadenaImprimir+'    1[label ='+'"'+'{'
        aux = self.primero
        CadenaImprimir=CadenaImprimir+' '
        while aux is not None:
            CadenaImprimir = CadenaImprimir + " "+ '|' + '(' +str(aux.Posicion_X) +","+str(aux.Posicion_Y)+ ')'
            aux = aux.siguiente

        CadenaImprimir=CadenaImprimir+' }"]'+'\n'
        CadenaImprimir = CadenaImprimir+" }"
        file = open("EDD_201701133_Pila"+str(Pila_Bocadillo.ContarDocumentos)+".dot", "w")
        file.write(CadenaImprimir)
        file.close()
        os.system('dot -Tpng EDD_201701133_Pila'+str(Pila_Bocadillo.ContarDocumentos)+'.dot -o  EDD_Pila'+str(Pila_Bocadillo.ContarDocumentos)+'.png')
        os.system('Start EDD_Pila'+str(Pila_Bocadillo.ContarDocumentos)+'.png')
        Pila_Bocadillo.ContarDocumentos +=1


