import csv
import curses
import subprocess
import os
from ListaDoleCircular_Usuarios import  ListaDoblementeEnlazada_U
from ListaDoble_Serpiente import ListaDoblementeEnlazada_S



ListaSerpienet=ListaDoblementeEnlazada_S()
ListaUsuarios=ListaDoblementeEnlazada_U()
#variables del menu
OpcionReportes=0
opcion =0
while(opcion!=6):
    print("-------------------- Main -------------------")
    print("|1. Play                                    |");
    print("|2. Scoreboard                              |");
    print("|3. Seleccion de Usuario                    |");
    print("|4. Reportes                                |");
    print("|5. Bulk Loading                            |");
    print("|6.Salir                                    |");
    print("---------------------------------------------")
    opcion = int(input("Ingrese una Opcion"))
    if(opcion==4):
        while(opcion!=5):
            print("----------------- Opcion Reportes -----------")
            print("|1. Snake Report                            |");
            print("|2. Score Report                            |");
            print("|3. Scoreboard Report                       |");
            print("|4. Users Report                            |");
            print("|5.Salir                                    |");
            OpcionReportes = int(input("Ingrese una Opcion"))
            #opciones del menu reportes
            if(OpcionReportes==4):
                ListaUsuarios.Graficar()
    if(opcion==5):
        nombre=input("Ingrese Nombre del archivo")
        f=open(nombre)
        with open(nombre, newline='') as File:
            reader = csv.reader(File)
            for linea in reader:
                #ListaUsuarios.Insertar_Final(linea)
                ListaUsuarios.Insertar_Final(f.readline())
        ListaUsuarios.Eliminar()
        ListaUsuarios.Imprimir()
        ListaUsuarios.Graficar()


