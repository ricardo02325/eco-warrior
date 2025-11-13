import pygame
import sys
import dificultad

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana principal
ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))

# Cargar fondo y escalar a las dimensiones de la ventana
fondo = pygame.image.load("recursos/fondos/TiposBasura.png")
fondo = pygame.transform.scale(fondo, (ancho, alto))
 
# Colores RGB
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)

# Recursos para botones
volver = pygame.image.load("recursos/botones/botonregregsar.png")
volver.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
volver = pygame.transform.scale(volver, (70, 70))

# Fuente y tamaño del texto
fuente = pygame.font.Font(None, 60)

# Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Variable para controlar el clic del ratón
clic = False

# Función para el menú principal
def ayudar():
    clic = False
    while True:
        ventana.blit(fondo, (0, 0))

        # Obtener la posición del ratón
        mx, my = pygame.mouse.get_pos()

        # Dibujar el botón
        ventana.blit(volver, (100, 100))

        # Obtener el rectángulo del botón
        volver_rect = volver.get_rect(topleft=(100, 100))

        # Verificar si el ratón está sobre el botón
        if volver_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
                dificultad.dificultad() # Llamar a la función de selector

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
    ayudar()