#Librerias
import csv
import random
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library
import subprocess
import os
#Instancias de Clases
from ListaDoleCircular_Usuarios import  ListaDoblementeEnlazada_U
from ListaDoble_Serpiente import ListaDoblementeEnlazada_S
from Pila_Bocadillos import  Pila_Bocadillo
from Pila_Bocadillos import  Bloque
Pila_Bocad=Pila_Bocadillo()
ListaSerpienet=ListaDoblementeEnlazada_S()
ListaUsuarios=ListaDoblementeEnlazada_U()

#variables del menu
OpcionReportes=0
UsuarioSeleccionado=""
opcion =0
#Variables de la serpiente
TamanioSer=3
ExisteBocadillo=0
#Metodos de Curses
stdscr = curses.initscr()
TamañoTablero_y=20
TamañoTablero_x=70
window = curses.newwin(TamañoTablero_y,TamañoTablero_x,0,0)
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

#instancia de valores iniciales del juego
Pos_x = 5
Pos_y = 5
ListaSerpienet.Insertar_Final(Pos_x, Pos_y)
ListaSerpienet.Insertar_Final(Pos_x - 1, Pos_y)
ListaSerpienet.Insertar_Final(Pos_x - 2, Pos_y)


#Ciclo de Opciones
while opcion==0:
    opcion= window.getch()
    #posicion inicial de la serpiente
    Pos_x = 5
    Pos_y = 5
    if(opcion==49):#opcion 1
        Movimiento = KEY_RIGHT
        Pintado_Titulo(window," PLAY ")
        if(UsuarioSeleccionado==""):
            window.addstr(5, 21, "INGRESE UN USUARIO")
            NombreU = window.getstr(1, 0, 20)
            window.addstr(5,21,"Usuario Creado: ")
            window.addstr(5, 38, NombreU)
            ListaUsuarios.Insertar_Final(NombreU)
            espacio=window.getch()#para que exita un salto de linea en el programa
            Pintado_Titulo(window, " PLAY ")
        #Fin Creacion de Usuario


        #Ciclo Principal
        while(Movimiento!=32):
            window.timeout(150)
            #Limites del tablero
            if(Pos_y==TamañoTablero_y-1):
                Pos_y=1
            if(Pos_y==0):
                Pos_y=TamañoTablero_y-1
            if (Pos_x == TamañoTablero_x-1):
                Pos_x = 1
            if (Pos_x == 0):
                Pos_x = TamañoTablero_x - 1
            window.border(0)
            posicion_x = round((60 - len("SNAKE RELOADED")) / 2)
            window.addstr(0, posicion_x, "SNAKE RELOADED")

            # creacion de los bocadillos
            if(ExisteBocadillo==0):
                EleccionBocadillo = random.randint(0, 2)
                PosBocadillo_x = random.randint(2,TamañoTablero_x-2)
                PosBocadillo_y =random.randint(2,TamañoTablero_y-2)
                print(EleccionBocadillo)
                if (EleccionBocadillo == 0):
                    # realiza un push
                    window.addch(PosBocadillo_y,PosBocadillo_x,'+')
                    ExisteBocadillo=1
                else:
                    #realiza un pop
                    window.addch(PosBocadillo_y,PosBocadillo_x,'*')
                    ExisteBocadillo=1



            NuevoMovimiento=window.getch()
            if(NuevoMovimiento is not -1):
                Movimiento=NuevoMovimiento
            #Borrado
            for i in range(ListaSerpienet.Tamaño() + 1):
                Pos_yb = ListaSerpienet.Obtener_Pos_y(i)
                Pos_xb = ListaSerpienet.Obtener_Pos_x(i)
                window.addch(Pos_yb, Pos_xb, ' ')  # Es el que borra
            #Fin Borrado
            # Movimientos
            if Movimiento == KEY_RIGHT:
                Pos_x = Pos_x + 1
                ListaSerpienet.ActualizarPos_A(Pos_x, Pos_y)
            elif Movimiento == KEY_LEFT:
                Pos_x = Pos_x - 1
                ListaSerpienet.ActualizarPos_A(Pos_x, Pos_y)
            elif Movimiento == KEY_UP:
                Pos_y = Pos_y - 1
                ListaSerpienet.ActualizarPos_A(Pos_x, Pos_y)
            elif Movimiento == KEY_DOWN:
                Pos_y = Pos_y + 1
                ListaSerpienet.ActualizarPos_A(Pos_x, Pos_y)

            #si toca un bocadillo
            if (Pos_x == PosBocadillo_x and Pos_y == PosBocadillo_y):
                CadenaInsertar=Bloque()
                CadenaInsertar.Dar_Valor([PosBocadillo_x,PosBocadillo_y])
                if (EleccionBocadillo == 0):
                    # realiza un push
                    Pila_Bocad.Insertar(CadenaInsertar)
                    ListaSerpienet.Insertar_Final(PosBocadillo_x, PosBocadillo_y)
                else:
                    #realiza un pop
                    if(ListaSerpienet.Tamaño()<2):
                        Pila_Bocad.Eliminar()
                    else:
                        if(Pila_Bocad.Obtener_Tamaño()==0):
                            ListaSerpienet.Eliminar()
                        else:
                            Pila_Bocad.Eliminar()



                ExisteBocadillo = 0
            #impresion de Gusano
            for i in range(ListaSerpienet.Tamaño() + 1):
                Pos_yb = ListaSerpienet.Obtener_Pos_y(i)
                Pos_xb = ListaSerpienet.Obtener_Pos_x(i)
                window.addch(Pos_yb, Pos_xb, '#')  # Es el que borra
            # Fin de Impresion de Gusano

                    #Fin de Inicio de Juego
        ListaSerpienet.Imprimir()
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
        if(OpcionReportes==49):
            ListaSerpienet.Graficar()
        elif(OpcionReportes==50):
            print()
        elif(OpcionReportes==51):
            print("")
        elif(OpcionReportes==52):
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
