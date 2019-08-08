import subprocess
import os
class Nodo():
    def __init__(self,valorx,valory):
        self.anterior = None
        self.siguiente = None
        self.PosicionX=valorx
        self.Posiciony=valory

class ListaDoblementeEnlazada_S():
    ContadorDocumentos = 0
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

#comprobacion si la lista esta vacia
    def vacio(self):
        return self.primero is None

    def Tamaño(self):
        return self.size

    def Insertar_Final(self, valor_x,valor_y):
        nuevaLista = Nodo(valor_x,valor_y)
        if self.vacio():
            self.primero =self.ultimo = nuevaLista
        else:
            aux = self.ultimo
            self.ultimo = nuevaLista
            aux.siguiente = nuevaLista
            self.ultimo.anterior=aux
            self.size += 1

    def Eliminar(self):
        aux=self.ultimo.anterior
        self.ultimo.anterior = None
        self.ultimo=aux
        self.ultimo.siguiente=None
        self.size-=1

    def Imprimir(self):
        aux = self.primero
        cont = 0
        while aux is not None:
            print("No.", cont, "Posicion", aux.PosicionX, "  ", aux.Posiciony)
            aux = aux.siguiente
            cont += 1

    1
    def ActualizarPos_A(self,valorx,valory):
        #Inserta al Inicio
        nuevaLista = Nodo(valorx,valory)
        aux = self.primero
        self.primero = nuevaLista
        self.primero.siguiente = aux
        aux.anterior = self.primero

        aux = self.ultimo.anterior
        self.ultimo.anterior = None
        self.ultimo = aux
        self.ultimo.siguiente = None


    def Empezar_Nuevo(self):
        self.primero=None
        self.ultimo=None
        self.size=0

    def Reversa(self):
        cont=0
        nuevaLista = Nodo(self.primero.PosicionX, self.primero.Posiciony)
        aux = self.ultimo
        self.ultimo = nuevaLista
        aux.siguiente = nuevaLista
        self.ultimo.anterior = aux

        aux2 = self.primero.siguiente
        self.primero.siguiente = None
        aux2.anterior = None
        self.primero = aux2
        while cont<self.size:
            nuevaLista = Nodo(self.primero.PosicionX, self.primero.Posiciony)
            aux = self.ultimo.anterior
            


            aux2 = self.primero.siguiente
            self.primero.siguiente=None
            aux2.anterior = None
            self.primero=aux2

            cont +=1







    def Obtener_Pos_x(self,posicion):
        aux = self.primero
        contador=0
        while aux is not None:
            if contador == posicion:
                return (aux.PosicionX)
            aux = aux.siguiente
            contador +=1

    def Obtener_Pos_y(self,posicion):
        aux = self.primero
        contador=0
        while aux is not None:
            if contador == posicion:
                return (aux.Posiciony)
            aux = aux.siguiente
            contador +=1

    def Graficar(self):
        CadenaImprimir="digraph List { rankdir=LR "+'\n'
        CadenaImprimir=CadenaImprimir+' size="9,9"'+'\n'
        CadenaImprimir = CadenaImprimir + 'node[shape=record,style=filled] ' + '\n'
        CadenaImprimir=CadenaImprimir+'"NULL"'+" [shape=box] "+ '\n'
        CadenaImprimir = CadenaImprimir + '"NULL."' + " [shape=box] "+ '\n'
        aux = self.primero
        CadenaSig=''
        CadenaAnt=''
        #ciclo para los enlaces siguientes

        while aux is not None:
            CadenaImprimir = CadenaImprimir + " " + '"(' +str(aux.PosicionX) +","+str(aux.Posiciony)+ ')"' +'[label ='+'"'+'{'
            CadenaImprimir= CadenaImprimir+'|'+ '(' +str(aux.PosicionX) +","+str(aux.Posiciony)+ ')' +'|'+'}"]'+ '\n'
            if aux.siguiente is None:
                CadenaSig=CadenaSig+" "+ '"(' +str(aux.PosicionX) +","+str(aux.Posiciony)+ ')"'
            else:
                CadenaSig=CadenaSig+" "+ '"(' +str(aux.PosicionX) +","+str(aux.Posiciony)+ ')"' +" -> "

            aux = aux.siguiente
        #ciclo para los enlaces anteriores
        aux = self.ultimo
        while aux is not None:
            if aux.anterior is None:
                CadenaAnt=CadenaAnt+" "+ '"(' +str(aux.PosicionX) +","+str(aux.Posiciony)+ ')"'
            else:
                CadenaAnt=CadenaAnt+" "+ '"(' +str(aux.PosicionX) +","+str(aux.Posiciony)+ ')"' +" -> "

            aux = aux.anterior
        CadenaSig=CadenaSig+' -> '+'"NULL"'
        CadenaAnt=CadenaAnt+' -> '+'"NULL."'
        CadenaImprimir = CadenaImprimir+" "+CadenaSig+'\n'+CadenaAnt+"}"
        file = open("EDD_201701133_Ser"+str(ListaDoblementeEnlazada_S.ContadorDocumentos)+".dot", "w")
        file.write(CadenaImprimir)
        file.close()
        os.system('dot -Tpng EDD_201701133_Ser'+str(ListaDoblementeEnlazada_S.ContadorDocumentos)+'.dot -o  EDD_Ser'+str(ListaDoblementeEnlazada_S.ContadorDocumentos)+'.png')
        os.system('Start EDD_Ser'+str(ListaDoblementeEnlazada_S.ContadorDocumentos)+'.png')
        ListaDoblementeEnlazada_S.ContadorDocumentos +=1

