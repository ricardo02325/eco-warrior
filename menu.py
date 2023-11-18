import pygame
import sys
import dificultad
import configuraciones
import comic1

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana principal
ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))

# Cargar fondo y escalar a las dimensiones de la ventana
fondo = pygame.image.load("recursos/fondos/fondo.png")
fondo = pygame.transform.scale(fondo, (ancho, alto))
 
# Colores RGB
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)

# Recursos para botones
boton1 = pygame.image.load("recursos/botones/play.png")
boton1.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
boton1 = pygame.transform.scale(boton1, (130, 50))

# Recursos para botones
boton2 = pygame.image.load("recursos/botones/comic.png")
boton2.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
boton2 = pygame.transform.scale(boton2, (80, 80))

# Cargar sonido
sonido = pygame.mixer.music.load("recursos/musica/nivel3.mp3")
sonido = pygame.mixer.music.play(-1)

confi = pygame.image.load("recursos/botones/configuracion.png")
confi.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
confi = pygame.transform.scale(confi, (80, 80))

logo = pygame.image.load("recursos/fondos/logo.png")
logo.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
logo = pygame.transform.scale(logo, (400, 400))

# Fuente y tamaño del texto
fuente = pygame.font.Font(None, 60)

# Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Función para el menú principal
def menu_principal():
    volumen_actual1 = configuraciones.volumen_actual
    # Variable para controlar el clic del ratón
    clic = False
    while True:
        ventana.blit(fondo, (0, 0))

        # Obtener la posición del ratón
        mx, my = pygame.mouse.get_pos()

        #Sonido
        sonido = pygame.mixer.music.set_volume(volumen_actual1)

        # Dibujar el botón
        ventana.blit(boton1, (560, 510))

        # Dibujar el botón
        ventana.blit(boton2, (1180, 500))

        # Dibujar el boton de confi
        ventana.blit(confi, (1170, 10))

        # Dibujar el logo
        ventana.blit(logo, (440, 40))    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        # Obtener el rectángulo del botón
        confi_rect = confi.get_rect(topleft=(1170, 10))

        # Obtener el rectángulo del botón
        boton1_rect = boton1.get_rect(topleft=(560, 510))
        
        # Obtener el rectángulo del botón
        boton2_rect = boton2.get_rect(topleft=(1180, 500))

        # Verificar si el ratón está sobre el botón
        if boton1_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
                dificultad.dificultad() # Llamar a la función de selector
                # Verificar si el ratón está sobre el botón
        if boton2_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
                comic1.comic1() # Llamar a la función de selector

        # Verificar si el ratón está sobre el botón
        if confi_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
                configuraciones.volumen() # Llamar a la función del volumen

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

# Iniciar el menú principal
if __name__ == "__main__":
    menu_principal()