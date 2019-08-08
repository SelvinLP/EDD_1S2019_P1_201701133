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
from Fila_Puntuaciones import  Fila_Puntuacion
Fila_P=Fila_Puntuacion()
Pila_Bocad=Pila_Bocadillo()
ListaSerpienet=ListaDoblementeEnlazada_S()
ListaUsuarios=ListaDoblementeEnlazada_U()
#
Pausa_del_Juego=0
#variables del menu
OpcionReportes=0
UsuarioSeleccionado=""
opcion =0
Puntuacion=0
Nivel=0
#Variables de la serpiente
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
velocidad_tiempo=100

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

def Pintado_Titulo_Tablero(Vent,Puntos,Usuario):

    Vent.border(0)
    Vent.addstr(0,5,"Score :")
    Vent.addstr(0, 12, Puntos)
    Vent.addstr(0, 25, "SNAKE RELOADED")
    Vent.addstr(0, 45, "User :")
    Vent.addstr(0, 51, Usuario)

#Muestra Pantalla
Pintado_Menu(window)

#instancia de valores iniciales del juego
Pos_x = 5
Pos_y = 5


#Ciclo de Opciones
while opcion==0:
    opcion= window.getch()
    #posicion inicial de la serpiente
    if(opcion==49):#opcion 1
        ListaSerpienet.Empezar_Nuevo()
        Pila_Bocad.Iniciar_Nuevo()
        Pos_x = 5
        Pos_y = 5
        ListaSerpienet.Insertar_Final(Pos_x, Pos_y)
        ListaSerpienet.Insertar_Final(Pos_x - 1, Pos_y)
        ListaSerpienet.Insertar_Final(Pos_x - 2, Pos_y)

        Puntuacion = 0
        Movimiento = KEY_RIGHT
        Movimiento_Anterior = Movimiento


        Pintado_Titulo(window, " PLAY ")
        #Creacion de Usuario
        if (UsuarioSeleccionado == ""):
            window.addstr(5, 21, "INGRESE UN USUARIO")
            NombreU = window.getstr(1, 0, 20)
            window.addstr(5, 21, "Usuario Creado: ")
            window.addstr(5, 38, NombreU)
            ListaUsuarios.Insertar_Final(NombreU)
            UsuarioSeleccionado = NombreU
            espacio = window.getch()  # para que exita un salto de linea en el programa
            Pintado_Titulo(window, " PLAY ")
        # Fin Creacion de Usuario
        window.clear()
        #Inicio del Movimiento
        while(Pausa_del_Juego==0):

            while (Movimiento != 32):
                window.timeout(velocidad_tiempo)
                # Limites del tablero
                if (Pos_y == TamañoTablero_y - 1):
                    Pos_y = 1
                if (Pos_y == 0):
                    Pos_y = TamañoTablero_y - 1
                if (Pos_x == TamañoTablero_x - 1):
                    Pos_x = 1
                if (Pos_x == 0):
                    Pos_x = TamañoTablero_x - 1
                Pintado_Titulo_Tablero(window, str(Puntuacion), UsuarioSeleccionado)

                # creacion de los bocadillos
                if (ExisteBocadillo == 0):
                    EleccionBocadillo = random.randint(Nivel, 2)
                    PosBocadillo_x = random.randint(2, TamañoTablero_x - 2)
                    PosBocadillo_y = random.randint(2, TamañoTablero_y - 2)
                    if (EleccionBocadillo == 0 or EleccionBocadillo == 1):
                        # realiza un push
                        window.addch(PosBocadillo_y, PosBocadillo_x, '+')
                        ExisteBocadillo = 1
                    else:

                        # realiza un pop
                        window.addch(PosBocadillo_y, PosBocadillo_x, '*')
                        ExisteBocadillo = 1

                # Bloqueo de movimiento hacia direccion Opuesta
                NuevoMovimiento = window.getch()
                Movimiento_Anterior = Movimiento
                if (Movimiento == KEY_UP and NuevoMovimiento == KEY_DOWN):
                    NuevoMovimiento = Movimiento
                if (Movimiento == KEY_DOWN and NuevoMovimiento == KEY_UP):
                    NuevoMovimiento = Movimiento
                if (Movimiento == KEY_RIGHT and NuevoMovimiento == KEY_LEFT):
                    NuevoMovimiento = Movimiento
                if (Movimiento == KEY_LEFT and NuevoMovimiento == KEY_RIGHT):
                    NuevoMovimiento = Movimiento

                if (NuevoMovimiento is not -1):
                    Movimiento = NuevoMovimiento
                # Borrado
                for i in range(ListaSerpienet.Tamaño() + 1):
                    Pos_yb = ListaSerpienet.Obtener_Pos_y(i)
                    Pos_xb = ListaSerpienet.Obtener_Pos_x(i)
                    window.addch(Pos_yb, Pos_xb, ' ')  # Es el que borra
                # Fin Borrado
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
                elif Movimiento == 49:
                    newLista = ListaDoblementeEnlazada_S()
                    # prueba de invertir lista
                    for i in range(ListaSerpienet.Tamaño() + 1):
                        Pos_yb = ListaSerpienet.Obtener_Pos_y(i)
                        Pos_xb = ListaSerpienet.Obtener_Pos_x(i)
                        newLista.ParaTemporal(Pos_xb, Pos_yb)
                    ListaSerpienet.Empezar_Nuevo()
                    for i in range(newLista.Tamaño() + 1):
                        Pos_yb = newLista.Obtener_Pos_y(i)
                        Pos_xb = newLista.Obtener_Pos_x(i)
                        ListaSerpienet.Insertar_Final(Pos_xb, Pos_yb)
                    # FIN DE INVERTIR LISTA
                    # MOVIMIENTO DE INVERSION
                    if (Movimiento_Anterior == KEY_UP):
                        Movimiento = KEY_DOWN
                    if (Movimiento_Anterior == KEY_LEFT):
                        Movimiento = KEY_RIGHT
                    if (Movimiento_Anterior == KEY_DOWN):
                        Movimiento = KEY_UP
                    if (Movimiento_Anterior == KEY_RIGHT):
                        Movimiento = KEY_LEFT

                # si toca un bocadillo
                if (Pos_x == PosBocadillo_x and Pos_y == PosBocadillo_y):
                    if (EleccionBocadillo == 0 or EleccionBocadillo == 1):
                        # realiza un push
                        Puntuacion += 1
                        ListaSerpienet.Insertar_Final(PosBocadillo_x, PosBocadillo_y)
                        Pila_Bocad.Insertar(PosBocadillo_x, PosBocadillo_y)
                    else:
                        if (ListaSerpienet.size > 2):
                            ListaSerpienet.Eliminar()
                            Puntuacion -= 1
                        Pila_Bocad.Eliminar()
                    ExisteBocadillo = 0

                    #Pausa del Juego
                    # impresion de Gusano
                for i in range(ListaSerpienet.Tamaño() + 1):
                    Pos_yb = ListaSerpienet.Obtener_Pos_y(i)
                    Pos_xb = ListaSerpienet.Obtener_Pos_x(i)
                    window.addch(Pos_yb, Pos_xb, '#')

                # Comprobacion si topa con si misma
                for i in range(1, ListaSerpienet.Tamaño()):
                    Pos_yb = ListaSerpienet.Obtener_Pos_y(i)
                    Pos_xb = ListaSerpienet.Obtener_Pos_x(i)
                    if (Pos_x == Pos_xb and Pos_y == Pos_yb):
                        window.clear()
                        window.addstr(7, 25, "FIN DEL JUEGO")
                        window.addstr(9, 25, "Presione DELETE para salir")
                        Movimiento = 32

                # Fin de Impresion de Gusano
                Pintado_Titulo_Tablero(window, str(Puntuacion), UsuarioSeleccionado)
                if (Puntuacion == 15):
                    velocidad_tiempo = 60
                    Pila_Bocad.Iniciar_Nuevo()
                if (Puntuacion == 20):
                    velocidad_tiempo = 40
                    Pila_Bocad.Iniciar_Nuevo()
                if (Puntuacion == 40):
                    velocidad_tiempo = 20
                    Pila_Bocad.Iniciar_Nuevo()
                if (Puntuacion == 60):
                    window.clear()
                    window.addstr(7, 25, "HAS GANADO")
                    window.addstr(9, 25, "Presione DELETE para salir")
                    Movimiento = 32

            #Fin de segundo while
            window.clear()
            window.addstr(7, 25, "JUEGO PAUSADO")
            window.addstr(8, 25, "1. Continuar")
            window.addstr(9, 25, "2. Generar Reporte Score")
            window.addstr(10, 25, "3. Generar Reporte Snake")
            window.addstr(11, 25, "Presione DELETE para salir")
            OpcionPausa = window.getch()
            if (OpcionPausa is not -1):
                if (OpcionPausa == 49):
                    ExisteBocadillo = 0
                    window.clear()
                    Movimiento = Movimiento_Anterior
                if (OpcionPausa == 50):
                    window.clear()
                    Pila_Bocad.Graficar()
                if (OpcionPausa == 51):
                    window.clear()
                    ListaSerpienet.Graficar()
                if (OpcionPausa == 8):
                    Pausa_del_Juego=1

        # Fin de Inicio de Juego
        Fila_P.Insertar(UsuarioSeleccionado, Puntuacion)
        UsuarioSeleccionado = ""
        ExisteBocadillo=0
        Pintado_Menu(window)
        opcion = 0
        Pausa_del_Juego=0


    elif(opcion==50):#opcion 2
        Pintado_Titulo(window, " SCOREBOARD ")
        window.addstr(5, 25, "NOMBRE")
        window.addstr(5, 40, "PUNTUACION")
        Fila_P.Imprimir(window)
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
        while(OpcionReportes!=8):
            Pintado_Titulo(window, " REPORTS ")
            window.addstr(7, 21, '1. SNAKE REPORT')
            window.addstr(8, 21, '2. SCORE REPORT')
            window.addstr(9, 21, '3. SCOREBOARD REPORT')
            window.addstr(10, 21, '4. USERS REPORT')

            OpcionReportes = window.getch()
            if (OpcionReportes == 49):
                ListaSerpienet.Graficar()

            elif (OpcionReportes == 50):
                Pila_Bocad.Graficar()
            elif (OpcionReportes == 51):
                Fila_P.Graficar()
            elif (OpcionReportes == 52):
                ListaUsuarios.Graficar()
            else:
                window.addstr(11, 21, 'Opcion Incorrecta')
            window.addstr(12, 21, 'Presione DELETE para salir')

        Pintado_Menu(window)
        opcion = 0
        #Fin opcion 4




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
