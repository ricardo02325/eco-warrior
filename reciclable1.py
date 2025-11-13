import pygame
import sys
import selector_avanzado
import configuraciones

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana principal
ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))

# Cargar fondo y escalar a las dimensiones de la ventana
fondo = pygame.image.load("recursos/fondos/BasuraReciclable.png")
fondo = pygame.transform.scale(fondo, (ancho, alto))
 
# Colores RGB
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)

# Recursos para botones
boton1 = pygame.image.load("recursos/botones/botonregregsar.png")
boton1.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
boton1 = pygame.transform.scale(boton1, (70, 70))

# Fuente y tamaño del texto
fuentemax = pygame.font.SysFont("PixAntiqua", 60)
fuentemin = pygame.font.SysFont("PixAntiqua", 30)

# Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Función
def reciclable():
    clic = False
    while True:
        ventana.blit(fondo, (0, 0))

        # Obtener la posición del ratón
        mx, my = pygame.mouse.get_pos()

        # Dibujar el botón
        ventana.blit(boton1, (20, 20))

        # Obtener el rectángulo del botón
        boton1_rect = boton1.get_rect(topleft=(20, 20))

        # Verificar si el ratón está sobre el botón
        if boton1_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
                selector_avanzado.selector()
        # Reiniciar la variable de clic
        clic = False
        if configuraciones.idioma == "español":
            Tipo = fuentemax.render("Reciclable", True, color_negro)
            ventana.blit(Tipo, (125, 170))
            Texto1 = fuentemin.render("Libro", True, color_negro)
            ventana.blit(Texto1, (670, 100))
            Texto2 = fuentemin.render("Sobre", True, color_negro)
            ventana.blit(Texto2, (670, 270))
            Texto3 = fuentemin.render("Periodico", True, color_negro)
            ventana.blit(Texto3, (670, 430))
            Texto4 = fuentemin.render("Botella", True, color_negro)
            ventana.blit(Texto4, (670, 610))
            Texto5 = fuentemin.render("Lata de Atun", True, color_negro)
            ventana.blit(Texto5, (1000, 100))
            Texto6 = fuentemin.render("Lata", True, color_negro)
            ventana.blit(Texto6, (1000, 270))
            Texto7 = fuentemin.render("Botella", True, color_negro)
            ventana.blit(Texto7, (1000, 430))
            Texto8 = fuentemin.render("Bolsa de Papel", True, color_negro)
            ventana.blit(Texto8, (1000, 610))
        elif configuraciones.idioma == "inglés":
            Tipo = fuentemax.render("Recyclable", True, color_negro)
            ventana.blit(Tipo, (125, 170))
            Texto1 = fuentemin.render("Book", True, color_negro)
            ventana.blit(Texto1, (670, 100))
            Texto2 = fuentemin.render("Envelope", True, color_negro)
            ventana.blit(Texto2, (670, 270))
            Texto3 = fuentemin.render("Newspaper", True, color_negro)
            ventana.blit(Texto3, (670, 430))
            Texto4 = fuentemin.render("Bottle", True, color_negro)
            ventana.blit(Texto4, (670, 610))
            Texto5 = fuentemin.render("Can of tuna", True, color_negro)
            ventana.blit(Texto5, (1000, 100))
            Texto6 = fuentemin.render("Can", True, color_negro)
            ventana.blit(Texto6, (1000, 270))
            Texto7 = fuentemin.render("Bottle", True, color_negro)
            ventana.blit(Texto7, (1000, 430))
            Texto8 = fuentemin.render("Paper Bag", True, color_negro)
            ventana.blit(Texto8, (1000, 610))
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
    reciclable()