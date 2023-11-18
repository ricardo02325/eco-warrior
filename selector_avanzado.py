import pygame
import sys
import nivel1fa
import nivel2fa
import nivel3fa
import dificultad
import menu
import configuraciones

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana principal
ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))

# Cargar fondo y escalar a las dimensiones de la ventana
fondo = pygame.image.load("recursos/fondos/SeleccionNivel.png").convert()
fondo = pygame.transform.scale(fondo, (ancho, alto))

# Fuente
fuente = pygame.font.SysFont("PixAntiqua", 60)
 
# Colores RGB
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)

# Recursos para botones
jugar = pygame.image.load("recursos/botones/BotonNivel1.png")
jugar.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
jugar = pygame.transform.scale(jugar, (277, 66))

jugar2 = pygame.image.load("recursos/botones/BotonNivel2.png")
jugar2.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
jugar2 = pygame.transform.scale(jugar2, (277, 66))

jugar3 = pygame.image.load("recursos/botones/BotonNivel3.png")
jugar3.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
jugar3 = pygame.transform.scale(jugar3, (277, 66))

home = pygame.image.load("recursos/botones/home.png")
home.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
home = pygame.transform.scale(home, (120, 80))

regresar = pygame.image.load("recursos/botones/regresar.png")
regresar.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
regresar = pygame.transform.scale(regresar, (130, 60))

# Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Variable para controlar el clic del ratón
clic = False

# Función para el menú principal
def selector():
    global clic  # Declarar "clic" como globales
    while True:
        ventana.blit(fondo, (0, 0))

        # Obtener la posición del ratón
        mx, my = pygame.mouse.get_pos()

        # Dibujar el botón
        ventana.blit(jugar, (130, 200))

        # Dibujar el botón
        ventana.blit(jugar2, (500, 200))

        # Dibujar el botón
        ventana.blit(jugar3, (900, 200))

        # Dibujar el boton de regresar
        ventana.blit(regresar, (65, 70))

        # Dibujar la casita
        ventana.blit(home, (1100, 70))

        # Obtener el rectángulo del botón jugar 1
        boton1_rect = jugar.get_rect(topleft=(130, 200))

        # Obtener el rectángulo del botón juag 2
        boton2_rect = jugar2.get_rect(topleft=(500, 200))

        # Obtener el rectángulo del botón jugar 3
        boton3_rect = jugar3.get_rect(topleft=(900, 200))

        # Obtener el rectángulo del botón home
        home_rect = home.get_rect(topleft=(1100, 70))

        # Obtener el rectángulo del botón
        nivel1facil_rect = regresar.get_rect(topleft=(65, 70))

        # Idioma
        if configuraciones.idioma == "español":
            texto_saludo = fuente.render("Niveles", True, color_negro)
            ventana.blit(texto_saludo, (540, 42))
        elif configuraciones.idioma == "inglés":
            texto_saludo = fuente.render("Levels", True, color_negro)
            ventana.blit(texto_saludo, (540, 42))

        # Verificar si el ratón está sobre el botón
        if boton1_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
               nivel1fa.main() # Llamar a la función de nivel1 fácil

        # Verificar si el ratón está sobre el botón
        if boton2_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
               nivel2fa.main() # Llamar a la función de nivel2 fácil
        
        if home_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
               menu.menu_principal() # Llamar a la función de nivel1 fácil
        
        # Verificar si el ratón está sobre el botón
        if boton3_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
               nivel3fa.main() # Llamar a la función de nivel3 fácil

        if  nivel1facil_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
                dificultad.dificultad() # Llamar a la función de dificultad

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
    selector()