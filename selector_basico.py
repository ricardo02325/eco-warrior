import pygame
import sys
import nivel1fa
import nivel2fa
import nivel3fa
import dificultad
import menu
import configuraciones
import noreciclable1
import reciclable1
import organica1

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana principal
ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))

# Cargar fondo y escalar a las dimensiones de la ventana
fondo = pygame.image.load("recursos/fondos/SeleccionNivel.png").convert()
fondo = pygame.transform.scale(fondo, (ancho, alto))

# Colores RGB
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)

# Idioma
idiomas = {
    "español": {
        "seleccionar": "Elige tu nivel"
    },
    "inglés": {
        "saludo": "Hello World!"
    }
}
fuente = pygame.font.SysFont("PixAntiqua", 60)

# Recursos para botones
jugar = pygame.image.load("recursos/botones/BotonNivel1.png")
jugar.set_colorkey(color_blanco)
jugar = pygame.transform.scale(jugar, (277, 66))

jugar2 = pygame.image.load("recursos/botones/BotonNivel2.png")
jugar2.set_colorkey(color_blanco)
jugar2 = pygame.transform.scale(jugar2, (277, 66))

jugar3 = pygame.image.load("recursos/botones/BotonNivel3.png")
jugar3.set_colorkey(color_blanco)
jugar3 = pygame.transform.scale(jugar3, (277, 66))

home = pygame.image.load("recursos/botones/home.png")
home.set_colorkey(color_blanco)
home = pygame.transform.scale(home, (120, 80))

regresar = pygame.image.load("recursos/botones/regresar.png")
regresar.set_colorkey(color_blanco)
regresar = pygame.transform.scale(regresar, (130, 60))

bote = pygame.image.load("recursos/botones/BoteVerde.png")
bote.set_colorkey(color_blanco)
bote = pygame.transform.scale(bote, (112, 133))
bote2 = pygame.image.load("recursos/botones/BoteBlanco.png")
bote2.set_colorkey(color_blanco)
bote2 = pygame.transform.scale(bote2, (112, 133))
bote3 = pygame.image.load("recursos/botones/Bote_Negro.png")
bote3.set_colorkey(color_blanco)
bote3 = pygame.transform.scale(bote3, (112, 133))
#Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Variable para controlar el clic del ratón
clic = False

# Función para el menú principal
def selector():
    while True:
        clic = False
        ventana.blit(fondo, (0, 0))

        # Obtener la posición del ratón
        mx, my = pygame.mouse.get_pos()

        # Dibujar los botones
        ventana.blit(jugar, (130, 200))
        ventana.blit(jugar2, (500, 200))
        ventana.blit(jugar3, (900, 200))
        ventana.blit(regresar, (65, 70))
        ventana.blit(home, (1100, 70))
        ventana.blit(bote, (210, 370))
        ventana.blit(bote2, (590, 370))
        ventana.blit(bote3, (990, 370))

        # Obtener los rectángulos de los botones
        boton1_rect = jugar.get_rect(topleft=(130, 200))
        boton2_rect = jugar2.get_rect(topleft=(500, 200))
        boton3_rect = jugar3.get_rect(topleft=(900, 200))
        home_rect = home.get_rect(topleft=(1100, 70))
        bote_rect = bote.get_rect(topleft=(210, 370))
        bote2_rect = bote2.get_rect(topleft=(590, 370))
        bote3_rect = bote3.get_rect(topleft=(990, 370))
        nivel1facil_rect = regresar.get_rect(topleft=(65, 70))

        if configuraciones.idioma == "español":
            texto_saludo = fuente.render("Niveles", True, color_negro)
        elif configuraciones.idioma == "inglés":
            texto_saludo = fuente.render("Levels", True, color_negro)
        
        ventana.blit(texto_saludo, (540, 42))

        # Verificar clics y ejecutar funciones
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

        if boton1_rect.collidepoint((mx, my)):
            if clic:
                nivel1fa.main()
        elif home_rect.collidepoint((mx, my)):
            if clic:
                menu.menu_principal()
        elif bote_rect.collidepoint((mx, my)):
            if clic:
                organica1.organica()
        elif bote2_rect.collidepoint((mx, my)):
            if clic:
                reciclable1.reciclable()
        elif bote3_rect.collidepoint((mx, my)):
            if clic:
                noreciclable1.noreciclable()
        elif boton2_rect.collidepoint((mx, my)):
            if clic:
                nivel2fa.main()

        elif boton3_rect.collidepoint((mx, my)):
            if clic:
                nivel3fa.main()

        elif nivel1facil_rect.collidepoint((mx, my)):
            if clic:
                dificultad.dificultad()

        clic = False

        pygame.display.update()
        relojPrincipal.tick(60)

# Iniciar el menú principal
if __name__ == "__main__":
    selector()