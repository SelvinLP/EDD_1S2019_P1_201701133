
import os
class Nodo():
    def __init__(self,Descripcion):
        self.anterior = None
        self.siguiente = None
        self.NombreUsu = Descripcion

class ListaDoblementeEnlazada_U():
    ContadorDocumentos = 0
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

#comprobacion si la lista esta vacia
    def vacio(self):
        return self.primero is None

    def Insertar_Final(self, valor2):
        nuevaLista = Nodo(valor2)
        if self.vacio():
            self.primero = self.ultimo = nuevaLista
        else:
            aux = self.ultimo
            self.ultimo = nuevaLista
            aux.siguiente = nuevaLista
            self.ultimo.anterior = aux
            self.ultimo.siguiente=self.primero
            self.primero.anterior=self.ultimo
            self.size += 1

    def Imprimir(self):
        aux = self.primero
        cont=0
        print("No.", cont, "Descripcion", aux.NombreUsu)
        aux=aux.siguiente
        cont += 1
        while aux is not self.primero:
            print("No.",cont,"Descripcion" , aux.NombreUsu)
            aux = aux.siguiente
            cont +=1

    def Eliminar(self):
        aux = self.primero
        aux=aux.siguiente
        aux.anterior=self.ultimo
        self.ultimo.siguiente=aux
        self.primero=aux
        self.size-=1

    def Graficar(self):
        CadenaImprimir = "digraph List { rankdir=LR "
        aux = self.primero
        CadenaSig = ''
        CadenaAnt = ''
        CadenaImprimir = CadenaImprimir + " " +'"'+ str(aux.NombreUsu) +'"'+  " [shape=box] "
        CadenaSig = CadenaSig + " " +'"'+  str(aux.NombreUsu)+'"'
        aux=aux.siguiente
        while aux is not self.primero:
            CadenaImprimir = CadenaImprimir + " " +'"'+  str(aux.NombreUsu) +'"'+  " [shape=box] "
            CadenaSig = CadenaSig +" -> " +'"'+  str(aux.NombreUsu)+'"'+ " "
            aux = aux.siguiente
        CadenaSig=CadenaSig +" -> " +'"'+  str(self.primero.NombreUsu)+'"'+ " "

        #Ciclo para la otra relacion
        aux=self.ultimo
        CadenaAnt=CadenaAnt+ " " +'"'+  str(aux.NombreUsu)+'"'
        aux=aux.anterior
        while aux is not self.ultimo:
            CadenaAnt = CadenaAnt + " -> " +'"'+  str(aux.NombreUsu) +'"'+  " "
            aux=aux.anterior
        CadenaAnt=CadenaAnt+" -> " +'"'+  str(self.ultimo.NombreUsu)+'"'+ " "

        #generacion de documentos
        CadenaImprimir=CadenaImprimir+" "+CadenaSig+'\n'+CadenaAnt+" }"
        file = open("EDD_201701133_Usu" + str(ListaDoblementeEnlazada_U.ContadorDocumentos) + ".dot", "w")
        file.write(CadenaImprimir)
        file.close()
        os.system('dot -Tpng EDD_201701133_Usu' + str(
        ListaDoblementeEnlazada_U.ContadorDocumentos) + '.dot -o  EDD_Usu' + str(
        ListaDoblementeEnlazada_U.ContadorDocumentos) + '.png')
        os.system('Start EDD_Usu' + str(ListaDoblementeEnlazada_U.ContadorDocumentos) + '.png')
        ListaDoblementeEnlazada_U.ContadorDocumentos += 1


        print(CadenaImprimir)
