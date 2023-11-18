import pygame
import sys
import comic3
import comic1

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana principal
ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))

# Cargar fondo y escalar a las dimensiones de la ventana
fondo = pygame.image.load("recursos/comic/comic2.png")
fondo = pygame.transform.scale(fondo, (ancho, alto))
 
# Colores RGB
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)

# Recursos para botones
boton1 = pygame.image.load("recursos/botones/botonregregsar.png")
boton1.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
boton1 = pygame.transform.scale(boton1, (70, 70))

# Recursos para botones
boton2 = pygame.image.load("recursos/botones/BotonRegresar_volteado.png")
boton2.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
boton2 = pygame.transform.scale(boton2, (70, 70))


# Fuente y tamaño del texto
fuente = pygame.font.Font(None, 60)

# Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Función para el menú principal
def comic2():
    clic = False
    while True:
        ventana.blit(fondo, (0, 0))

        # Obtener la posición del ratón
        mx, my = pygame.mouse.get_pos()

        # Dibujar el botón
        ventana.blit(boton1, (70, 70))

        # Dibujar el botón
        ventana.blit(boton2, (1150, 70))

        # Obtener el rectángulo del botón
        boton1_rect = boton1.get_rect(topleft=(70, 70))

        # Obtener el rectángulo del botón
        boton2_rect = boton2.get_rect(topleft=(1150, 70))

        # Verificar si el ratón está sobre el botón
        if boton1_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
                comic1.comic1()
        # Verificar si el ratón está sobre el botón
        if boton2_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
                comic3.comic3()

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
    comic2()