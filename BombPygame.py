import random
import sys
from time import sleep

import pygame
import pygame_textinput
from pygame import *

pygame.init() #Iniciando la libreria

sizeScreen= (950, 700) #Definiendo tamaño de ventana

# ---- Tipografía ----
tipografia = font.SysFont("Helvetica", 20, bold=True)

# ---- Volumen Global Inicial ----
volumenGlobal = 1.0

# ----------------------------------- Iniciando la Ventana de Información -----------------------------------
def screenInformacion():
    pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el volumen
    ventanaInformacion = pygame.display.set_mode(sizeScreen) #Creación de Ventana
    ventanaInformacion.fill("#FFC154") #Color de fondo
    # ---- Dibujando rectángulo ----
    pygame.draw.rect(ventanaInformacion, ("#FFFFFF"), (95, 95, 760, 270), 0)
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes/BotonRegreso.png") #Agregando Imagen representativa de botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (50, 50))  #Ajustando el tamaño
    ventanaInformacion.blit(botonRegreso, (15,15)) #Visualizar la imagen con su posición
    # ---- Imágen de la autora ----
    botonRegreso = pygame.image.load("Imagenes//autora.png") #Agregando imagen mía
    botonRegreso = pygame.transform.scale(botonRegreso, (130, 230))  #Ajustando el tamaño
    ventanaInformacion.blit(botonRegreso, (115,115)) #Visualizar la imagen con su posición
    # ---- Creando Textos ----
    nombre = tipografia.render("Camila Lizano Brenes", True, ("#000000")) #Indicando mi nombre
    ventanaInformacion.blit(nombre, (260, 115)) #Reflejando el texto
    cedula = tipografia.render("Cédula: 119390227", True, ("#000000")) #Indicando mi cédula
    ventanaInformacion.blit(cedula, (260, 150)) #Reflejando el texto
    carnet = tipografia.render("Carné: 2024255324", True, ("#000000")) #Indicando mi carnet
    ventanaInformacion.blit(carnet, (260, 185)) #Reflejando el texto
    carrera = tipografia.render("Carrera: Ingeniería en Computadores", True, ("#000000")) #Indicando mi carrera
    ventanaInformacion.blit(carrera, (260, 220)) #Reflejando el texto
    asignatura = tipografia.render("Curso: Introducción a la Programación", True, ("#000000")) #Indicando la asignatura
    ventanaInformacion.blit(asignatura, (260, 255)) #Reflejando el texto
    profesor = tipografia.render("Nombre de Profesor: Leonardo Araya", True, ("#000000")) #Indicando el nombre del profesor
    ventanaInformacion.blit(profesor, (260, 290)) #Reflejando el texto
    institucion = tipografia.render("Tecnológico de Costa Rica, campus Central", True, ("#000000")) #Indicando la institución
    ventanaInformacion.blit(institucion, (260, 320)) #Reflejando el texto
    pais = tipografia.render("Costa Rica", True, ("#000000")) #Indicando el país
    ventanaInformacion.blit(pais, (700, 115)) #Reflejando el texto
    version = tipografia.render("Python 3.12.2", True, ("#000000")) #Indicando la versión de python
    ventanaInformacion.blit(version, (700, 150)) #Reflejando el texto
    # ---- Dibujando rectángulo ----
    pygame.draw.rect(ventanaInformacion, ("#FF4D39"), (95, 400, 760, 230), 0)
    # ---- Creando Textos ----
    informacion = tipografia.render("Acerca del Juego", True, ("#FFFFFF")) #Indicando parámetros de mi título
    xPregunta = (ventanaInformacion.get_width() - informacion.get_width()) / 2 #Calcular la posición horizontal para centrar el texto
    ventanaInformacion.blit(informacion, (xPregunta, 420)) #Reflejando el texto
    contexto = tipografia.render("El juego consiste en movilizarse por el laberinto manteniendo cuidado por los enemigos.", True, ("#FFFFFF")) #Indicando contexto
    xcontexto = (ventanaInformacion.get_width() - contexto.get_width()) / 2 #Calcular la posición horizontal para centrar el texto
    ventanaInformacion.blit(contexto, (xcontexto, 460)) #Reflejando el texto
    contexto1 = tipografia.render("Se cuenta con una cantidad de bombas limitadas y la idea es conseguir la llave que abre", True, ("#FFFFFF")) #Indicando contexto
    xcontexto1 = (ventanaInformacion.get_width() - contexto1.get_width()) / 2 #Calcular la posición horizontal para centrar el texto
    ventanaInformacion.blit(contexto1, (xcontexto1, 495)) #Reflejando el texto
    contexto2 = tipografia.render("una puerta en el laberinto que te lleva a un siguiente nivel que aumenta su dificultad.", True, ("#FFFFFF")) #Indicando contexto
    xcontexto2 = (ventanaInformacion.get_width() - contexto2.get_width()) / 2 #Calcular la posición horizontal para centrar el texto
    ventanaInformacion.blit(contexto2, (xcontexto2, 530)) #Reflejando el texto
    contexto3 = tipografia.render("Si deseas ganar debes de realizar la operación en la menor cantidad de tiempo posible.", True, ("#FFFFFF"))#Indicando contexto
    xcontexto3 = (ventanaInformacion.get_width() - contexto3.get_width()) / 2 #Calcular la posición horizontal para centrar el texto
    ventanaInformacion.blit(contexto3, (xcontexto3, 565)) #Reflejando el texto

    # ---- Bucle de la ventana de Información ----
    while True:
        for event in pygame.event.get(): #Iterando sobre eventos
            if (event.type == pygame.QUIT): #Si usuario intenta cerrar ventana:
                return #Cerrar juego
            elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                if (event.button == 1): #Verificar si fue clic izquierdo
                    x, y = event.pos #Guardando en variables donde se hizo clic
                    # ---- Verificar si el clic fue dentro de alguno de los botones de la Ventana de Información ----
                    if (15 < x < 65 and 15 < y < 65): #Botón de Regreso
                        screenPrincipal(volumenGlobal) #Ir a ventana principal
        pygame.display.flip() #Actualizar Pantalla
    
# ----------------------------------- Finalizando la Ventana de Información -----------------------------------
    
# ----------------------------------- Iniciando la Ventana de Configuración -----------------------------------
# ---- Botones ----
def screenConfiguracion():
    ventanaConfiguracion = pygame.display.set_mode(sizeScreen) #Creación de Ventana
    fondoVentanaConfiguracion = pygame.image.load("Imagenes/FondoConfiguración.png") #Agregando fondo de pantalla de Configuración
    ventanaConfiguracion.blit(fondoVentanaConfiguracion, (0,0)) #Visualizar el fondo
    draw.rect(ventanaConfiguracion, ("#000000"), (95, 95, 760, 510), 0) #Dibujando el borde del rectángulo
    rectanguloVentanaConfiguracion = pygame.image.load("Imagenes/confrec.png") #Agregando rectángulo de Configuración
    ventanaConfiguracion.blit(rectanguloVentanaConfiguracion, (100,100)) #Visualizar el rectángulo
    # ---- Activar Sonido ----
    activarMusica = pygame.image.load("Imagenes/VOL-ACT.png") #Agregando Imagen representativa de activar volumen
    activarMusica = pygame.transform.scale(activarMusica, (100, 100)) #Ajustando el tamaño
    ventanaConfiguracion.blit(activarMusica, (270,220)) #Visualizar la imagen con su posición
    
    # ---- Subir Volumen ----
    subirVolumen = pygame.image.load("Imagenes/VOL-SUB.png") #Agregando Imagen representativa de subir volumen
    subirVolumen = pygame.transform.scale(subirVolumen, (100, 100)) #Ajustando el tamaño
    ventanaConfiguracion.blit(subirVolumen, (370,220)) #Visualizar la imagen con su posición
    
    # ---- Bajar Volumen ----
    bajarVolumen = pygame.image.load("Imagenes/VOL-BAJ.png") #Agregando Imagen representativa de bajar volumen
    bajarVolumen = pygame.transform.scale(bajarVolumen, (100, 100)) #Ajustando el tamaño
    ventanaConfiguracion.blit(bajarVolumen, (470,220)) #Visualizar la imagen con su posición
    
    # ---- Desactivar Sonido ----
    desactivarMusica = pygame.image.load("Imagenes/VOL-QUIT.png") #Agregando Imagen representativa de desactivar volumen
    desactivarMusica = pygame.transform.scale(desactivarMusica, (100, 100)) #Ajustando el tamaño
    ventanaConfiguracion.blit(desactivarMusica, (570,220)) #Visualizar la imagen con su posición
    
    # ---- Botón Personalizar ----
    botonPersonalizar = pygame.image.load("Imagenes/PuertaPersonalizar.png") #Agregando Imagen representativa del botón personalizar
    botonPersonalizar = pygame.transform.scale(botonPersonalizar, (250, 250)) #Ajustando el tamaño
    ventanaConfiguracion.blit(botonPersonalizar, (350,340)) #Visualizar la imagen con su posición
    
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes/BotonRegreso.png") #Agregando Imagen representativa del botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (50, 50)) #Ajustando el tamaño
    ventanaConfiguracion.blit(botonRegreso, (15,15)) #Visualizar la imagen con su posición
    
    # ---- Posiciones de los botones de Sonido ----
    botonActivarMusica = Rect(280,220,70,70) #X, Y, Ancho, Alto
    botonSubirVolumen = Rect(380,220,70,70) #X, Y, Ancho, Alto
    botonBajarVolumen = Rect(480,220,70,70) #X, Y, Ancho, Alto
    botonDesactivarMusica = Rect(580,220,70,70) #X, Y, Ancho, Alto
    # ---- Posición del botón de Personalización ----
    botonPersonalizacion = Rect(400,380,140,200) #X, Y, Ancho, Alto
    # ---- Posición del botón de Regreso ----
    botonRegreso = Rect(15,15,50,50) #X, Y, Ancho, Alto

    # ---- Funciones de Botones de Sonido ----
    # ---- Activar Sonido ----
    def sonidoActivado():
        global volumenGlobal #Llamando a variable global de volumen inicial
        if (botonActivarMusica.collidepoint(x, y)): #Si se presiona el botón de activar música:
            volumenGlobal = 1.0 #Activando música con volumen al máximo
            pygame.mixer.music.set_volume(volumenGlobal) #Estableciendo el volumen
    # ---- Subir Volumen ----
    def volumenAumenta():
        global volumenGlobal #Llamando a variable global de volumen inicial
        if (botonSubirVolumen.collidepoint(x, y) and volumenGlobal < 1.0): #Si se presiona el botón de subir volumen y el volumen no está en su máximo:
            volumenGlobal += 0.1 #Subiendo el volumen de 0.1 en 0.1
            pygame.mixer.music.set_volume(volumenGlobal) #Estableciendo el volumen
    # ---- Bajar Volumen ----
    def volumenDisminuye():
        global volumenGlobal #Llamando a variable global de volumen inicial
        if (botonBajarVolumen.collidepoint(x, y) and volumenGlobal > 0.0): #Si se presiona el botón de bajar volumen y el volumen no está en su mínimo:
            volumenGlobal -= 0.1 #Bajando el volumen de 0.1 en 0.1
            pygame.mixer.music.set_volume(volumenGlobal) #Estableciendo el volumen
    # ---- Desactivar Sonido ----
    def sonidoDesactivado():
        global volumenGlobal #Llamando a variable global de volumen inicial
        if (botonDesactivarMusica.collidepoint(x, y)): #Si se presiona el botón de desactivar música:
            volumenGlobal = 0.0 #Desactivando música por completo
            pygame.mixer.music.set_volume(volumenGlobal) #Estableciendo el volumen
        
    # ---- Bucle de la Ventana de Configuración ----
    while True:
        for event in pygame.event.get(): #Iterando sobre eventos
            if (event.type == pygame.QUIT): #Si usuario intenta cerrar ventana:
                return #Cerrar ventana
            elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                if (event.button == 1): #Verificar si fue clic izquierdo
                    x, y = event.pos #Guardando en variables donde se hizo clic
                    # ---- Verificar si el clic fue dentro de alguno de los botones de la Ventana de Configuración ----
                    if (botonActivarMusica.collidepoint(event.pos)):
                        sonidoActivado()
                    elif (botonSubirVolumen.collidepoint(event.pos)):
                        volumenAumenta()
                    elif (botonBajarVolumen.collidepoint(event.pos)):
                        volumenDisminuye()
                    elif (botonDesactivarMusica.collidepoint(event.pos)):
                        sonidoDesactivado()
                    elif (botonPersonalizacion.collidepoint(event.pos)):
                        screenPersonalización()
                    elif (botonRegreso.collidepoint(event.pos)):
                        screenPrincipal(volumenGlobal)
        pygame.display.flip() #Actualizando la pantalla
                    
# ----------------------------------- Finalizando la Ventana de Configuración -----------------------------------

# ----------------------------------- Iniciando la Ventana de Personalización -----------------------------------
nombreUsuario = "" #Guardando el nombre ingresado por el usuario
def screenPersonalización():
    pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el volumen
    global nombreUsuario
    global skinSeleccionada #Globalizando mi variable para la skin del personaje
    ventanaPersonalizacion = pygame.display.set_mode((950, 700)) #Creación de Ventana
    ventanaPersonalizacion.fill("#ff994c") #Agregando color de fondo
    cartelEleccionPersonaje = pygame.image.load("Imagenes/CartelElección.png") #Agregando Imagen representativa del cartel de Elección
    cartelEleccionPersonaje = pygame.transform.scale(cartelEleccionPersonaje, (300, 300)) #Ajustando el tamaño
    ventanaPersonalizacion.blit(cartelEleccionPersonaje, (330,0)) #Visualizar la imagen con su posición
    pygame.draw.rect(ventanaPersonalizacion, ("#FFFFFF"), (0, 180, 950, 300)) #Agregando cuadro blanco
    # ---- Agregando imágenes de las diferentes skins del personaje principal ----
    # ---- Skin 1 ----
    skin1Personaje = pygame.image.load("Imagenes/Skin1(Principal).png") #Agregando Imagen representativa de la skin 1
    skin1Personaje = pygame.transform.scale(skin1Personaje, (240, 240)) #Ajustando el tamaño
    ventanaPersonalizacion.blit(skin1Personaje, (80,190)) #Visualizar la imagen con su posición
    # ---- Skin 2 ----
    skin2Personaje = pygame.image.load("Imagenes/Skin2(Principal).png") #Agregando Imagen representativa de la skin 2
    skin2Personaje = pygame.transform.scale(skin2Personaje, (240, 240)) #Ajustando el tamaño
    ventanaPersonalizacion.blit(skin2Personaje, (360,190)) #Visualizar la imagen con su posición
    # ---- Skin 3 ----
    skin3Personaje = pygame.image.load("Imagenes/Skin3(Principal).png") #Agregando Imagen representativa de la skin 3
    skin3Personaje = pygame.transform.scale(skin3Personaje, (240, 240)) #Ajustando el tamaño
    ventanaPersonalizacion.blit(skin3Personaje, (640,190)) #Visualizar la imagen con su posición
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes/BotonRegreso.png") #Agregando Imagen representativa de activar volumen
    botonRegreso = pygame.transform.scale(botonRegreso, (50, 50)) #Ajustando el tamaño
    posicionRegreso = ventanaPersonalizacion.blit(botonRegreso, (15,15)) #Visualizar la imagen con su posición
    # ---- Creando Botones para la Selección de las diferentes Skins disponibles ----
    # ---- Cargando las imágenes de los botones ----
    # ---- Imágenes Seleccionadas ----
    imagenSeleccionadaOpcion1 = pygame.image.load("Imagenes/seleccionado.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion1 = pygame.transform.scale(imagenSeleccionadaOpcion1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1 = ventanaPersonalizacion.blit(imagenSeleccionadaOpcion1, (170,400)) #Visualizar la imagen con su posición
    imagenSeleccionadaOpcion2 = pygame.image.load("Imagenes/seleccionado.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion2 = pygame.transform.scale(imagenSeleccionadaOpcion2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2 = ventanaPersonalizacion.blit(imagenSeleccionadaOpcion2, (445,400)) #Visualizar la imagen con su posición
    imagenSeleccionadaOpcion3 = pygame.image.load("Imagenes/seleccionado.png") #Agregando Imagen representativa del botón seleccionado
    imagenSeleccionadaOpcion3 = pygame.transform.scale(imagenSeleccionadaOpcion3, (70, 70)) #Ajustando el tamaño
    posicionOpcion3 = ventanaPersonalizacion.blit(imagenSeleccionadaOpcion3, (725,400)) #Visualizar la imagen con su posición
    # ---- Imágenes No Seleccionadas ----
    imagenNoSeleccionadaOpcion1 = pygame.image.load("Imagenes/noseleccionado.png") #Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion1 = pygame.transform.scale(imagenNoSeleccionadaOpcion1, (70, 70)) #Ajustando el tamaño
    posicionOpcion1 = ventanaPersonalizacion.blit(imagenNoSeleccionadaOpcion1, (170,400)) #Visualizar la imagen con su posición
    imagenNoSeleccionadaOpcion2 = pygame.image.load("Imagenes/noseleccionado.png") #Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion2 = pygame.transform.scale(imagenNoSeleccionadaOpcion2, (70, 70)) #Ajustando el tamaño
    posicionOpcion2 = ventanaPersonalizacion.blit(imagenNoSeleccionadaOpcion2, (445,400)) #Visualizar la imagen con su posición
    imagenNoSeleccionadaOpcion3 = pygame.image.load("Imagenes/noseleccionado.png") #Agregando Imagen representativa del botón no seleccionado
    imagenNoSeleccionadaOpcion3 = pygame.transform.scale(imagenNoSeleccionadaOpcion3, (70, 70)) #Ajustando el tamaño
    posicionOpcion3 = ventanaPersonalizacion.blit(imagenNoSeleccionadaOpcion3, (725,400)) #Visualizar la imagen con su posición

    # ---- Estableciendo el estado inicial de selección donde todas están apagadas (no seleccionadas) ----
    opcion1Seleccionada = False
    opcion2Seleccionada = False
    opcion3Seleccionada = False
    
    # ---- Agregando entrada de usuario ----
    global textoUsuario
    textoUsuario = "" #Iniciando cadena vacía, aquí se guardará lo que el usuario escriba
    rectanguloEntrada = pygame.Rect(380, 590, 200, 50) #Creando medidas y definiendo posiciones del rectángulo de entrada de texto
    
    # ---- Agregando cartel de indicación ----
    cartelIndicacionNombre = pygame.image.load("Imagenes/Cartel-Indicación.png") #Agregando Imagen representativa del cartel de Indicación
    cartelIndicacionNombre = pygame.transform.scale(cartelIndicacionNombre, (250, 250)) #Ajustando el tamaño
    ventanaPersonalizacion.blit(cartelIndicacionNombre, (355,410)) #Visualizar la imagen con su posición
    
    while True: #Bucle para ventana de Personalización
        for event in pygame.event.get(): #Iterando sobre eventos
            if (event.type == pygame.QUIT): #Si el usuario intenta cerrar ventana:
                sys.exit() #Saliendo del Juego
            elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                if (event.button == 1): #Verificar si fue clic izquierdo
                    if (posicionOpcion1.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 1
                        opcion1Seleccionada = True #Encendido
                        opcion2Seleccionada = False #Apagado
                        opcion3Seleccionada = False #Apagado
                        skinSeleccionada = 1 #Guardando la skin seleccionada
                    elif (posicionOpcion2.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 2
                        opcion1Seleccionada = False #Apagado
                        opcion2Seleccionada = True #Encendido
                        opcion3Seleccionada = False #Apagado
                        skinSeleccionada = 2 #Guardando la skin seleccionada
                    elif (posicionOpcion3.collidepoint(event.pos)): #Verificar si se presionó el botón de la opción 3
                        opcion1Seleccionada = False #Apagado
                        opcion2Seleccionada = False #Apagado
                        opcion3Seleccionada = True #Encendido
                        skinSeleccionada = 3 #Guardando la skin seleccionada
                    elif (posicionRegreso.collidepoint(event.pos)): #Verificar si se presionó el botón de regreso
                        screenConfiguracion() #Ir a Ventana de Configuración
                        return #Saliendo del bucle
            elif (event.type == pygame.KEYDOWN): #Detección de teclas
                if (event.key == pygame.K_BACKSPACE): #Detección de tecla de retroceso
                    textoUsuario = textoUsuario[:-1] #Elimina el último carácter de textoUsuario
                    pygame.draw.rect(ventanaPersonalizacion, ("#ff994c"), rectanguloEntrada) #Limpiando el área de la entrada de texto en la ventana
                elif (event.key == pygame.K_RETURN): #Detección de la tecla ENTER
                    nombreUsuario = textoUsuario #Guardando nombre
                    print("Texto ingresado:", nombreUsuario) #Imprimir texto en consola
                    textoUsuario = "" #Reestablecer texto a cadena vacía
                else:
                    if (event.unicode.isprintable() and len(textoUsuario) <= 20): #Verificando si tecla presionada es imprimible (carácter visible) y que su máximo sean 20 caracteres
                        textoUsuario += event.unicode #Agregando carácter imprimible
        
        # ---- Dibujando los botones con la apariencia correspondiente a su estado de selección ----
        ventanaPersonalizacion.blit(imagenSeleccionadaOpcion1 if opcion1Seleccionada else imagenNoSeleccionadaOpcion1, posicionOpcion1)
        ventanaPersonalizacion.blit(imagenSeleccionadaOpcion2 if opcion2Seleccionada else imagenNoSeleccionadaOpcion2, posicionOpcion2)
        ventanaPersonalizacion.blit(imagenSeleccionadaOpcion3 if opcion3Seleccionada else imagenNoSeleccionadaOpcion3, posicionOpcion3)
        # ---- Dibujando la entrada del usuario ----
        pygame.draw.rect(ventanaPersonalizacion, ("#000000"), rectanguloEntrada, 2) #Dibujando rectángulo para texto
        superficieTexto = tipografia.render(textoUsuario, True, ("#000000")) #Dibujando el texto, true para más nítido
        ventanaPersonalizacion.blit(superficieTexto, (rectanguloEntrada.x + 10, rectanguloEntrada.y + 12)) #Dibujando la posición del texto
        rectanguloEntrada.w = max(200, superficieTexto.get_width() + 10) #Dibujando ancho mínimo de rectángulo y asegurando un margen de 10px para el texto
        pygame.display.flip() #Actualizando la pantalla
# ----------------------------------- Finalizando la Ventana de Personalización -----------------------------------

# ----------------------------------- Iniciando la Ventana de Derrota -----------------------------------
def screenDerrota():
    pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el volumen
    ventanaDerrota = pygame.display.set_mode((950, 700)) #Creación de Ventana
    fondoVentanaDerrota = pygame.image.load("Imagenes//DerrotaPantalla.png") #Agregando fondo de pantalla de derrota
    ventanaDerrota.blit(fondoVentanaDerrota, (0,0)) #Visualizar el fondo
    tipografia = font.SysFont("Helvetica", 35, bold=True) #Actualizando la tipografía
    preguntaReiniciarJuego = tipografia.render("¿Volver a Jugar?", True, ("#FFFFFF"))  #Indicando parámetros de mi pregunta
    xPregunta = (ventanaDerrota.get_width() - preguntaReiniciarJuego.get_width()) / 2 #Calcular la posición horizontal para centrar el texto
    yPregunta = 480  #Posición vertical fija para el texto (pregunta)
    ventanaDerrota.blit(preguntaReiniciarJuego, (xPregunta, yPregunta)) #Reflejando el texto (pregunta)
    
    # ---- Botón de Volver a Jugar ----
    reiniciarJuego = pygame.image.load("Imagenes//VolverJugar.png") #Agregando Imagen representativa para reinicio de juego
    reiniciarJuego = pygame.transform.scale(reiniciarJuego, (80, 80)) #Ajustando el tamaño
    posicionReinicio = ventanaDerrota.blit(reiniciarJuego, (370,550)) #Visualizar la imagen con su posición
    
    # ---- Botón de Salir ----
    salirJuego = pygame.image.load("Imagenes//Salir.png") #Agregando Imagen representativa para salir del juego
    salirJuego = pygame.transform.scale(salirJuego, (80, 80)) #Ajustando el tamaño
    posicionSalida = ventanaDerrota.blit(salirJuego, (500,550)) #Visualizar la imagen con su posición
    
    # ---- Bucle principal de Ventana de Derrota ----
    running = True
    while running:
        for event in pygame.event.get(): #Iterando sobre eventos
            if (event.type == pygame.QUIT): #Si el usuario intenta cerrar ventana:
                pygame.quit() #Cerrando módulos de pygame
                sys.exit() #Asegurando salida del juego
            elif (event.type == pygame.KEYDOWN): #Detectando Teclas
                if (event.key == pygame.K_ESCAPE):
                    running = False  #Salir del bucle si se presiona la tecla Esc
            elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                if (event.button == 1): #Verificar si fue clic izquierdo
                    if (posicionReinicio.collidepoint(event.pos)): #Verificar si se presionó el botón de reinicio
                        screenJuego1() #Devolverse a ventana de juego
                    if (posicionSalida.collidepoint(event.pos)): #Verificar si se presionó el botón de salida
                        screenPrincipal(volumenGlobal) #Devolverse a ventana principal
        pygame.display.flip() #Actualizando pantalla

# ----------------------------------- Finalizando la Ventana de Derrota -----------------------------------

# ----------------------------------- Iniciando la Ventana de Juego 1 -----------------------------------
skinSeleccionada = 1 #Skin predeterminada
def screenJuego1():
    pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el Volumen
    ventanaJuego = pygame.display.set_mode((950, 700)) #Creación de Ventana
    tamañoBloques = 50 #Tamaño de los bloques

    # ---- Agregando Imágenes de los Enemigos ----
    imagenEnemigo1F = pygame.image.load("Imagenes//Monstruo1n1.png") #Agregando Imágen de Monstruo 1 en nivel 1
    imagenEnemigo1F = pygame.transform.scale(imagenEnemigo1F, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    imagenEnemigo2F = pygame.image.load("Imagenes//Monstruo2n2.png") #Agregando Imágen de Monstruo 2 en nivel 1
    imagenEnemigo2F = pygame.transform.scale(imagenEnemigo2F, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    
    # ---- Definiendo las Posiciones Iniciales de los Enemigos ----
    posicionEnemigo1 = (2, 2)
    posicionEnemigo2 = (4, 16)
    posicionEnemigo3 = (10, 4)
    posicionEnemigo4 = (9, 10)
    posicionesEnemigos = [posicionEnemigo1, posicionEnemigo2, posicionEnemigo3, posicionEnemigo4] #Coordenadas iniciales de los enemigos
    
    # ---- Agregando Imágenes del Personaje Principal ----
    personaje1 = pygame.image.load("Imagenes//Skin1(Principal).png") #Agregando Imágen de Skin 1
    personaje1 = pygame.transform.scale(personaje1, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    personaje2 = pygame.image.load("Imagenes//Skin2(Principal).png") #Agregando Imágen de Skin 2
    personaje2 = pygame.transform.scale(personaje2, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    personaje3 = pygame.image.load("Imagenes//Skin3(Principal).png") #Agregando Imágen de Skin 3
    personaje3 = pygame.transform.scale(personaje3, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    
    # ---- Agregando el condicional para seleccionar la imagen correspondiente a la skin del personaje principal ----
    if (skinSeleccionada == 1):
        imagenPersonajePrincipal = personaje1
    elif (skinSeleccionada == 2):
        imagenPersonajePrincipal = personaje2
    elif (skinSeleccionada == 3):
        imagenPersonajePrincipal = personaje3
    
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes/BotonRegreso.png") #Agregando Imagen representativa del botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (40, 40)) #Ajustando el tamaño
    posicionRegreso = ventanaJuego.blit(botonRegreso, (10,655)) #Visualizar la imagen con su posición
    
    # ---- Cargar imágenes de bloques sólidos y destructibles ----
    imagenBloqueSolido = pygame.image.load("Imagenes//solid-bloque.png") #Agregando Imagen representativa de bloque sólido
    imagenBloqueSolido = pygame.transform.scale(imagenBloqueSolido, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño
    imagenBloqueDestructible = pygame.image.load("Imagenes//des-bloque.png") #Agregando Imagen representativa de bloque destructible
    imagenBloqueDestructible = pygame.transform.scale(imagenBloqueDestructible, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño
    
    # ---- Cargar imágenes de posesión de la llave ----
    poseerLlave = pygame.image.load("Imagenes//llave.png") #Agregando Imagen representativa para saber si se tiene la llave
    poseerLlave = pygame.transform.scale(poseerLlave, (100, 40)) #Ajustando el tamaño
    ventanaJuego.blit(poseerLlave, (640, 655)) #Visualizar la imagen con su posición
    tengoLlave = False #Inicialmente no tengo la llave
    tipografia = font.SysFont("Helvetica", 35, bold=True) #Actualizando la tipografía
    noTengoLlave = tipografia.render("0", True, ("#FFFFFF")) #Indicando parámetros para indicar que no tengo la llave
    ventanaJuego.blit(noTengoLlave, (730, 655)) #Reflejando que tengo 0 llaves
    
    # ---- Cargar imágen que cuenta las bombas ----
    bombasTotales = pygame.image.load("Imagenes//contadorBombas.png") #Agregando Imagen representativa de contador de bombas
    bombasTotales = pygame.transform.scale(bombasTotales, (100, 40)) #Ajustando el tamaño
    ventanaJuego.blit(bombasTotales, (470, 655)) #Visualizar la imagen con su posición
    global contadorBombas #Globalizando mi variable
    contadorBombas = 16 #Inicialmente tengo disponibles 16 bombas
    cantidadBomb = tipografia.render("16", True, ("#FFFFFF"))  #Indicando parámetros para indicar que tengo 16 bombas
    ventanaJuego.blit(cantidadBomb, (570, 655)) #Reflejando la cantidad de bombas
    
    # ---- Creando el Laberinto ----
    #El valor 0 son los pasillos
    #El valor 1 son los bloques sólidos
    #El valor 2 son los bloques destructibles
    #El valor 3 es la puerta
    laberinto1= [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,1,0,0,1,2,0,0,1,0,0,0,0,2,1,1],
                [1,2,0,0,0,1,0,0,2,0,2,0,0 ,0,2,0,1,2,1],
                [1,0,1,0,0,1,1,0,1,0,1,0,1,1,0,0,0,0,1],
                [1,2,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1],
                [1,2,2,0,1,0,2,1,0,1,0,0,1,2,0,2,1,0,1],
                [1,2,0,0,0,1,0,0,0,1,0,1,2,2,1,0,1,1,1],
                [1,0,0,1,0,0,0,1,0,0,1,2,0,0,1,0,0,2,1],
                [1,1,2,0,0,1,2,2,0,0,0,1,0,2,0,1,0,0,1],
                [1,0,0,0,0,0,0,1,0,0,0,1,0,1,3,0,0,2,1],
                [1,0,2,1,1,0,0,1,2,1,2,0,2,2,0,2,0,0,1],
                [1,0,0,2,0,0,0,0,2,0,1,0,1,0,0,0,0,2,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    
    # ---- Imágen de LLave ----
    imagenLlave = pygame.image.load("Imagenes//llave.png") #Agregando Imagen representativa de la llave
    imagenLlave = pygame.transform.scale(imagenLlave, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño
    # ---- Definiendo la posición de la llave de forma aleatoria ----
    fila_llave, columna_llave = random.choice([(fila, columna) for fila in range(len(laberinto1)) #Generando lista de todas las coordenadas donde (fila, columna) sea 2
                                                for columna in range(len(laberinto1[0])) #0 es por el primer elemento de la fila
                                                if laberinto1[fila][columna] == 2])
    
    # ---- Dibujando el Laberinto ----
    def dibujandoLaberinto():
        for fila in range(len(laberinto1)): #Recorriendo desde fila 0 hasta el final de la fila
            for columna in range(len(laberinto1[0])): #Recorriendo desde columna 0 hasta el final de la columna
                if (laberinto1[fila][columna] == 0): #Condición si hay un 0 en el laberinto
                    pygame.draw.rect(ventanaJuego, ("#AAAAAA"), (columna*tamañoBloques, fila*tamañoBloques, tamañoBloques, tamañoBloques)) #Agregando Pasillos
                elif (laberinto1[fila][columna] == 1): #Condición si hay un 1 en el laberinto
                    ventanaJuego.blit(imagenBloqueSolido, (columna*tamañoBloques, fila*tamañoBloques)) #Agregando imágen de bloque sólido
                elif (laberinto1[fila][columna] == 2): #Condición si hay un 2 en el laberinto
                    ventanaJuego.blit(imagenBloqueDestructible, (columna*tamañoBloques, fila*tamañoBloques)) #Agregando imágen de bloque destructible
                elif (laberinto1[fila][columna] == 3): #Condición si hay un 3 en el laberinto
                    imagenPuerta = pygame.image.load("Imagenes//puerta.png") #Agregando imágen de puerta
                    imagenPuerta = pygame.transform.scale(imagenPuerta, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño
                    ventanaJuego.blit(imagenPuerta, (columna*tamañoBloques, fila*tamañoBloques)) #Visualizar la imagen con su posición
                    global fila_puerta, columna_puerta #Globalizando las coordenadas con la fila y la columna de la posición de la puerta
                    fila_puerta, columna_puerta = fila, columna
    
    # ---- Definiendo el Movimiento de los enemigos ----
    def movimientoEnemigos(laberinto1):
        for i, (y_enemigo, x_enemigo) in enumerate(posicionesEnemigos): #Iterando sobre todas las posiciones de los enemigos. (índice de posición y coordenadas)
            movimientosValidos = [] #Inicializando lista vacía que va a guardar los movimientos validos de mis enemigos
            if (laberinto1[y_enemigo - 1][x_enemigo] == 0): #Si arriba del enemigo es un pasillo:
                movimientosValidos.append('up') #Se puede mover hacia arriba
            if (laberinto1[y_enemigo + 1][x_enemigo] == 0): #Si abajo del enemigo es un pasillo:
                movimientosValidos.append('down') #Se puede mover hacia abajo
            if (laberinto1[y_enemigo][x_enemigo - 1] == 0): #Si al lado izquierdo del enemigo es un pasillo:
                movimientosValidos.append('left') #Se puede mover hacia la izquierda
            if (laberinto1[y_enemigo][x_enemigo + 1] == 0): #Si al lado derecho del enemigo es un pasillo:
                movimientosValidos.append('right') #Se puede mover hacia la derecha
                
            if (movimientosValidos): #Si hay movimientos válidos:
                movimiento = random.choice(movimientosValidos) #Elige un movimiento aleatorio de los movimientos válidos que tiene disponible
                if (movimiento == 'up'): #Si el movimiento válido es up
                    y_enemigo -= 1 #Mover hacia arriba
                elif (movimiento == 'down'): #Si el movimiento válido es down
                    y_enemigo += 1 #Mover hacia abajo
                elif (movimiento == 'left'): #Si el movimiento válido es left
                    x_enemigo -= 1 #Mover hacia la izquierda
                elif (movimiento == 'right'): #Si el movimiento válido es right
                    x_enemigo += 1 #Mover hacia la derecha
                posicionesEnemigos[i] = (y_enemigo, x_enemigo) #Actualizando la posición de cada enemigo con sus nuevas coordenadas
    
    def eliminar_enemigos_afectados(posicion_explosion, rango_explosion):
        enemigos_eliminados = []  #Lista para almacenar los índices de los enemigos eliminados (identificarlos)
        for i, (y_enemigo, x_enemigo) in enumerate(posicionesEnemigos): #Iterando sobre todas las posiciones de los enemigos. (índice de posición y coordenadas)
            if (abs(y_enemigo - posicion_explosion[0]) <= rango_explosion) and (abs(x_enemigo - posicion_explosion[1]) <= rango_explosion): #Si el enemigo está dentro del rango de la explosión:
                enemigos_eliminados.append(i)  #Agregar el índice del enemigo a la lista de eliminados
    
        # ---- Eliminar los enemigos afectados de la lista de posiciones de los enemigos ----
        for index in sorted(enemigos_eliminados, reverse=True): #Iterando sobre los enemigos eliminados (de índice mayor a menor para eliminar primero a los más cercanos a la explosión)
            del posicionesEnemigos[index] #Eliminando al enemigo (por su índice) de la lista que contiene las posiciones de los enemigos
    
    def dibujar_enemigos():
        enemigo_actual = 0  #Variable inicial que me permite alternar entre los tipos de enemigos
        for pos in posicionesEnemigos: #Iterando sobre cada posición de un enemigo (lista posicionesEnemigos)
            y, x = pos #Guardando las coordenadas de mi enemigo actual
            if ((y, x) in posicionesEnemigos): #Verificando si el enemigo está en la lista de posiciones
                # Dibujar el enemigo si aún está en la lista
                if (laberinto1[y][x] == 0): #Dibujar al enemigo si la posición del laberinto es un pasillo
                    if (enemigo_actual == 0): #Si mi enemigo está representado con el 0:
                        ventanaJuego.blit(imagenEnemigo1F, (x * tamañoBloques, y * tamañoBloques)) #Dibuja al enemigo 1
                    else: #De lo contrario (de ser un 1):
                        ventanaJuego.blit(imagenEnemigo2F, (x * tamañoBloques, y * tamañoBloques)) #Dibuja al enemigo 2
                    enemigo_actual = (enemigo_actual + 1) % 2 #Alterna entre los tipos de enemigos
    
    # ---- Definiendo Características del Jugador Principal ----
    # ---- Cargando las imágenes de vidas ----
    tresVidas = pygame.image.load("Imagenes//3vidas.png") #Agregando Imagen representativa de las tres vidas
    tresVidas = pygame.transform.scale(tresVidas, (150, 100)) #Ajustando el tamaño
    dosVidas = pygame.image.load("Imagenes//2vidas.png") #Agregando Imagen representativa de las dos vidas
    dosVidas = pygame.transform.scale(dosVidas, (150, 100)) #Ajustando el tamaño
    unaVida = pygame.image.load("Imagenes//1vida.png") #Agregando Imagen representativa de una vida
    unaVida = pygame.transform.scale(unaVida, (150, 100)) #Ajustando el tamaño
    ceroVidas = pygame.image.load("Imagenes//0vidas.png") #Agregando Imagen representativa de cero vidas
    ceroVidas = pygame.transform.scale(ceroVidas, (150, 100)) #Ajustando el tamaño
    
    # ---- Movimiento del Personaje ----
    posicionPrincipal = [(1, 10)] #Coordenadas iniciales del personaje principal
    direccion_movimiento = None  #Variable para almacenar la dirección del movimiento continuo (sin movimiento inicialmente)
    # ---- Definiendo Movimiento del Personaje Principal ----
    def movimientoPrincipal(laberinto1):
        movimientosValidos = [] #Lista que va a almacenar movimientos válidos del personaje principal
        for principal in range(len(posicionPrincipal)): #Recorriendo cada posición de la lista de posiciones del personaje principal
            y_principal, x_principal = posicionPrincipal[principal] #Guardando las nuevas coordenadas del personaje principal en X y Y
            # ---- Movimientos Válidos para el Personaje Principal ----
            if (laberinto1[y_principal - 1][x_principal] == 0):  #Verifica si el bloque de arriba es un 0 (pasillo)
                movimientosValidos.append('up') #Se puede mover hacia arriba
            if (laberinto1[y_principal + 1][x_principal] == 0):  #Verifica si el bloque de abajo es un 0 (pasillo)
                movimientosValidos.append('down') #Se puede mover hacia abajo
            if (laberinto1[y_principal][x_principal - 1] == 0):  #Verifica si el bloque de la izquierda es un 0 (pasillo)
                movimientosValidos.append('left') #Se puede mover hacia la izquierda
            if (laberinto1[y_principal][x_principal + 1] == 0):  #Verifica si el bloque de la derecha es un 0 (pasillo)
                movimientosValidos.append('right') #Se puede mover hacia la derecha
        return movimientosValidos  #Devuelve la lista de movimientos válidos
    
    # ---- Función para la pérdida de vidas ----
    vidasPrincipal = 3 #Cantidad de Vidas Iniciales del Personaje Principal
    def perdidaVidas():
        for enemigo in posicionesEnemigos: #Recorriendo a todos los enemigos por la lista (mapa)
            if (enemigo[0] == posicionPrincipal[0][0] and enemigo[1] == posicionPrincipal[0][1]): #Verificando que enemigo y principal se encuentren en la misma posición
                return True #Si hay colisión con un enemigo se retorna True
        return False #Si no hay colisión con ningún enemigo se retorna False
    
    # ---- Agregando imágen de la bomba ----
    imagenBomba = pygame.image.load("Imagenes//bomba.png") #Agregando imagen representativa de bomba
    imagenBomba = pygame.transform.scale(imagenBomba, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño

    # ---- Función para manejar la explosión de la bomba ----
    def explosion(y_bomba, x_bomba, visitado):
        ventanaJuego.blit(imagenBomba, (x_bomba * tamañoBloques, y_bomba * tamañoBloques)) #Dibujar la imágen de la bomba en la pantalla
        pygame.display.flip() #Actualizar la ventana
        sleep(1) #1 segundo para la explosión
        for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]: #Iterando alrededor de la posición de la bomba (arriba, abajo, izquierda, derecha)
            y = y_bomba + dy #Nueva coordenada en y de la bomba después de moverse al bloque destructible
            x = x_bomba + dx #Nueva coordenada en x de la bomba después de moverse al bloque destructible
            if (0 <= y < len(laberinto1) and 0 <= x < len(laberinto1[y])): #Si las coordenadas se encuentran dentro de los límites del laberinto:
                if (laberinto1[y][x] == 2 and (y, x) not in visitado): #Si el bloque es destructible y no ha sido visitado
                    visitado.add((y, x)) #Agregarlo como visitado (evitando que se visiten bloques que ya se explotaron)
                    laberinto1[y][x] = 0 #Convirtiendo el bloque destructible en un pasillo
                    explosion(y, x, visitado) #Realizando las explosiones en bloques adyacentes para propagarla
        eliminar_enemigos_afectados((y_bomba, x_bomba), 1) #Eliminando a los enemigos que están dentro del rango (1) de explosión

    # ---- Función para colocar una bomba ----
    def colocar_bomba():
        global contadorBombas #Declarando contadorBombas como global
        if (contadorBombas > 0): #Verificando si hay bombas disponibles
            contadorBombas -= 1 #Reduciendo la cantidad de bombas después de colocarla
            posicion_bomba = posicionPrincipal[0] #Guardando la posición actual del personaje principal
            explosion(posicion_bomba[0], posicion_bomba[1], set()) #Realizando la explosión de la bomba (set es un conjunto (optimizando))
            contarBombas(contadorBombas) #Actualizando el contador de bombas

    # ---- Verificar cantidad de Bombas ----
    tipografia = font.SysFont("Helvetica", 35, bold=True) #Definiendo nuevamente la tipografía modificada
    def contarBombas(contadorBombas):
        bomb = tipografia.render(str(contadorBombas), True, ("#FFFFFF")) #Mostrando y convirtiendo el contador de bombas a cadena antes de renderizarlo
        pygame.draw.rect(ventanaJuego, ("#000000"), (570, 655, 50, 40)) #Dibujando un rectángulo negro para cubrir el número anterior
        ventanaJuego.blit(bomb, (570, 655)) #Dibujando el nuevo número de bombas
        pygame.display.flip() #Actualizando la pantalla
        pygame.time.delay(1000) #Esperando 1 segundo para limitar la velocidad de actualización

    # ---- Variables para el temporizador ----
    tiempoInicio = pygame.time.get_ticks() #Obteniendo el tiempo (milisegundos) al inicio del nivel
    global tiempoTranscurrido #Globalizando la variable
    tiempoTranscurrido = 0 #Iniciando el tiempo transcurrido

    # ---- Bucle Ventana Juego 1 ----
    while True:
        for event in pygame.event.get(): #Iterando sobre eventos
            if (event.type == pygame.QUIT): #Si usuario intenta cerrar ventana
                pygame.quit() #Cerrando ventana
                sys.exit() #Saliendo del script Python por completo para detener el programa en su totalidad
            elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                if (event.button == 1): #Verificar si fue clic izquierdo
                    if (posicionRegreso.collidepoint(event.pos)): #Verificar si se presionó el botón de regreso
                        screenPrincipal(volumenGlobal) #Regresando a ventana principal
            elif (event.type == pygame.KEYDOWN): #Detectar teclas
                movimientosValidos = movimientoPrincipal(laberinto1) #Obteniendo los movimientos válidos del personaje principal
                if (event.key == pygame.K_w and 'up' in movimientosValidos): #Si se presiona w y up es un movimiento válido
                    posicionPrincipal[0] = (posicionPrincipal[0][0] - 1, posicionPrincipal[0][1]) #Mover hacia arriba
                elif (event.key == pygame.K_s and 'down' in movimientosValidos): #Si se presiona s y down es un movimiento válido
                    posicionPrincipal[0] = (posicionPrincipal[0][0] + 1, posicionPrincipal[0][1]) #Mover hacia abajo
                elif (event.key == pygame.K_a and 'left' in movimientosValidos): #Si se presiona a y left es un movimiento válido
                    posicionPrincipal[0] = (posicionPrincipal[0][0], posicionPrincipal[0][1] - 1) #Mover hacia la izquierda
                elif (event.key == pygame.K_d and 'right' in movimientosValidos): #Si se presiona d y right es un movimiento válido
                    posicionPrincipal[0] = (posicionPrincipal[0][0], posicionPrincipal[0][1] + 1) #Mover hacia la derecha
                elif (event.key  == pygame.K_SPACE): #Si se presiona la tecla espacio:
                    colocar_bomba() #Colocar la bomba
        
        # ---- Calculando el tiempo transcurrido en segundos ----
        tiempoActual = pygame.time.get_ticks() #Obteniendo el tiempo actual en milisegundos
        tiempoTranscurrido = (tiempoActual - tiempoInicio) // 1000 #Convertir a segundos
        # ---- Dibujando el temporizador en la ventana ----
        pygame.draw.rect(ventanaJuego, ("#000000"), (250, 655, 200, 50)) #Limpiando el área del temporizador
        tipografia_tiempo = font.SysFont("Helvetica", 30, bold=True) #Actualizando la tipografía
        texto_tiempo = tipografia_tiempo.render(f"Tiempo: {tiempoTranscurrido} s", True, ("#FFFFFF")) #Colocando los parámetros de mi tiempo
        ventanaJuego.blit(texto_tiempo, (250, 655)) #Mostrando en la ventana
        
        # ---- Dibujando las posesión de la llave ----
        if ((posicionPrincipal[0][0], posicionPrincipal[0][1]) == (fila_llave, columna_llave) and not tengoLlave): #Si la posición del principal es igual a la de la llave y no tengo la llave:
            tipografia = font.SysFont("Helvetica", 35, bold=True) #Actualizando la tipografía
            tengoLlave = tipografia.render("1", True, ("#FFFFFF")) #Definiendo parámetros de que tengo la llave
            pygame.draw.rect(ventanaJuego, ("#000000"), (730, 655, 30, 40)) #Cuadro negro para tapar lo dibujado anteriormente
            ventanaJuego.blit(tengoLlave, (730, 655)) #Mostrando en ventana que tengo la llave
            tengoLlave = True #Cambiando el valor, ahora sí tengo la llave
            if (tengoLlave == True): #Si tengo la llave:
                pygame.draw.rect(ventanaJuego, ("#AAAAAA"), (columna_llave * tamañoBloques, fila_llave * tamañoBloques, tamañoBloques, tamañoBloques)) #Dibuja un cuadro gris sobre ella para que nunca sea visible
        # ---- Verificar si el jugador tiene la llave y está alrededor de la puerta ----
        if tengoLlave and (((posicionPrincipal[0][0] - 1, posicionPrincipal[0][1]) == (fila_puerta, columna_puerta)) or
                        ((posicionPrincipal[0][0] + 1, posicionPrincipal[0][1]) == (fila_puerta, columna_puerta)) or
                        ((posicionPrincipal[0][0], posicionPrincipal[0][1] - 1) == (fila_puerta, columna_puerta)) or
                        ((posicionPrincipal[0][0], posicionPrincipal[0][1] + 1) == (fila_puerta, columna_puerta))):
            #Si el jugador tiene la llave y está alrededor de la puerta va al segundo nivel
            screenJuego2()
            break
        # ---- Movimiento continuo mientras se mantiene presionada una tecla ----
        if (direccion_movimiento): #Si se está manteniendo una tecla presionada:
            movimientosValidos = movimientoPrincipal(laberinto1) #Obtengo la lista de los movimientos válidos del personaje
            if (direccion_movimiento == 'up' and 'up' in movimientosValidos): #Si estoy presionando w y up es válido:
                posicionPrincipal[0] = (posicionPrincipal[0][0] - 1, posicionPrincipal[0][1]) #Moverse hacia arriba
            elif (direccion_movimiento == 'down' and 'down' in movimientosValidos): #Si estoy presionando s y down es válido:
                posicionPrincipal[0] = (posicionPrincipal[0][0] + 1, posicionPrincipal[0][1]) #Moverse hacia abajo
            elif (direccion_movimiento == 'left' and 'left' in movimientosValidos): #Si estoy presionando a y left es válido:
                posicionPrincipal[0] = (posicionPrincipal[0][0], posicionPrincipal[0][1] - 1) #Moverse hacia la izquierda
            elif (direccion_movimiento == 'right' and 'right' in movimientosValidos): #Si estoy presionando d y right es válido:
                posicionPrincipal[0] = (posicionPrincipal[0][0], posicionPrincipal[0][1] + 1) #Moverse hacia la derecha
        
        # ---- Verificando colisión con enemigos ----
        if (perdidaVidas()):
            vidasPrincipal -= 1  #Restando una vida al personaje principal si hay colisión con un enemigo
            if (vidasPrincipal == 0): #Si ya no se tienen vidas:
                screenDerrota() #Ir a ventana de derrota
                break #Saliendo del bucle de ventana juego 1 si se pierden todas las vidas
        
        # ---- Verificando no tener llave y no tener bombas a la vez ----
        if not tengoLlave and contadorBombas==0:
            screenDerrota() #Ir a ventana de derrota
            break #Saliendo del bucle principal del juego
        
        dibujandoLaberinto() #Dibujando laberinto
        ventanaJuego.blit(imagenPersonajePrincipal, (posicionPrincipal[0][1] * tamañoBloques, posicionPrincipal[0][0] * tamañoBloques)) #Dibujando la imagen del personaje principal según la skin seleccionada
        
        # ---- Dibujando las imágenes de las vidas ----
        if (vidasPrincipal == 3): #Si tengo tres vidas:
            ventanaJuego.blit(tresVidas, (780, 625)) #Mostrando en pantalla imágen representativa de las tres vidas
        elif (vidasPrincipal == 2): #Si tengo dos vidas:
            ventanaJuego.blit(dosVidas, (780, 625)) #Mostrando en pantalla imágen representativa de las dos vidas
        elif (vidasPrincipal == 1): #Si tengo una vida:
            ventanaJuego.blit(unaVida, (780, 625)) #Mostrando en pantalla imágen representativa de la vida
        elif (vidasPrincipal == 0): #Si tengo cero vidas:
            ventanaJuego.blit(ceroVidas, (780, 625)) #Mostrando en pantalla imágen representativa de las cero vidas
        
        dibujar_enemigos() #Dibujando a los enemigos
        movimientoEnemigos(laberinto1) #Actualizando posiciones de enemigos
        movimientoPrincipal(laberinto1) #Reflejando el movimiento del personaje principal
        pygame.display.flip() #Actualizando pantalla
        sleep (1/3) #Limitar la velocidad del juego
    return tiempoTranscurrido
# ----------------------------------- Finalizando la Ventana de Juego 1 -----------------------------------

# ----------------------------------- Iniciando la Ventana de Juego 2 -----------------------------------
skinSeleccionada = 1 #Skin predeterminada
def screenJuego2():
    mixer.init()
    pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el Volumen
    ventanaJuego = pygame.display.set_mode((950, 700)) #Creación de Ventana
    tamañoBloques = 50 #Tamaño de los bloques

    # ---- Agregando Imágenes de los Enemigos ----
    imagenEnemigo1F = pygame.image.load("Imagenes//Monstruo1_Nivel2.png") #Agregando Imágen de Monstruo 1 en nivel 1
    imagenEnemigo1F = pygame.transform.scale(imagenEnemigo1F, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    imagenEnemigo2F = pygame.image.load("Imagenes//Monstruo2_Nivel2.png") #Agregando Imágen de Monstruo 2 en nivel 1
    imagenEnemigo2F = pygame.transform.scale(imagenEnemigo2F, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    
    # ---- Definiendo las Posiciones Iniciales de los Enemigos ----
    posicionEnemigo1 = (11, 5)
    posicionEnemigo2 = (11, 12)
    posicionEnemigo3 = (9, 11)
    posicionEnemigo4 = (7, 5)
    posicionEnemigo5 = (6, 13)
    posicionEnemigo6 = (1, 6)
    posicionesEnemigos = [posicionEnemigo1, posicionEnemigo2, posicionEnemigo3, posicionEnemigo4, posicionEnemigo5, posicionEnemigo6] #Coordenadas iniciales de los enemigos
    
    # ---- Agregando Imágenes del Personaje Principal ----
    personaje1 = pygame.image.load("Imagenes//Skin1(Principal).png") #Agregando Imágen de Skin 1
    personaje1 = pygame.transform.scale(personaje1, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    personaje2 = pygame.image.load("Imagenes//Skin2(Principal).png") #Agregando Imágen de Skin 2
    personaje2 = pygame.transform.scale(personaje2, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    personaje3 = pygame.image.load("Imagenes//Skin3(Principal).png") #Agregando Imágen de Skin 3
    personaje3 = pygame.transform.scale(personaje3, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    
    # ---- Agregando el condicional para seleccionar la imagen correspondiente a la skin del personaje principal ----
    if (skinSeleccionada == 1):
        imagenPersonajePrincipal = personaje1
    elif (skinSeleccionada == 2):
        imagenPersonajePrincipal = personaje2
    elif (skinSeleccionada == 3):
        imagenPersonajePrincipal = personaje3
    
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes/BotonRegreso.png") #Agregando Imagen representativa del botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (40, 40)) #Ajustando el tamaño
    posicionRegreso = ventanaJuego.blit(botonRegreso, (10,655)) #Visualizar la imagen con su posición
    
    # ---- Cargar imágenes de bloques sólidos y destructibles ----
    imagenBloqueSolido = pygame.image.load("Imagenes//solid-bloque.png") #Agregando Imagen representativa de bloque sólido
    imagenBloqueSolido = pygame.transform.scale(imagenBloqueSolido, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño
    imagenBloqueDestructible = pygame.image.load("Imagenes//des-bloque.png") #Agregando Imagen representativa de bloque destructible
    imagenBloqueDestructible = pygame.transform.scale(imagenBloqueDestructible, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño
    
    # ---- Cargar imágenes de posesión de la llave ----
    poseerLlave = pygame.image.load("Imagenes//llave.png") #Agregando Imagen representativa para saber si se tiene la llave
    poseerLlave = pygame.transform.scale(poseerLlave, (100, 40)) #Ajustando el tamaño
    ventanaJuego.blit(poseerLlave, (640, 655)) #Visualizar la imagen con su posición
    tengoLlave = False #Inicialmente no tengo la llave
    tipografia = font.SysFont("Helvetica", 35, bold=True) #Actualizando la tipografía
    noTengoLlave = tipografia.render("0", True, ("#FFFFFF")) #Indicando parámetros para indicar que no tengo la llave
    ventanaJuego.blit(noTengoLlave, (730, 655)) #Reflejando que tengo 0 llaves
    
    # ---- Cargar imágen que cuenta las bombas ----
    bombasTotales = pygame.image.load("Imagenes//contadorBombas.png") #Agregando Imagen representativa de contador de bombas
    bombasTotales = pygame.transform.scale(bombasTotales, (100, 40)) #Ajustando el tamaño
    ventanaJuego.blit(bombasTotales, (470, 655)) #Visualizar la imagen con su posición
    global contadorBombas #Globalizando mi variable
    contadorBombas = 14 #Inicialmente tengo disponibles 14 bombas
    cantidadBomb = tipografia.render("14", True, ("#FFFFFF"))  #Indicando parámetros para indicar que tengo 14 bombas
    ventanaJuego.blit(cantidadBomb, (570, 655)) #Reflejando la cantidad de bombas
    
    # ---- Creando el Laberinto ----
    #El valor 0 son los pasillos
    #El valor 1 son los bloques sólidos
    #El valor 2 son los bloques destructibles
    #El valor 3 es la puerta
    laberinto1= [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,2,2,1,0,0,1,1,0,0,1,0,0,2,1,0,0,1],
                [1,0,2,0,2,1,0,0,2,0,2,0,0,2,1,0,1,2,1],
                [1,1,1,3,0,1,0,0,1,0,1,0,1,1,0,0,2,0,1],
                [1,0,2,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1],
                [1,0,2,0,1,0,2,1,0,1,0,0,1,2,0,2,1,0,1],
                [1,2,1,1,0,1,0,0,0,1,2,0,0,2,1,0,1,1,1],
                [1,2,0,1,0,0,0,1,0,0,1,2,0,0,1,2,0,2,1],
                [1,1,0,1,0,1,2,2,0,0,0,1,0,2,0,0,0,0,1],
                [1,0,2,0,0,0,0,2,0,2,0,1,0,1,0,1,1,2,1],
                [1,0,2,1,1,0,0,1,2,1,2,0,2,2,0,2,1,0,1],
                [1,1,0,2,0,0,0,0,2,0,1,0,1,0,0,0,1,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    
    # ---- Imágen de LLave ----
    imagenLlave = pygame.image.load("Imagenes//llave.png") #Agregando Imagen representativa de la llave
    imagenLlave = pygame.transform.scale(imagenLlave, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño
    # ---- Definiendo la posición de la llave de forma aleatoria ----
    fila_llave, columna_llave = random.choice([(fila, columna) for fila in range(len(laberinto1)) #Generando lista de todas las coordenadas donde (fila, columna) sea 2
                                                for columna in range(len(laberinto1[0])) #0 es por el primer elemento de la fila
                                                if laberinto1[fila][columna] == 2])
    
    # ---- Dibujando el Laberinto ----
    def dibujandoLaberinto():
        for fila in range(len(laberinto1)): #Recorriendo desde fila 0 hasta el final de la fila
            for columna in range(len(laberinto1[0])): #Recorriendo desde columna 0 hasta el final de la columna
                if (laberinto1[fila][columna] == 0): #Condición si hay un 0 en el laberinto
                    pygame.draw.rect(ventanaJuego, ("#808080"), (columna*tamañoBloques, fila*tamañoBloques, tamañoBloques, tamañoBloques)) #Agregando Pasillos
                elif (laberinto1[fila][columna] == 1): #Condición si hay un 1 en el laberinto
                    ventanaJuego.blit(imagenBloqueSolido, (columna*tamañoBloques, fila*tamañoBloques)) #Agregando imágen de bloque sólido
                elif (laberinto1[fila][columna] == 2): #Condición si hay un 2 en el laberinto
                    ventanaJuego.blit(imagenBloqueDestructible, (columna*tamañoBloques, fila*tamañoBloques)) #Agregando imágen de bloque destructible
                elif (laberinto1[fila][columna] == 3): #Condición si hay un 3 en el laberinto
                    imagenPuerta = pygame.image.load("Imagenes//puerta.png") #Agregando imágen de puerta
                    imagenPuerta = pygame.transform.scale(imagenPuerta, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño
                    ventanaJuego.blit(imagenPuerta, (columna*tamañoBloques, fila*tamañoBloques)) #Visualizar la imagen con su posición
                    global fila_puerta, columna_puerta #Globalizando las coordenadas con la fila y la columna de la posición de la puerta
                    fila_puerta, columna_puerta = fila, columna
    
    # ---- Definiendo el Movimiento de los enemigos ----
    def movimientoEnemigos(laberinto1):
        for i, (y_enemigo, x_enemigo) in enumerate(posicionesEnemigos): #Iterando sobre todas las posiciones de los enemigos. (índice de posición y coordenadas)
            movimientosValidos = [] #Inicializando lista vacía que va a guardar los movimientos validos de mis enemigos
            if (laberinto1[y_enemigo - 1][x_enemigo] == 0): #Si arriba del enemigo es un pasillo:
                movimientosValidos.append('up') #Se puede mover hacia arriba
            if (laberinto1[y_enemigo + 1][x_enemigo] == 0): #Si abajo del enemigo es un pasillo:
                movimientosValidos.append('down') #Se puede mover hacia abajo
            if (laberinto1[y_enemigo][x_enemigo - 1] == 0): #Si al lado izquierdo del enemigo es un pasillo:
                movimientosValidos.append('left') #Se puede mover hacia la izquierda
            if (laberinto1[y_enemigo][x_enemigo + 1] == 0): #Si al lado derecho del enemigo es un pasillo:
                movimientosValidos.append('right') #Se puede mover hacia la derecha
                
            if (movimientosValidos): #Si hay movimientos válidos:
                movimiento = random.choice(movimientosValidos) #Elige un movimiento aleatorio de los movimientos válidos que tiene disponible
                if (movimiento == 'up'): #Si el movimiento válido es up
                    y_enemigo -= 1 #Mover hacia arriba
                elif (movimiento == 'down'): #Si el movimiento válido es down
                    y_enemigo += 1 #Mover hacia abajo
                elif (movimiento == 'left'): #Si el movimiento válido es left
                    x_enemigo -= 1 #Mover hacia la izquierda
                elif (movimiento == 'right'): #Si el movimiento válido es right
                    x_enemigo += 1 #Mover hacia la derecha
                posicionesEnemigos[i] = (y_enemigo, x_enemigo) #Actualizando la posición de cada enemigo con sus nuevas coordenadas
    
    def eliminar_enemigos_afectados(posicion_explosion, rango_explosion):
        enemigos_eliminados = []  #Lista para almacenar los índices de los enemigos eliminados (identificarlos)
        for i, (y_enemigo, x_enemigo) in enumerate(posicionesEnemigos): #Iterando sobre todas las posiciones de los enemigos. (índice de posición y coordenadas)
            if (abs(y_enemigo - posicion_explosion[0]) <= rango_explosion) and (abs(x_enemigo - posicion_explosion[1]) <= rango_explosion): #Si el enemigo está dentro del rango de la explosión:
                enemigos_eliminados.append(i)  #Agregar el índice del enemigo a la lista de eliminados
    
        # ---- Eliminar los enemigos afectados de la lista de posiciones de los enemigos ----
        for index in sorted(enemigos_eliminados, reverse=True): #Iterando sobre los enemigos eliminados (de índice mayor a menor para eliminar primero a los más cercanos a la explosión)
            del posicionesEnemigos[index] #Eliminando al enemigo (por su índice) de la lista que contiene las posiciones de los enemigos
    
    def dibujar_enemigos():
        enemigo_actual = 0  #Variable inicial que me permite alternar entre los tipos de enemigos
        for pos in posicionesEnemigos: #Iterando sobre cada posición de un enemigo (lista posicionesEnemigos)
            y, x = pos #Guardando las coordenadas de mi enemigo actual
            if ((y, x) in posicionesEnemigos): #Verificando si el enemigo está en la lista de posiciones
                # Dibujar el enemigo si aún está en la lista
                if (laberinto1[y][x] == 0): #Dibujar al enemigo si la posición del laberinto es un pasillo
                    if (enemigo_actual == 0): #Si mi enemigo está representado con el 0:
                        ventanaJuego.blit(imagenEnemigo1F, (x * tamañoBloques, y * tamañoBloques)) #Dibuja al enemigo 1
                    else: #De lo contrario (de ser un 1):
                        ventanaJuego.blit(imagenEnemigo2F, (x * tamañoBloques, y * tamañoBloques)) #Dibuja al enemigo 2
                    enemigo_actual = (enemigo_actual + 1) % 2 #Alterna entre los tipos de enemigos
    
    # ---- Definiendo Características del Jugador Principal ----
    # ---- Cargando las imágenes de vidas ----
    tresVidas = pygame.image.load("Imagenes//3vidas.png") #Agregando Imagen representativa de las tres vidas
    tresVidas = pygame.transform.scale(tresVidas, (150, 100)) #Ajustando el tamaño
    dosVidas = pygame.image.load("Imagenes//2vidas.png") #Agregando Imagen representativa de las dos vidas
    dosVidas = pygame.transform.scale(dosVidas, (150, 100)) #Ajustando el tamaño
    unaVida = pygame.image.load("Imagenes//1vida.png") #Agregando Imagen representativa de una vida
    unaVida = pygame.transform.scale(unaVida, (150, 100)) #Ajustando el tamaño
    ceroVidas = pygame.image.load("Imagenes//0vidas.png") #Agregando Imagen representativa de cero vidas
    ceroVidas = pygame.transform.scale(ceroVidas, (150, 100)) #Ajustando el tamaño
    
    # ---- Movimiento del Personaje ----
    posicionPrincipal = [(1, 10)] #Coordenadas iniciales del personaje principal
    direccion_movimiento = None  #Variable para almacenar la dirección del movimiento continuo (sin movimiento inicialmente)
    # ---- Definiendo Movimiento del Personaje Principal ----
    def movimientoPrincipal(laberinto1):
        movimientosValidos = [] #Lista que va a almacenar movimientos válidos del personaje principal
        for principal in range(len(posicionPrincipal)): #Recorriendo cada posición de la lista de posiciones del personaje principal
            y_principal, x_principal = posicionPrincipal[principal] #Guardando las nuevas coordenadas del personaje principal en X y Y
            # ---- Movimientos Válidos para el Personaje Principal ----
            if (laberinto1[y_principal - 1][x_principal] == 0):  #Verifica si el bloque de arriba es un 0 (pasillo)
                movimientosValidos.append('up') #Se puede mover hacia arriba
            if (laberinto1[y_principal + 1][x_principal] == 0):  #Verifica si el bloque de abajo es un 0 (pasillo)
                movimientosValidos.append('down') #Se puede mover hacia abajo
            if (laberinto1[y_principal][x_principal - 1] == 0):  #Verifica si el bloque de la izquierda es un 0 (pasillo)
                movimientosValidos.append('left') #Se puede mover hacia la izquierda
            if (laberinto1[y_principal][x_principal + 1] == 0):  #Verifica si el bloque de la derecha es un 0 (pasillo)
                movimientosValidos.append('right') #Se puede mover hacia la derecha
        return movimientosValidos  #Devuelve la lista de movimientos válidos
    
    # ---- Función para la pérdida de vidas ----
    vidasPrincipal = 3 #Cantidad de Vidas Iniciales del Personaje Principal
    def perdidaVidas():
        for enemigo in posicionesEnemigos: #Recorriendo a todos los enemigos por la lista (mapa)
            if (enemigo[0] == posicionPrincipal[0][0] and enemigo[1] == posicionPrincipal[0][1]): #Verificando que enemigo y principal se encuentren en la misma posición
                return True #Si hay colisión con un enemigo se retorna True
        return False #Si no hay colisión con ningún enemigo se retorna False
    
    # ---- Agregando imágen de la bomba ----
    imagenBomba = pygame.image.load("Imagenes//bomba.png") #Agregando imagen representativa de bomba
    imagenBomba = pygame.transform.scale(imagenBomba, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño

    # ---- Función para manejar la explosión de la bomba ----
    def explosion(y_bomba, x_bomba, visitado):
        ventanaJuego.blit(imagenBomba, (x_bomba * tamañoBloques, y_bomba * tamañoBloques)) #Dibujar la imágen de la bomba en la pantalla
        pygame.display.flip() #Actualizar la ventana
        sleep(1) #1 segundo para la explosión
        for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]: #Iterando alrededor de la posición de la bomba (arriba, abajo, izquierda, derecha)
            y = y_bomba + dy #Nueva coordenada en y de la bomba después de moverse al bloque destructible
            x = x_bomba + dx #Nueva coordenada en x de la bomba después de moverse al bloque destructible
            if (0 <= y < len(laberinto1) and 0 <= x < len(laberinto1[y])): #Si las coordenadas se encuentran dentro de los límites del laberinto:
                if (laberinto1[y][x] == 2 and (y, x) not in visitado): #Si el bloque es destructible y no ha sido visitado
                    visitado.add((y, x)) #Agregarlo como visitado (evitando que se visiten bloques que ya se explotaron)
                    laberinto1[y][x] = 0 #Convirtiendo el bloque destructible en un pasillo
                    explosion(y, x, visitado) #Realizando las explosiones en bloques adyacentes para propagarla
        eliminar_enemigos_afectados((y_bomba, x_bomba), 1) #Eliminando a los enemigos que están dentro del rango (1) de explosión

    # ---- Función para colocar una bomba ----
    def colocar_bomba():
        global contadorBombas #Declarando contadorBombas como global
        if (contadorBombas > 0): #Verificando si hay bombas disponibles
            contadorBombas -= 1 #Reduciendo la cantidad de bombas después de colocarla
            posicion_bomba = posicionPrincipal[0] #Guardando la posición actual del personaje principal
            explosion(posicion_bomba[0], posicion_bomba[1], set()) #Realizando la explosión de la bomba (set es un conjunto (optimizando))
            contarBombas(contadorBombas) #Actualizando el contador de bombas

    # ---- Verificar cantidad de Bombas ----
    tipografia = font.SysFont("Helvetica", 35, bold=True) #Definiendo nuevamente la tipografía modificada
    def contarBombas(contadorBombas):
        bomb = tipografia.render(str(contadorBombas), True, ("#FFFFFF")) #Mostrando y convirtiendo el contador de bombas a cadena antes de renderizarlo
        pygame.draw.rect(ventanaJuego, ("#000000"), (570, 655, 50, 40)) #Dibujando un rectángulo negro para cubrir el número anterior
        ventanaJuego.blit(bomb, (570, 655)) #Dibujando el nuevo número de bombas
        pygame.display.flip() #Actualizando la pantalla
        pygame.time.delay(1000) #Esperando 1 segundo para limitar la velocidad de actualización
        
    tiempoInicialSegundoNivel = pygame.time.get_ticks() #Obteniendo el tiempo inicial al abrir mi segunda ventana
    global tiempoTotal
    # ---- Bucle Ventana Juego 2 ----
    while True:
        for event in pygame.event.get(): #Iterando sobre eventos
            if (event.type == pygame.QUIT): #Si usuario intenta cerrar ventana
                pygame.quit() #Cerrando ventana
                sys.exit() #Saliendo del script Python por completo para detener el programa en su totalidad
            elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                if (event.button == 1): #Verificar si fue clic izquierdo
                    if (posicionRegreso.collidepoint(event.pos)): #Verificar si se presionó el botón de regreso
                        screenPrincipal(volumenGlobal) #Regresando a ventana principal
            elif (event.type == pygame.KEYDOWN): #Detectar teclas
                movimientosValidos = movimientoPrincipal(laberinto1) #Obteniendo los movimientos válidos del personaje principal
                if (event.key == pygame.K_w and 'up' in movimientosValidos): #Si se presiona w y up es un movimiento válido
                    posicionPrincipal[0] = (posicionPrincipal[0][0] - 1, posicionPrincipal[0][1]) #Mover hacia arriba
                elif (event.key == pygame.K_s and 'down' in movimientosValidos): #Si se presiona s y down es un movimiento válido
                    posicionPrincipal[0] = (posicionPrincipal[0][0] + 1, posicionPrincipal[0][1]) #Mover hacia abajo
                elif (event.key == pygame.K_a and 'left' in movimientosValidos): #Si se presiona a y left es un movimiento válido
                    posicionPrincipal[0] = (posicionPrincipal[0][0], posicionPrincipal[0][1] - 1) #Mover hacia la izquierda
                elif (event.key == pygame.K_d and 'right' in movimientosValidos): #Si se presiona d y right es un movimiento válido
                    posicionPrincipal[0] = (posicionPrincipal[0][0], posicionPrincipal[0][1] + 1) #Mover hacia la derecha
                elif (event.key  == pygame.K_SPACE): #Si se presiona la tecla espacio:
                    colocar_bomba() #Colocar la bomba
        
        # ---- Llamando al Tiempo Transcurrido desde nivel 1 ----
        # ---- Calculando el tiempo transcurrido en segundos ----
        tiempoActual = pygame.time.get_ticks() #Obteniendo tiempo actual
        tiempoTranscurridoSegundaVentana = (tiempoActual - tiempoInicialSegundoNivel)//1000 # Calcula el tiempo transcurrido (milisegundos) en la segunda ventana
        tiempoTotal = tiempoTranscurrido + tiempoTranscurridoSegundaVentana  # Calcula el tiempo total transcurrido desde el inicio del juego
        # ---- Dibujando el temporizador en la ventana ----
        pygame.draw.rect(ventanaJuego, ("#000000"), (250, 655, 200, 50)) #Limpiando el área del temporizador
        tipografia_tiempo = font.SysFont("Helvetica", 30, bold=True) #Actualizando la tipografía
        texto_tiempo = tipografia_tiempo.render(f"Tiempo: {tiempoTotal} s", True, ("#FFFFFF")) #Colocando los parámetros de mi tiempo
        ventanaJuego.blit(texto_tiempo, (250, 655)) #Mostrando en la ventana
        
        # ---- Dibujando las posesión de la llave ----
        if ((posicionPrincipal[0][0], posicionPrincipal[0][1]) == (fila_llave, columna_llave) and not tengoLlave): #Si la posición del principal es igual a la de la llave y no tengo la llave:
            tipografia = font.SysFont("Helvetica", 35, bold=True) #Actualizando la tipografía
            tengoLlave = tipografia.render("1", True, ("#FFFFFF")) #Definiendo parámetros de que tengo la llave
            pygame.draw.rect(ventanaJuego, ("#000000"), (730, 655, 30, 40)) #Cuadro negro para tapar lo dibujado anteriormente
            ventanaJuego.blit(tengoLlave, (730, 655)) #Mostrando en ventana que tengo la llave
            tengoLlave = True #Cambiando el valor, ahora sí tengo la llave
            if (tengoLlave == True): #Si tengo la llave:
                pygame.draw.rect(ventanaJuego, ("#808080"), (columna_llave * tamañoBloques, fila_llave * tamañoBloques, tamañoBloques, tamañoBloques)) #Dibuja un cuadro gris sobre ella para que nunca sea visible
        # ---- Verificar si el jugador tiene la llave y está alrededor de la puerta ----
        if tengoLlave and (((posicionPrincipal[0][0] - 1, posicionPrincipal[0][1]) == (fila_puerta, columna_puerta)) or
                        ((posicionPrincipal[0][0] + 1, posicionPrincipal[0][1]) == (fila_puerta, columna_puerta)) or
                        ((posicionPrincipal[0][0], posicionPrincipal[0][1] - 1) == (fila_puerta, columna_puerta)) or
                        ((posicionPrincipal[0][0], posicionPrincipal[0][1] + 1) == (fila_puerta, columna_puerta))):
            #Si el jugador tiene la llave y está alrededor de la puerta va al segundo nivel
            screenJuego3()
            break
        # ---- Movimiento continuo mientras se mantiene presionada una tecla ----
        if (direccion_movimiento): #Si se está manteniendo una tecla presionada:
            movimientosValidos = movimientoPrincipal(laberinto1) #Obtengo la lista de los movimientos válidos del personaje
            if (direccion_movimiento == 'up' and 'up' in movimientosValidos): #Si estoy presionando w y up es válido:
                posicionPrincipal[0] = (posicionPrincipal[0][0] - 1, posicionPrincipal[0][1]) #Moverse hacia arriba
            elif (direccion_movimiento == 'down' and 'down' in movimientosValidos): #Si estoy presionando s y down es válido:
                posicionPrincipal[0] = (posicionPrincipal[0][0] + 1, posicionPrincipal[0][1]) #Moverse hacia abajo
            elif (direccion_movimiento == 'left' and 'left' in movimientosValidos): #Si estoy presionando a y left es válido:
                posicionPrincipal[0] = (posicionPrincipal[0][0], posicionPrincipal[0][1] - 1) #Moverse hacia la izquierda
            elif (direccion_movimiento == 'right' and 'right' in movimientosValidos): #Si estoy presionando d y right es válido:
                posicionPrincipal[0] = (posicionPrincipal[0][0], posicionPrincipal[0][1] + 1) #Moverse hacia la derecha
        
        # ---- Verificando colisión con enemigos ----
        if (perdidaVidas()):
            vidasPrincipal -= 1  #Restando una vida al personaje principal si hay colisión con un enemigo
            if (vidasPrincipal == 0): #Si ya no se tienen vidas:
                screenDerrota() #Ir a ventana de derrota
                break #Saliendo del bucle de ventana juego 1 si se pierden todas las vidas
        
        # ---- Verificando no tener llave y no tener bombas a la vez ----
        if not tengoLlave and contadorBombas==0:
            screenDerrota() #Ir a ventana de derrota
            break #Saliendo del bucle principal del juego
        
        dibujandoLaberinto() #Dibujando laberinto
        ventanaJuego.blit(imagenPersonajePrincipal, (posicionPrincipal[0][1] * tamañoBloques, posicionPrincipal[0][0] * tamañoBloques)) #Dibujando la imagen del personaje principal según la skin seleccionada
        
        # ---- Dibujando las imágenes de las vidas ----
        if (vidasPrincipal == 3): #Si tengo tres vidas:
            ventanaJuego.blit(tresVidas, (780, 625)) #Mostrando en pantalla imágen representativa de las tres vidas
        elif (vidasPrincipal == 2): #Si tengo dos vidas:
            ventanaJuego.blit(dosVidas, (780, 625)) #Mostrando en pantalla imágen representativa de las dos vidas
        elif (vidasPrincipal == 1): #Si tengo una vida:
            ventanaJuego.blit(unaVida, (780, 625)) #Mostrando en pantalla imágen representativa de la vida
        elif (vidasPrincipal == 0): #Si tengo cero vidas:
            ventanaJuego.blit(ceroVidas, (780, 625)) #Mostrando en pantalla imágen representativa de las cero vidas
        
        dibujar_enemigos() #Dibujando a los enemigos
        movimientoEnemigos(laberinto1) #Actualizando posiciones de enemigos
        movimientoPrincipal(laberinto1) #Reflejando el movimiento del personaje principal
        pygame.display.flip() #Actualizando pantalla
        sleep (1/3) #Limitar la velocidad del juego
    return tiempoTotal
# ----------------------------------- Finalizando la Ventana de Juego 2 -----------------------------------

# ----------------------------------- Iniciando la Ventana de Juego 3 -----------------------------------
skinSeleccionada = 1 #Skin predeterminada
def screenJuego3():
    mixer.init()
    pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el Volumen
    ventanaJuego = pygame.display.set_mode((950, 700)) #Creación de Ventana
    tamañoBloques = 50 #Tamaño de los bloques

    # ---- Agregando Imágenes de los Enemigos ----
    imagenEnemigo1F = pygame.image.load("Imagenes//Monstruo1_Nivel3.png") #Agregando Imágen de Monstruo 1 en nivel 1
    imagenEnemigo1F = pygame.transform.scale(imagenEnemigo1F, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    imagenEnemigo2F = pygame.image.load("Imagenes//Monstruo2_Nivel3.png") #Agregando Imágen de Monstruo 2 en nivel 1
    imagenEnemigo2F = pygame.transform.scale(imagenEnemigo2F, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    
    # ---- Definiendo las Posiciones Iniciales de los Enemigos ----
    posicionEnemigo1 = (11, 1)
    posicionEnemigo2 = (11, 14)
    posicionEnemigo3 = (1, 5)
    posicionEnemigo4 = (2, 3)
    posicionEnemigo5 = (3, 15)
    posicionEnemigo6 = (8, 9)
    posicionEnemigo7 = (8, 17)
    posicionEnemigo8 = (7, 12)
    posicionesEnemigos = [posicionEnemigo1, posicionEnemigo2, posicionEnemigo3, posicionEnemigo4, posicionEnemigo5, posicionEnemigo6, posicionEnemigo7, posicionEnemigo8] #Coordenadas iniciales de los enemigos
    
    # ---- Agregando Imágenes del Personaje Principal ----
    personaje1 = pygame.image.load("Imagenes//Skin1(Principal).png") #Agregando Imágen de Skin 1
    personaje1 = pygame.transform.scale(personaje1, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    personaje2 = pygame.image.load("Imagenes//Skin2(Principal).png") #Agregando Imágen de Skin 2
    personaje2 = pygame.transform.scale(personaje2, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    personaje3 = pygame.image.load("Imagenes//Skin3(Principal).png") #Agregando Imágen de Skin 3
    personaje3 = pygame.transform.scale(personaje3, (tamañoBloques, tamañoBloques)) #Ajustando tamaño
    
    # ---- Agregando el condicional para seleccionar la imagen correspondiente a la skin del personaje principal ----
    if (skinSeleccionada == 1):
        imagenPersonajePrincipal = personaje1
    elif (skinSeleccionada == 2):
        imagenPersonajePrincipal = personaje2
    elif (skinSeleccionada == 3):
        imagenPersonajePrincipal = personaje3
    
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes/BotonRegreso.png") #Agregando Imagen representativa del botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (40, 40)) #Ajustando el tamaño
    posicionRegreso = ventanaJuego.blit(botonRegreso, (10,655)) #Visualizar la imagen con su posición
    
    # ---- Cargar imágenes de bloques sólidos y destructibles ----
    imagenBloqueSolido = pygame.image.load("Imagenes//solid-bloque.png") #Agregando Imagen representativa de bloque sólido
    imagenBloqueSolido = pygame.transform.scale(imagenBloqueSolido, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño
    imagenBloqueDestructible = pygame.image.load("Imagenes//des-bloque.png") #Agregando Imagen representativa de bloque destructible
    imagenBloqueDestructible = pygame.transform.scale(imagenBloqueDestructible, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño
    
    # ---- Cargar imágenes de posesión de la llave ----
    poseerLlave = pygame.image.load("Imagenes//llave.png") #Agregando Imagen representativa para saber si se tiene la llave
    poseerLlave = pygame.transform.scale(poseerLlave, (100, 40)) #Ajustando el tamaño
    ventanaJuego.blit(poseerLlave, (640, 655)) #Visualizar la imagen con su posición
    tengoLlave = False #Inicialmente no tengo la llave
    tipografia = font.SysFont("Helvetica", 35, bold=True) #Actualizando la tipografía
    noTengoLlave = tipografia.render("0", True, ("#FFFFFF")) #Indicando parámetros para indicar que no tengo la llave
    ventanaJuego.blit(noTengoLlave, (730, 655)) #Reflejando que tengo 0 llaves
    
    # ---- Cargar imágen que cuenta las bombas ----
    bombasTotales = pygame.image.load("Imagenes//contadorBombas.png") #Agregando Imagen representativa de contador de bombas
    bombasTotales = pygame.transform.scale(bombasTotales, (100, 40)) #Ajustando el tamaño
    ventanaJuego.blit(bombasTotales, (470, 655)) #Visualizar la imagen con su posición
    global contadorBombas #Globalizando mi variable
    contadorBombas = 12 #Inicialmente tengo disponibles 12 bombas
    cantidadBomb = tipografia.render("12", True, ("#FFFFFF"))  #Indicando parámetros para indicar que tengo 12 bombas
    ventanaJuego.blit(cantidadBomb, (570, 655)) #Reflejando la cantidad de bombas
    
    # ---- Creando el Laberinto ----
    #El valor 0 son los pasillos
    #El valor 1 son los bloques sólidos
    #El valor 2 son los bloques destructibles
    #El valor 3 es la puerta
    laberinto1= [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,2,2,1,0,0,1,1,0,0,1,0,0,2,1,0,0,1],
                [1,0,2,0,0,0,2,1,2,0,2,0,0,2,1,0,1,0,1],
                [1,1,0,0,0,1,1,2,0,0,1,0,1,1,0,0,2,1,1],
                [1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1],
                [1,0,2,0,1,0,2,1,0,0,1,0,1,2,0,2,1,0,1],
                [1,2,1,2,0,1,0,0,0,1,2,0,0,2,1,0,0,1,1],
                [1,2,1,1,0,0,0,1,0,0,1,2,0,0,1,2,0,2,1],
                [1,1,0,0,0,1,0,2,0,0,0,1,0,2,0,0,0,0,1],
                [1,0,0,2,0,0,1,2,0,2,0,1,0,1,0,1,1,2,1],
                [1,0,2,1,1,0,0,1,2,1,2,0,2,2,0,2,1,0,1],
                [1,0,0,1,0,2,2,1,2,3,1,0,1,0,0,0,2,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    
    # ---- Imágen de LLave ----
    imagenLlave = pygame.image.load("Imagenes//llave.png") #Agregando Imagen representativa de la llave
    imagenLlave = pygame.transform.scale(imagenLlave, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño
    # ---- Definiendo la posición de la llave de forma aleatoria ----
    fila_llave, columna_llave = random.choice([(fila, columna) for fila in range(len(laberinto1)) #Generando lista de todas las coordenadas donde (fila, columna) sea 2
                                                for columna in range(len(laberinto1[0])) #0 es por el primer elemento de la fila
                                                if laberinto1[fila][columna] == 2])
    
    # ---- Dibujando el Laberinto ----
    def dibujandoLaberinto():
        for fila in range(len(laberinto1)): #Recorriendo desde fila 0 hasta el final de la fila
            for columna in range(len(laberinto1[0])): #Recorriendo desde columna 0 hasta el final de la columna
                if (laberinto1[fila][columna] == 0): #Condición si hay un 0 en el laberinto
                    pygame.draw.rect(ventanaJuego, ("#1D1D1D"), (columna*tamañoBloques, fila*tamañoBloques, tamañoBloques, tamañoBloques)) #Agregando Pasillos
                elif (laberinto1[fila][columna] == 1): #Condición si hay un 1 en el laberinto
                    ventanaJuego.blit(imagenBloqueSolido, (columna*tamañoBloques, fila*tamañoBloques)) #Agregando imágen de bloque sólido
                elif (laberinto1[fila][columna] == 2): #Condición si hay un 2 en el laberinto
                    ventanaJuego.blit(imagenBloqueDestructible, (columna*tamañoBloques, fila*tamañoBloques)) #Agregando imágen de bloque destructible
                elif (laberinto1[fila][columna] == 3): #Condición si hay un 3 en el laberinto
                    imagenPuerta = pygame.image.load("Imagenes//puerta.png") #Agregando imágen de puerta
                    imagenPuerta = pygame.transform.scale(imagenPuerta, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño
                    ventanaJuego.blit(imagenPuerta, (columna*tamañoBloques, fila*tamañoBloques)) #Visualizar la imagen con su posición
                    global fila_puerta, columna_puerta #Globalizando las coordenadas con la fila y la columna de la posición de la puerta
                    fila_puerta, columna_puerta = fila, columna
    
    # ---- Definiendo el Movimiento de los enemigos ----
    def movimientoEnemigos(laberinto1):
        for i, (y_enemigo, x_enemigo) in enumerate(posicionesEnemigos): #Iterando sobre todas las posiciones de los enemigos. (índice de posición y coordenadas)
            movimientosValidos = [] #Inicializando lista vacía que va a guardar los movimientos validos de mis enemigos
            if (laberinto1[y_enemigo - 1][x_enemigo] == 0): #Si arriba del enemigo es un pasillo:
                movimientosValidos.append('up') #Se puede mover hacia arriba
            if (laberinto1[y_enemigo + 1][x_enemigo] == 0): #Si abajo del enemigo es un pasillo:
                movimientosValidos.append('down') #Se puede mover hacia abajo
            if (laberinto1[y_enemigo][x_enemigo - 1] == 0): #Si al lado izquierdo del enemigo es un pasillo:
                movimientosValidos.append('left') #Se puede mover hacia la izquierda
            if (laberinto1[y_enemigo][x_enemigo + 1] == 0): #Si al lado derecho del enemigo es un pasillo:
                movimientosValidos.append('right') #Se puede mover hacia la derecha
                
            if (movimientosValidos): #Si hay movimientos válidos:
                movimiento = random.choice(movimientosValidos) #Elige un movimiento aleatorio de los movimientos válidos que tiene disponible
                if (movimiento == 'up'): #Si el movimiento válido es up
                    y_enemigo -= 1 #Mover hacia arriba
                elif (movimiento == 'down'): #Si el movimiento válido es down
                    y_enemigo += 1 #Mover hacia abajo
                elif (movimiento == 'left'): #Si el movimiento válido es left
                    x_enemigo -= 1 #Mover hacia la izquierda
                elif (movimiento == 'right'): #Si el movimiento válido es right
                    x_enemigo += 1 #Mover hacia la derecha
                posicionesEnemigos[i] = (y_enemigo, x_enemigo) #Actualizando la posición de cada enemigo con sus nuevas coordenadas
    
    def eliminar_enemigos_afectados(posicion_explosion, rango_explosion):
        enemigos_eliminados = []  #Lista para almacenar los índices de los enemigos eliminados (identificarlos)
        for i, (y_enemigo, x_enemigo) in enumerate(posicionesEnemigos): #Iterando sobre todas las posiciones de los enemigos. (índice de posición y coordenadas)
            if (abs(y_enemigo - posicion_explosion[0]) <= rango_explosion) and (abs(x_enemigo - posicion_explosion[1]) <= rango_explosion): #Si el enemigo está dentro del rango de la explosión:
                enemigos_eliminados.append(i)  #Agregar el índice del enemigo a la lista de eliminados
    
        # ---- Eliminar los enemigos afectados de la lista de posiciones de los enemigos ----
        for index in sorted(enemigos_eliminados, reverse=True): #Iterando sobre los enemigos eliminados (de índice mayor a menor para eliminar primero a los más cercanos a la explosión)
            del posicionesEnemigos[index] #Eliminando al enemigo (por su índice) de la lista que contiene las posiciones de los enemigos
    
    def dibujar_enemigos():
        enemigo_actual = 0  #Variable inicial que me permite alternar entre los tipos de enemigos
        for pos in posicionesEnemigos: #Iterando sobre cada posición de un enemigo (lista posicionesEnemigos)
            y, x = pos #Guardando las coordenadas de mi enemigo actual
            if ((y, x) in posicionesEnemigos): #Verificando si el enemigo está en la lista de posiciones
                # Dibujar el enemigo si aún está en la lista
                if (laberinto1[y][x] == 0): #Dibujar al enemigo si la posición del laberinto es un pasillo
                    if (enemigo_actual == 0): #Si mi enemigo está representado con el 0:
                        ventanaJuego.blit(imagenEnemigo1F, (x * tamañoBloques, y * tamañoBloques)) #Dibuja al enemigo 1
                    else: #De lo contrario (de ser un 1):
                        ventanaJuego.blit(imagenEnemigo2F, (x * tamañoBloques, y * tamañoBloques)) #Dibuja al enemigo 2
                    enemigo_actual = (enemigo_actual + 1) % 2 #Alterna entre los tipos de enemigos
    
    # ---- Definiendo Características del Jugador Principal ----
    # ---- Cargando las imágenes de vidas ----
    tresVidas = pygame.image.load("Imagenes//3vidas.png") #Agregando Imagen representativa de las tres vidas
    tresVidas = pygame.transform.scale(tresVidas, (150, 100)) #Ajustando el tamaño
    dosVidas = pygame.image.load("Imagenes//2vidas.png") #Agregando Imagen representativa de las dos vidas
    dosVidas = pygame.transform.scale(dosVidas, (150, 100)) #Ajustando el tamaño
    unaVida = pygame.image.load("Imagenes//1vida.png") #Agregando Imagen representativa de una vida
    unaVida = pygame.transform.scale(unaVida, (150, 100)) #Ajustando el tamaño
    ceroVidas = pygame.image.load("Imagenes//0vidas.png") #Agregando Imagen representativa de cero vidas
    ceroVidas = pygame.transform.scale(ceroVidas, (150, 100)) #Ajustando el tamaño
    
    # ---- Movimiento del Personaje ----
    posicionPrincipal = [(1, 10)] #Coordenadas iniciales del personaje principal
    direccion_movimiento = None  #Variable para almacenar la dirección del movimiento continuo (sin movimiento inicialmente)
    # ---- Definiendo Movimiento del Personaje Principal ----
    def movimientoPrincipal(laberinto1):
        movimientosValidos = [] #Lista que va a almacenar movimientos válidos del personaje principal
        for principal in range(len(posicionPrincipal)): #Recorriendo cada posición de la lista de posiciones del personaje principal
            y_principal, x_principal = posicionPrincipal[principal] #Guardando las nuevas coordenadas del personaje principal en X y Y
            # ---- Movimientos Válidos para el Personaje Principal ----
            if (laberinto1[y_principal - 1][x_principal] == 0):  #Verifica si el bloque de arriba es un 0 (pasillo)
                movimientosValidos.append('up') #Se puede mover hacia arriba
            if (laberinto1[y_principal + 1][x_principal] == 0):  #Verifica si el bloque de abajo es un 0 (pasillo)
                movimientosValidos.append('down') #Se puede mover hacia abajo
            if (laberinto1[y_principal][x_principal - 1] == 0):  #Verifica si el bloque de la izquierda es un 0 (pasillo)
                movimientosValidos.append('left') #Se puede mover hacia la izquierda
            if (laberinto1[y_principal][x_principal + 1] == 0):  #Verifica si el bloque de la derecha es un 0 (pasillo)
                movimientosValidos.append('right') #Se puede mover hacia la derecha
        return movimientosValidos  #Devuelve la lista de movimientos válidos
    
    # ---- Función para la pérdida de vidas ----
    vidasPrincipal = 3 #Cantidad de Vidas Iniciales del Personaje Principal
    def perdidaVidas():
        for enemigo in posicionesEnemigos: #Recorriendo a todos los enemigos por la lista (mapa)
            if (enemigo[0] == posicionPrincipal[0][0] and enemigo[1] == posicionPrincipal[0][1]): #Verificando que enemigo y principal se encuentren en la misma posición
                return True #Si hay colisión con un enemigo se retorna True
        return False #Si no hay colisión con ningún enemigo se retorna False
    
    # ---- Agregando imágen de la bomba ----
    imagenBomba = pygame.image.load("Imagenes//bomba.png") #Agregando imagen representativa de bomba
    imagenBomba = pygame.transform.scale(imagenBomba, (tamañoBloques, tamañoBloques)) #Ajustando el tamaño

    # ---- Función para manejar la explosión de la bomba ----
    def explosion(y_bomba, x_bomba, visitado):
        ventanaJuego.blit(imagenBomba, (x_bomba * tamañoBloques, y_bomba * tamañoBloques)) #Dibujar la imágen de la bomba en la pantalla
        pygame.display.flip() #Actualizar la ventana
        sleep(1) #1 segundo para la explosión
        for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]: #Iterando alrededor de la posición de la bomba (arriba, abajo, izquierda, derecha)
            y = y_bomba + dy #Nueva coordenada en y de la bomba después de moverse al bloque destructible
            x = x_bomba + dx #Nueva coordenada en x de la bomba después de moverse al bloque destructible
            if (0 <= y < len(laberinto1) and 0 <= x < len(laberinto1[y])): #Si las coordenadas se encuentran dentro de los límites del laberinto:
                if (laberinto1[y][x] == 2 and (y, x) not in visitado): #Si el bloque es destructible y no ha sido visitado
                    visitado.add((y, x)) #Agregarlo como visitado (evitando que se visiten bloques que ya se explotaron)
                    laberinto1[y][x] = 0 #Convirtiendo el bloque destructible en un pasillo
                    explosion(y, x, visitado) #Realizando las explosiones en bloques adyacentes para propagarla
        eliminar_enemigos_afectados((y_bomba, x_bomba), 1) #Eliminando a los enemigos que están dentro del rango (1) de explosión

    # ---- Función para colocar una bomba ----
    def colocar_bomba():
        global contadorBombas #Declarando contadorBombas como global
        if (contadorBombas > 0): #Verificando si hay bombas disponibles
            contadorBombas -= 1 #Reduciendo la cantidad de bombas después de colocarla
            posicion_bomba = posicionPrincipal[0] #Guardando la posición actual del personaje principal
            explosion(posicion_bomba[0], posicion_bomba[1], set()) #Realizando la explosión de la bomba (set es un conjunto (optimizando))
            contarBombas(contadorBombas) #Actualizando el contador de bombas

    # ---- Verificar cantidad de Bombas ----
    tipografia = font.SysFont("Helvetica", 35, bold=True) #Definiendo nuevamente la tipografía modificada
    def contarBombas(contadorBombas):
        bomb = tipografia.render(str(contadorBombas), True, ("#FFFFFF")) #Mostrando y convirtiendo el contador de bombas a cadena antes de renderizarlo
        pygame.draw.rect(ventanaJuego, ("#000000"), (570, 655, 50, 40)) #Dibujando un rectángulo negro para cubrir el número anterior
        ventanaJuego.blit(bomb, (570, 655)) #Dibujando el nuevo número de bombas
        pygame.display.flip() #Actualizando la pantalla
        pygame.time.delay(1000) #Esperando 1 segundo para limitar la velocidad de actualización
    
    tiempoTotal #Llamando a la variable
    tiempoInicialTercerNivel = pygame.time.get_ticks() #Obteniendo el tiempo inicial al abrir mi tercer ventana
    global tiempoTot
    # ---- Bucle Ventana Juego 3 ----
    while True:
        for event in pygame.event.get(): #Iterando sobre eventos
            if (event.type == pygame.QUIT): #Si usuario intenta cerrar ventana
                pygame.quit() #Cerrando ventana
                sys.exit() #Saliendo del script Python por completo para detener el programa en su totalidad
            elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                if (event.button == 1): #Verificar si fue clic izquierdo
                    if (posicionRegreso.collidepoint(event.pos)): #Verificar si se presionó el botón de regreso
                        screenPrincipal(volumenGlobal) #Regresando a ventana principal
            elif (event.type == pygame.KEYDOWN): #Detectar teclas
                movimientosValidos = movimientoPrincipal(laberinto1) #Obteniendo los movimientos válidos del personaje principal
                if (event.key == pygame.K_w and 'up' in movimientosValidos): #Si se presiona w y up es un movimiento válido
                    posicionPrincipal[0] = (posicionPrincipal[0][0] - 1, posicionPrincipal[0][1]) #Mover hacia arriba
                elif (event.key == pygame.K_s and 'down' in movimientosValidos): #Si se presiona s y down es un movimiento válido
                    posicionPrincipal[0] = (posicionPrincipal[0][0] + 1, posicionPrincipal[0][1]) #Mover hacia abajo
                elif (event.key == pygame.K_a and 'left' in movimientosValidos): #Si se presiona a y left es un movimiento válido
                    posicionPrincipal[0] = (posicionPrincipal[0][0], posicionPrincipal[0][1] - 1) #Mover hacia la izquierda
                elif (event.key == pygame.K_d and 'right' in movimientosValidos): #Si se presiona d y right es un movimiento válido
                    posicionPrincipal[0] = (posicionPrincipal[0][0], posicionPrincipal[0][1] + 1) #Mover hacia la derecha
                elif (event.key  == pygame.K_SPACE): #Si se presiona la tecla espacio:
                    colocar_bomba() #Colocar la bomba
        
        # ---- Llamando al Tiempo Transcurrido desde nivel 1 ----
        # ---- Calculando el tiempo transcurrido en segundos ----
        tiempoActual = pygame.time.get_ticks() #Obteniendo tiempo actual
        tiempoTranscurridoTercerVentana = (tiempoActual - tiempoInicialTercerNivel)//1000 # Calcula el tiempo transcurrido (milisegundos) en la tercer ventana
        tiempoTot = tiempoTotal + tiempoTranscurridoTercerVentana  # Calcula el tiempo total transcurrido desde el inicio del juego
        # ---- Dibujando el temporizador en la ventana ----
        pygame.draw.rect(ventanaJuego, ("#000000"), (250, 655, 200, 50)) #Limpiando el área del temporizador
        tipografia_tiempo = font.SysFont("Helvetica", 30, bold=True) #Actualizando la tipografía
        texto_tiempo = tipografia_tiempo.render(f"Tiempo: {tiempoTot} s", True, ("#FFFFFF")) #Colocando los parámetros de mi tiempo
        ventanaJuego.blit(texto_tiempo, (250, 655)) #Mostrando en la ventana
        
        # ---- Dibujando las posesión de la llave ----
        if ((posicionPrincipal[0][0], posicionPrincipal[0][1]) == (fila_llave, columna_llave) and not tengoLlave): #Si la posición del principal es igual a la de la llave y no tengo la llave:
            tipografia = font.SysFont("Helvetica", 35, bold=True) #Actualizando la tipografía
            tengoLlave = tipografia.render("1", True, ("#FFFFFF")) #Definiendo parámetros de que tengo la llave
            pygame.draw.rect(ventanaJuego, ("#000000"), (730, 655, 30, 40)) #Cuadro negro para tapar lo dibujado anteriormente
            ventanaJuego.blit(tengoLlave, (730, 655)) #Mostrando en ventana que tengo la llave
            tengoLlave = True #Cambiando el valor, ahora sí tengo la llave
            if (tengoLlave == True): #Si tengo la llave:
                pygame.draw.rect(ventanaJuego, ("#1D1D1D"), (columna_llave * tamañoBloques, fila_llave * tamañoBloques, tamañoBloques, tamañoBloques)) #Dibuja un cuadro gris sobre ella para que nunca sea visible
        # ---- Verificar si el jugador tiene la llave y está alrededor de la puerta ----
        if tengoLlave and (((posicionPrincipal[0][0] - 1, posicionPrincipal[0][1]) == (fila_puerta, columna_puerta)) or
                        ((posicionPrincipal[0][0] + 1, posicionPrincipal[0][1]) == (fila_puerta, columna_puerta)) or
                        ((posicionPrincipal[0][0], posicionPrincipal[0][1] - 1) == (fila_puerta, columna_puerta)) or
                        ((posicionPrincipal[0][0], posicionPrincipal[0][1] + 1) == (fila_puerta, columna_puerta))):
            #Si el jugador tiene la llave y está alrededor de la puerta va al segundo nivel
            screenTriunfo()
            break
        # ---- Movimiento continuo mientras se mantiene presionada una tecla ----
        if (direccion_movimiento): #Si se está manteniendo una tecla presionada:
            movimientosValidos = movimientoPrincipal(laberinto1) #Obtengo la lista de los movimientos válidos del personaje
            if (direccion_movimiento == 'up' and 'up' in movimientosValidos): #Si estoy presionando w y up es válido:
                posicionPrincipal[0] = (posicionPrincipal[0][0] - 1, posicionPrincipal[0][1]) #Moverse hacia arriba
            elif (direccion_movimiento == 'down' and 'down' in movimientosValidos): #Si estoy presionando s y down es válido:
                posicionPrincipal[0] = (posicionPrincipal[0][0] + 1, posicionPrincipal[0][1]) #Moverse hacia abajo
            elif (direccion_movimiento == 'left' and 'left' in movimientosValidos): #Si estoy presionando a y left es válido:
                posicionPrincipal[0] = (posicionPrincipal[0][0], posicionPrincipal[0][1] - 1) #Moverse hacia la izquierda
            elif (direccion_movimiento == 'right' and 'right' in movimientosValidos): #Si estoy presionando d y right es válido:
                posicionPrincipal[0] = (posicionPrincipal[0][0], posicionPrincipal[0][1] + 1) #Moverse hacia la derecha
        
        # ---- Verificando colisión con enemigos ----
        if (perdidaVidas()):
            vidasPrincipal -= 1  #Restando una vida al personaje principal si hay colisión con un enemigo
            if (vidasPrincipal == 0): #Si ya no se tienen vidas:
                screenDerrota() #Ir a ventana de derrota
                break #Saliendo del bucle de ventana juego 1 si se pierden todas las vidas
        
        # ---- Verificando no tener llave y no tener bombas a la vez ----
        if not tengoLlave and contadorBombas==0:
            screenDerrota() #Ir a ventana de derrota
            break #Saliendo del bucle principal del juego
        
        dibujandoLaberinto() #Dibujando laberinto
        ventanaJuego.blit(imagenPersonajePrincipal, (posicionPrincipal[0][1] * tamañoBloques, posicionPrincipal[0][0] * tamañoBloques)) #Dibujando la imagen del personaje principal según la skin seleccionada
        
        # ---- Dibujando las imágenes de las vidas ----
        if (vidasPrincipal == 3): #Si tengo tres vidas:
            ventanaJuego.blit(tresVidas, (780, 625)) #Mostrando en pantalla imágen representativa de las tres vidas
        elif (vidasPrincipal == 2): #Si tengo dos vidas:
            ventanaJuego.blit(dosVidas, (780, 625)) #Mostrando en pantalla imágen representativa de las dos vidas
        elif (vidasPrincipal == 1): #Si tengo una vida:
            ventanaJuego.blit(unaVida, (780, 625)) #Mostrando en pantalla imágen representativa de la vida
        elif (vidasPrincipal == 0): #Si tengo cero vidas:
            ventanaJuego.blit(ceroVidas, (780, 625)) #Mostrando en pantalla imágen representativa de las cero vidas
        
        dibujar_enemigos() #Dibujando a los enemigos
        movimientoEnemigos(laberinto1) #Actualizando posiciones de enemigos
        movimientoPrincipal(laberinto1) #Reflejando el movimiento del personaje principal
        pygame.display.flip() #Actualizando pantalla
        sleep (1/3) #Limitar la velocidad del juego
    return tiempoTot
# ----------------------------------- Finalizando la Ventana de Juego 3 -----------------------------------
global tiempoTot
# ----------------------------------- Iniciando la Ventana de Triunfo -----------------------------------
def screenTriunfo():
    mixer.init()
    pygame.mixer.music.set_volume(volumenGlobal) #Manteniendo el volumen
    ventanaTriunfo = pygame.display.set_mode((950, 700)) #Creación de Ventana
    fondoVentanaTriunfo = pygame.image.load("Imagenes//VICTORIA.png") #Agregando fondo de pantalla de victoria
    ventanaTriunfo.blit(fondoVentanaTriunfo, (0,0)) #Visualizar el fondo
    tipografia = font.SysFont("Helvetica", 45, bold=True) #Actualizando la tipografía
    mostrarTiempo = tipografia.render(str(tiempoTot) + " segundos", True, ("#FFFFFF"))  #Indicando parámetros de mi tiempo
    xPregunta = (ventanaTriunfo.get_width() - mostrarTiempo.get_width()) / 2 #Calcular la posición horizontal para centrar el texto
    yPregunta = 610  #Posición vertical fija para el texto (pregunta)
    ventanaTriunfo.blit(mostrarTiempo, (xPregunta, yPregunta)) #Reflejando el tiempo
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes/BotonRegreso.png") #Agregando Imagen representativa del botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (50, 50)) #Ajustando el tamaño
    posicionRegreso = ventanaTriunfo.blit(botonRegreso, (10,635)) #Visualizar la imagen con su posición
    # ---- Bucle principal de Ventana de Triunfo ----
    running = True
    while running:
        for event in pygame.event.get(): #Iterando sobre eventos
            if (event.type == pygame.QUIT): #Si el usuario intenta cerrar ventana:
                pygame.quit() #Cerrando módulos de pygame
                sys.exit() #Asegurando salida del juego
            elif (event.type == pygame.KEYDOWN): #Detectando Teclas
                if (event.key == pygame.K_ESCAPE):
                    running = False  #Salir del bucle si se presiona la tecla Esc
            elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                if (event.button == 1): #Verificar si fue clic izquierdo
                    if (posicionRegreso.collidepoint(event.pos)): #Verificar si se presionó el botón de reinicio
                        screenPrincipal(volumenGlobal) #Devolverse a ventana de juego
        pygame.display.flip() #Actualizando pantalla
    return tiempoTot
# ----------------------------------- Finalizando la Ventana de Triunfo -----------------------------------

# ----------------------------------- Iniciando la Ventana de Mejores Puntajes -----------------------------------
def cargar_puntajes():
    puntajes = [] #Esto se encarga de guardar los puntajes del txt, empezando vacía
    try:
        with open("puntajes.txt", "r") as file: #Se abre el texto en modo lectura
            for line in file: #Iterando sobre cada línea dentro del archivo
                # Verificar que la línea contenga una coma antes de dividirla
                if ("," in line): #Si la línea contiene una coma (para formato):
                    nombre, tiempo = line.strip().split(",") #Elimina espacios en blanco de la línea (principio y final), luego divide la línea en las dos parte y guarda en variables
                    puntajes.append((nombre, tiempo)) #Añadiendo la tupla a la lista de los puntajes
                else:
                    print(f"Error: línea incorrecta en el archivo puntajes.txt: {line}") #Si no hay coma se le da a entender al usuario con un mensaje de error
    except FileNotFoundError: #Si el archivo txt no se encuentra:
        pass #Pasar sin hacer nada
    return puntajes #Retorna la lista con puntajes

# ---- Función para guardar los puntajes en el archivo de texto ----
def guardar_puntajes(nombre_usuario, tiempo):
    global nombreUsuario #Agregando esta línea para usar nombreUsuario globalmente
    global tiempoTot #Agregando esta línea para usar tiempoTot globalmente
    try:
        with open("puntajes.txt", "a") as file: #a es el modo que te permite agregar nuevos datos al final del archivo y with nos ayuda para que el archivo se cierre correctamente
            file.write(f"{nombre_usuario},{tiempo}\n") #Escribiendo el nombre del usuario y su tiempo
    except FileNotFoundError: #Si el archivo txt no se encuentra:
        pass #Pasar sin hacer nada

def screenMejoresPuntajes():
    global nombreUsuario #Agregando esta línea para usar nombreUsuario globalmente
    global tiempoTot #Agregando esta línea para usar tiempoTot globalmente
    ventanaMejoresPuntajes = pygame.display.set_mode((950, 700)) #Creando ventana
    fondoVentanaMejoresPuntajes = pygame.image.load("Imagenes//FondoMejorePuntajes.png") #Agregando fondo de pantalla
    ventanaMejoresPuntajes.blit(fondoVentanaMejoresPuntajes, (0, 0)) #Visualizar el fondo
    
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes/BotonRegreso.png") #Agregando Imagen representativa de botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (50, 50)) #Ajustando el tamaño
    ventanaMejoresPuntajes.blit(botonRegreso, (15,15)) #Visualizar la imagen con su posición
    botonRegreso = Rect(15,15,50,50) #X, Y, Ancho, Alto

    puntajes = cargar_puntajes() #Guardando función cargar puntajes en variable
    puntajes_ordenados = sorted(puntajes, key=lambda x: x[1])[:5] #Obteniendo los 5 mejores puntajes (referencia al segundo elemento (tiempo))
    tipografia = font.SysFont("Helvetica", 20, bold=True) #Actualizando la tipografía
    y_pos = 270 #Definiendo coordenada inicial en y para dibujar
    for i, (nombre, tiempo) in enumerate(puntajes_ordenados): #Obteniendo índice y tupla de los puntajes ordenados
        texto_puntaje = tipografia.render(f"{nombre}: {tiempo} segundos", True, ("#000000")) #Creando el texto del puntaje
        x_pos = (ventanaMejoresPuntajes.get_width() - texto_puntaje.get_width()) / 2 #Posición en x
        ventanaMejoresPuntajes.blit(texto_puntaje, (x_pos, y_pos + i * 50)) #Dibujando en ventana el texto del puntaje
        
    guardar_puntajes(nombreUsuario, tiempoTot) #Llamando a función
    pygame.display.flip() #Actualizando pantalla
    # ---- Bucle principal de Ventana de Mejores Puntajes ----
    while True:
        for event in pygame.event.get(): #Iterando sobre eventos
            if event.type == pygame.QUIT: #Si el usuario intenta cerrar ventana:
                pygame.quit() #Cerrando módulos de pygame
                sys.exit() #Asegurando salida del juego
            elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                if (event.button == 1): #Verificar si fue clic izquierdo
                    x, y = event.pos #Guardando en variables donde se hizo clic
                    if (botonRegreso.collidepoint(event.pos)):
                        screenPrincipal(volumenGlobal)
        pygame.display.flip() #Actualizando pantalla
# ----------------------------------- Finalizando la Ventana de Mejores Puntajes -----------------------------------

# ----------------------------------- Iniciando la Ventana Principal -----------------------------------
def screenPrincipal(volumenGlobal):
    ventanaPrincipal = pygame.display.set_mode(sizeScreen) #Creando Ventana
    fondoVentanaPrincipal = pygame.image.load("Imagenes/Bombfondo.png") #Agregando fondo de pantalla principal
    ventanaPrincipal.blit(fondoVentanaPrincipal, (0,0)) #Visualizar el fondo
    pygame.mixer.music.load("Sonido/MISSING YOU.mp3") #Agregando música
    pygame.mixer.music.set_volume(volumenGlobal) #Establecer el volumen antes de reproducir la música
    pygame.mixer.music.play(-1) #Repitiendo el sonido de forma ilimitada

    # ---- Función para crear botones ----
    def creandoBotones(ventanaPrincipal, boton, palabra, color):
        pygame.draw.rect(ventanaPrincipal, ("#000000"), (boton.x - 2, boton.y - 2, boton.width + 4, boton.height + 4)) #Creando borde negro a los botones
        draw.rect(ventanaPrincipal, (color), boton, 0) #Dibujando el rectángulo en pantalla
        texto = tipografia.render(palabra, True, ("#000000")) #Creando los parámetros para el texto
        ventanaPrincipal.blit(texto, (boton.x+(boton.width-texto.get_width())/2,boton.y+(boton.height-texto.get_height())/2)) #Colocando texto sobre rectángulo y haciendo dinámica la posición del texto

    # ---- Medidas y Posiciones del rectángulo de los botones ----
    informacion = Rect(100,550,150,50) #X, Y, Ancho, Alto
    configuracion = Rect(300,550,150,50) #X, Y, Ancho, Alto
    jugar = Rect(500,550,150,50) #X, Y, Ancho, Alto
    mejoresPuntajes = Rect(700,550,150,50) #X, Y, Ancho, Alto

    # ---- Llamando a los Botones ----
    creandoBotones(ventanaPrincipal, informacion, "Información", "#FF4D39")
    creandoBotones(ventanaPrincipal, configuracion, "Configuración", "#FF7144")
    creandoBotones(ventanaPrincipal, jugar, "Jugar", "#ff994c")
    creandoBotones(ventanaPrincipal, mejoresPuntajes, "Mejores Puntajes","#FFC154")

    # ---- Ícono del Juego ----
    pygame.display.set_caption("Bomber CLB") #Poniendo nombre a la ventana
    icono = pygame.image.load("Imagenes/IconoBomberCLB.png") #Agregando imagen del icono
    pygame.display.set_icon(icono) #Colocando el icono

    # ---- Imágen de Ventana Principal ----
    logo = pygame.image.load("Imagenes/IconoBomberCLB.png") #Colocando Imágen
    ventanaPrincipal.blit(logo, ((sizeScreen[0] - logo.get_width())/2, 20)) #Colocando imágen (cálculos horizontales)

    while True: #Bucle para ventana principal
        for event in pygame.event.get(): #Iterando sobre eventos
            if (event.type == pygame.QUIT): #Si el usuario intenta cerrar ventana
                sys.exit() #Saliendo del juego
            elif (event.type == pygame.MOUSEBUTTONDOWN): #Detectar clic del mouse
                if (event.button == 1): # Verificar si fue clic izquierdo
                    x, y = event.pos #Guardando en variables donde se hizo clic
                    # -- Verificar si el clic fue dentro de alguno de los botones de la Ventana Principal
                    if (informacion.collidepoint(event.pos)):
                        ventanaPrincipal.fill(("#000000")) #Limpiando Ventana Principal
                        screenInformacion() #Ir a Ventana de Información
                    elif (configuracion.collidepoint(event.pos)):
                        ventanaPrincipal.fill(("#000000")) #Limpiando Ventana Principal
                        screenConfiguracion() #Ir a Ventana de Configuración
                    elif (jugar.collidepoint(event.pos)):
                        ventanaPrincipal.fill(("#000000")) #Limpiando Ventana Principal
                        screenJuego1() #Ir a Ventana de Juego
                    elif (mejoresPuntajes.collidepoint(event.pos)):
                        ventanaPrincipal.fill(("#000000")) #Limpiando Ventana Principal
                        screenMejoresPuntajes() #Ir a Ventana de Mejores Puntajes
        pygame.display.flip() #Actualizando Pantalla
# ----------------------------------- Finalizando la Ventana Principal -----------------------------------
screenPrincipal(volumenGlobal)
pygame.quit()