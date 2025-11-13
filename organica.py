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
fondo = pygame.image.load("recursos/fondos/BasuraOrganica.png")
fondo = pygame.transform.scale(fondo, (ancho, alto))
 
# Colores RGB
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)

# Recursos para botones
boton1 = pygame.image.load("recursos/botones/botonregregsar.png")
boton1.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
boton1 = pygame.transform.scale(boton1, (70, 70))

# Fuente y tamaño del texto
fuentemax = pygame.font.SysFont("PixAntiqua", 50)
fuentemin = pygame.font.SysFont("PixAntiqua", 30)
# Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Función
def organica():
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
          # Idioma
        if configuraciones.idioma == "español":
            Tipo = fuentemax.render("Organica", True, color_negro)
            ventana.blit(Tipo, (125, 170))
            Texto1 = fuentemin.render("Platano", True, color_negro)
            ventana.blit(Texto1, (670, 80))
            Texto2 = fuentemin.render("Manzana", True, color_negro)
            ventana.blit(Texto2, (670, 180))
            Texto3 = fuentemin.render("Pescado", True, color_negro)
            ventana.blit(Texto3, (670, 280))
            Texto4 = fuentemin.render("Sandia", True, color_negro)
            ventana.blit(Texto4, (670, 380))
            Texto5 = fuentemin.render("Hueso", True, color_negro)
            ventana.blit(Texto5, (670, 500))
            Texto6 = fuentemin.render("Huevo", True, color_negro)
            ventana.blit(Texto6, (670, 625))
        elif configuraciones.idioma == "inglés":
            Tipo = fuentemax.render("Organic", True, color_negro)  
            ventana.blit(Tipo, (135, 170))
            Texto1 = fuentemin.render("Banana", True, color_negro)
            ventana.blit(Texto1, (670, 80))
            Texto2 = fuentemin.render("Apple", True, color_negro)
            ventana.blit(Texto2, (670, 180))
            Texto3 = fuentemin.render("Fish", True, color_negro)
            ventana.blit(Texto3, (670, 280))
            Texto4 = fuentemin.render("Watermelon", True, color_negro)
            ventana.blit(Texto4, (670, 380))
            Texto5 = fuentemin.render("Bone", True, color_negro)
            ventana.blit(Texto5, (670, 500))
            Texto6 = fuentemin.render("Egg", True, color_negro)
            ventana.blit(Texto6, (670, 625))
            
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
    organica()