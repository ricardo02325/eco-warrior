import pygame
import sys
import menu

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana principal
ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))

# Cargar fondo y escalar a las dimensiones de la ventana
fondo = pygame.image.load("recursos/fondos/configuraciones.png").convert()
fondo = pygame.transform.scale(fondo, (ancho, alto))

# Colores RGB
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)

# Fuente y tamaño del texto 1
fuentemin = pygame.font.SysFont("PixAntiqua", 20)

# Fuente y tamaño del texto 2
fuentemid = pygame.font.SysFont("PixAntiqua", 40)

# Fuente y tamaño del texto 3
fuentemax = pygame.font.SysFont("PixAntiqua", 50)

# Cargar sonido
pygame.mixer.music.load("recursos/musica/menu.mp3")
pygame.mixer.music.play(-1) 

# Recursos para botones
boton = pygame.image.load("recursos/botones/botonregregsar.png")
boton.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
boton = pygame.transform.scale(boton, (89, 89))

# Recursos para controles
controles = pygame.image.load("recursos/botones/controles.png")
controles.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
controles = pygame.transform.scale(controles, (240, 170))

# Recursos para inglés
ingles = pygame.image.load("recursos/botones/banderaeu.png")
ingles.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
ingles = pygame.transform.scale(ingles, (110, 90))

# Recursos para español
espanol = pygame.image.load("recursos/botones/banderamx.png")
espanol.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
espanol = pygame.transform.scale(espanol, (110, 90))

# Recursos para botones de volumen
volume1 = pygame.image.load("recursos/botones/volumen+.png")
volume1.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
volume1 = pygame.transform.scale(volume1, (100, 100))

# Recursos para botones de volumen
volume2 = pygame.image.load("recursos/botones/volumen-.png")
volume2.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
volume2 = pygame.transform.scale(volume2, (100, 100))

# Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Variable para controlar el clic del ratón
clic = False

# Variable idioma
idioma = "español"
volumen_actual = 1

def volumen():
    global idioma # Declara "idioma" como globales
    clic = False
    global volumen_actual
    while True:
        ventana.blit(fondo, (0, 0))

        # Obtener la posición del ratón
        mx, my = pygame.mouse.get_pos()

        # Dibujar el botón
        ventana.blit(boton, (70, 70))

        # Dibujar el botón de español
        ventana.blit(espanol, (1000, 300))

        # Dibujar el botón de inglés
        ventana.blit(ingles, (1000, 430))

        # Dibujar los controles
        ventana.blit(controles, (90, 350))

        # Dibujar los botones de volumen
        ventana.blit(volume1, (600, 300))
        ventana.blit(volume2, (600, 420))

        # Obtener el rectángulo del botón
        boton_rect = boton.get_rect(topleft=(70, 70))

        # Verificar si el ratón está sobre el botón
        if boton_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
                menu.menu_principal()

        # Obtener los rectángulos de los botones de volumen
        volume_rect1 = volume1.get_rect(topleft=(600, 300))
        volume_rect2 = volume2.get_rect(topleft=(600, 420))

        # Obtener los rectángulos del botón español
        espanol_rect = espanol.get_rect(topleft=(1000, 300))

        # Obtener los rectángulos del botón inglés
        ingles_rect = ingles.get_rect(topleft=(1000, 430))

        # Verificar si se hizo clic en los botones de volumen
        if volume_rect1.collidepoint((mx, my)):
            if clic:
                volumen_actual += 0.1  # Reducir en 0.1 unidades
                pygame.mixer.music.set_volume(volumen_actual)
                print('Volumen aumentando:', volumen_actual)
        elif volume_rect2.collidepoint((mx, my)):
            if clic:
                volumen_actual -= 0.1  # Reducir en 0.1 unidades
                pygame.mixer.music.set_volume(volumen_actual)
                print('Volumen reducido:', volumen_actual)
        # Texto para el volumen
        #texto_volumen = fuentemid.render("Volumen: {:.1f}".format(volumen_actual), False, color_negro)
        #ventana.blit(texto_volumen, (770, 380))

        # Verificar si el ratón está sobre el botón
        if ingles_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
               idioma = "inglés"
               print(idioma)
        if espanol_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
               idioma = "español"
               print(idioma)
        if idioma == "español":
            texto_saludo = fuentemax.render("Configuraciones", False, color_negro)
            ventana.blit(texto_saludo, (445, 45))
            texto_controles = fuentemid.render("Controles", False, color_negro)
            ventana.blit(texto_controles, (120, 245))
            texto_volumen = fuentemid.render("Volumen", False, color_negro)
            ventana.blit(texto_volumen, (570, 245))
            texto_idioma = fuentemid.render("Idioma", False, color_negro)
            ventana.blit(texto_idioma, (990, 245))
            texto_mas = fuentemax.render("+", False, color_negro)
            ventana.blit(texto_mas, (750, 325))
            texto_menos = fuentemax.render("-", False, color_negro)
            ventana.blit(texto_menos, (750, 445))
        elif idioma == "inglés":
            texto_saludo = fuentemax.render("Settings", False, color_negro)
            ventana.blit(texto_saludo, (535, 45))
            texto_controles = fuentemid.render("Controls", False, color_negro)
            ventana.blit(texto_controles, (120, 245))
            texto_volumen = fuentemid.render("Volume", False, color_negro)
            ventana.blit(texto_volumen, (580, 245))
            texto_idioma = fuentemid.render("Language", False, color_negro)
            ventana.blit(texto_idioma, (970, 245))
            texto_mas = fuentemax.render("+", False, color_negro)
            ventana.blit(texto_mas, (750, 325))
            texto_menos = fuentemax.render("-", False, color_negro)
            ventana.blit(texto_menos, (750, 445))

        # Reiniciar la variable de clic
        clic = False

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    clic = True

        # Actualizar la ventana
        pygame.display.update()
        relojPrincipal.tick(60)

# Llamar a la función para iniciar la ventana
if __name__ == "__main__":
    volumen()