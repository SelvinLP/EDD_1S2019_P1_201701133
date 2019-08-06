#Librerias
import csv
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library
import subprocess
import os
#Instancias de Clases
from ListaDoleCircular_Usuarios import  ListaDoblementeEnlazada_U
from ListaDoble_Serpiente import ListaDoblementeEnlazada_S
ListaSerpienet=ListaDoblementeEnlazada_S()
ListaUsuarios=ListaDoblementeEnlazada_U()

#variables del menu
OpcionReportes=0
UsuarioSeleccionado=""
opcion =0
#Metodos de Curses

stdscr = curses.initscr()
window = curses.newwin(20,70,0,0)
window.keypad(True)
curses.noecho()
curses.curs_set(0)
window.nodelay(True)
#Movimiento del curses
Movimiento=KEY_RIGHT
Pos_x=5
Pos_y=5


def Espera_Salir(Vent):
    key = Vent.getch()
    while key!=8:#posicion para retroceder DELETE
        key = Vent.getch()

def Pintado_Menu(Vent):
    Pintado_Titulo(Vent,' MENU PRINCIPAL ')
    Vent.addstr(7,21, '1. PLAY')#49
    Vent.addstr(8,21, '2. SCOREBOARD')#50
    Vent.addstr(9,21, '3. USER SELECTION')#51
    Vent.addstr(10,21, '4. REPORTS')#52
    Vent.addstr(11,21, '5. BULK LOADING')#53
    Vent.addstr(12,21, '6. EXIT')#54
    Vent.timeout(-1)

def Pintado_Titulo(Vent,cadena):
    Vent.clear()
    Vent.border(0)
    posicion_x = round((60-len(cadena))/2)
    Vent.addstr(0,posicion_x,cadena)

#Muestra Pantalla
Pintado_Menu(window)

#Ciclo de Opciones
while opcion==0:
    opcion= window.getch()
    if(opcion==49):#opcion 1
        Pintado_Titulo(window," PLAY ")
        if(UsuarioSeleccionado==""):
            window.addstr(5, 21, "INGRESE UN USUARIO")
            NombreU = window.getstr(0, 0, 20)
            window.addstr(5,21,"Usuario Creado: ")
            window.addstr(5, 38, NombreU)
            ListaUsuarios.Insertar_Final(NombreU)
            espacio=window.getch()#para que exita un salto de linea en el programa
            Pintado_Titulo(window, " PLAY ")
        #Fin Creacion de Usuario

        #Creacion del tablero

        window.addch(Pos_y, Pos_x, '*') #Posicion Inicial
        #Ciclo Principal
        while(Movimiento!=8):
            window.timeout(100)
            NuevoMovimiento=window.getch()
            if(NuevoMovimiento is not -1):
                Movimiento=NuevoMovimiento

            window.addch(Pos_y, Pos_x, ' ')  # Es el que borra
            # Movimientos
            if Movimiento == KEY_RIGHT:
                Pos_x = Pos_x + 1
            elif Movimiento == KEY_LEFT:  # left direction
                Pos_x = Pos_x - 1  # pos_x decrease
            elif Movimiento == KEY_UP:  # up direction
                Pos_y = Pos_y - 1  # pos_y decrease
            elif Movimiento == KEY_DOWN:  # down direction
                Pos_y = Pos_y + 1
            window.addch(Pos_y, Pos_x, '*')

                    #Fin de Inicio de Juego
        Espera_Salir(window)
        Pintado_Menu(window)
        opcion=0



    elif(opcion==50):#opcion 2
        Pintado_Titulo(window, " SCOREBOARD ")
        Espera_Salir(window)
        Pintado_Menu(window)
        opcion = 0




    elif (opcion == 51):  # opcion 3
        #Pintado_Titulo(window, " USER SELECTION ")
        Aceptacion_Usu=0
        Fin_Ciclo=0
        while(Fin_Ciclo==0):
            Pintado_Titulo(window, " USER SELECTION ")
            window.addstr(5, 21, ListaUsuarios.Buscar(Aceptacion_Usu))
            window.addstr(5, 17, '->')
            window.addstr(5, 45, '<-')
            window.addstr(7, 19, '¿DESEA SELECCIONAR?')
            window.addstr(8, 19, '1.  SI')
            window.addstr(9, 19, 'Presione DELETE para salir')
            Pos = window.getch()
            if (Pos==KEY_RIGHT):
                Aceptacion_Usu +=1
            elif(Pos==KEY_LEFT):
                Aceptacion_Usu -=1
            elif(Pos == 49):
                UsuarioSeleccionado = ListaUsuarios.Buscar(Aceptacion_Usu)
                Fin_Ciclo=1
                print("Usuario Seleccionado: ",UsuarioSeleccionado)
            elif(Pos==8):
                Fin_Ciclo=1

        #Fin de seleccion de Usuario
        Pintado_Menu(window)
        opcion = 0





    elif (opcion == 52):  # opcion 4
        Pintado_Titulo(window, " REPORTS ")
        window.addstr(7, 21, '1. SNAKE REPORT')
        window.addstr(8, 21, '2. SCORE REPORT')
        window.addstr(9, 21, '3. SCOREBOARD REPORT')
        window.addstr(10, 21, '4. USERS REPORT')

        OpcionReportes=window.getch()
        if(opcion==49):
            print()
        elif(opcion==50):
            print()
        elif(opcion==51):
            print("")
        elif(opcion==52):
            ListaUsuarios.Graficar()
        else:
            window.addstr(11, 21, 'Opcion Incorrecta')
        window.addstr(12, 21, 'Presione DELETE para salir')


        #Fin opcion 4
        Espera_Salir(window)
        Pintado_Menu(window)
        opcion = 0





    elif (opcion == 53):  # opcion 5

        nombrecorrecto=50
        while(nombrecorrecto==50):
            Pintado_Titulo(window, " BULK LOADING ")
            window.addstr(7, 19, 'INGRESE EL NOMBRE DEL ARCHIVO')
            nombre = window.getstr(0, 0, 40)
            window.addstr(8, 23, nombre)
            window.addstr(9, 19, '¿EL NOMBRE ES CORRECTO?')
            window.addstr(10, 19, '1.  SI')
            window.addstr(11, 19, '2.  NO')
            nombrecorrecto=window.getch()
            if (nombrecorrecto==49 ):
                f = open(nombre)
                with open(nombre, newline='') as File:
                    reader = csv.reader(File)
                    for linea in reader:
                        # ListaUsuarios.Insertar_Final(linea)
                        ListaUsuarios.Insertar_Final(f.readline())
                ListaUsuarios.Eliminar()
                ListaUsuarios.Imprimir()
            elif(nombrecorrecto==50):
                nombrecorrecto=50
        window.addstr(12, 21, 'Presione DELETE para salir')


        #fin de abrir archivo5
        Espera_Salir(window)
        Pintado_Menu(window)
        opcion = 0




    elif (opcion == 54):  # opcion 6
        #salir
        opcion=100
    else:
        opcion=0



curses.endwin() #Cierra ventanas
