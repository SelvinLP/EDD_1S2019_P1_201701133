import os

class Bloque():
    #Definiendo el constructor
    def __init__(self,Usu,punto):
        self.NombreUsu = Usu
        self.Puntuacion = punto
        self.siguiente=None


class Fila_Puntuacion:
    ContarDocumentos=0
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacio(self):
        return self.primero is None

    def Tamaño(self):
        return self.size

    def Insertar(self, Usua,Punt):
        nuevaLista = Bloque(Usua, Punt)
        aux2=self.primero
        if self.vacio():
            self.primero = self.ultimo = nuevaLista
        else:
            aux = self.ultimo
            self.ultimo = nuevaLista
            aux.siguiente = nuevaLista
            if(self.size==10):

                aux2 = aux2.siguiente
                self.primero = aux2
                self.size-=1
        self.size += 1

    def Imprimir(self,vent):
        aux = self.primero
        cont = 6
        while aux is not None:
            vent.addstr(cont, 25, aux.NombreUsu)
            vent.addstr(cont, 40, str(aux.Puntuacion))

            aux = aux.siguiente
            cont += 1

    def Eliminar(self):
        aux = self.primero
        if (self.primero is None):
            print("No se puede eliminar no se encuentra nada en la Fila")
        else:
            if (self.size == 1):
                self.primero = None
            else:
                aux=aux.siguiente
                self.primero=aux
            self.size -= 1

    def Graficar(self):
        aux = self.primero
        CadenaSig = ''
        CadenaAnt = ''
        CadenaImprimir = "digraph List { rankdir=LR " + '\n'
        CadenaImprimir = CadenaImprimir + ' size="9,9"' + '\n'
        CadenaImprimir = CadenaImprimir + 'node[shape=record,style=filled] ' + '\n'
        CadenaImprimir = CadenaImprimir + '"NULL"' + " [shape=box] " + '\n'

        while aux is not None:
            CadenaImprimir = CadenaImprimir + " " + '"(' +str(aux.NombreUsu) +","+str(aux.Puntuacion)+ ')"' +'[label ='+'"'+'{'
            CadenaImprimir= CadenaImprimir+ '(' +str(aux.NombreUsu) +","+str(aux.Puntuacion)+ ')' +'|'+'}"]'+ '\n'
            if aux.siguiente is None:
                CadenaSig=CadenaSig+" "+ '"(' +str(aux.NombreUsu) +","+str(aux.Puntuacion)+ ')"'
            else:
                CadenaSig=CadenaSig+" "+ '"(' +str(aux.NombreUsu) +","+str(aux.Puntuacion)+ ')"' +" -> "

            aux = aux.siguiente

        CadenaSig = CadenaSig + ' -> ' + '"NULL"'
        CadenaImprimir = CadenaImprimir + " " + CadenaSig + "}"
        file = open("EDD_201701133_Punt" + str(Fila_Puntuacion.ContarDocumentos) + ".dot", "w")
        file.write(CadenaImprimir)
        file.close()
        os.system('dot -Tpng EDD_201701133_Punt' + str(Fila_Puntuacion.ContarDocumentos) + '.dot -o  EDD_Punt' + str(Fila_Puntuacion.ContarDocumentos) + '.png')
        os.system('Start EDD_Punt' + str(Fila_Puntuacion.ContarDocumentos) + '.png')
        Fila_Puntuacion.ContarDocumentos +=1