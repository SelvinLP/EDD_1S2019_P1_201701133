import subprocess
import os
class Nodo():
    def __init__(self,valorx,valory):
        self.anterior = None
        self.siguiente = None
        self.PosicionX=valorx
        self.Posiciony=valory

class ListaDoblementeEnlazada_S():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

#comprobacion si la lista esta vacia
    def vacio(self):
        return self.primero is None

