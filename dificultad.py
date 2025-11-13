import pygame
import sys
import menu
import selector_basico
import selector_avanzado
import configuraciones
import ayudar

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

# Recursos para botones
jugar = pygame.image.load("recursos/botones/BotonDificultad.png")
jugar.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
jugar = pygame.transform.scale(jugar, (300, 80))

# Recursos para botones
ayuda = pygame.image.load("recursos/botones/BotonAyuda.png")
ayuda.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
ayuda = pygame.transform.scale(ayuda, (100, 90))

jugar2 = pygame.image.load("recursos/botones/BotonDificultad.png")
jugar2.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
jugar2 = pygame.transform.scale(jugar2, (300, 80))

regresar = pygame.image.load("recursos/botones/botonregregsar.png")
regresar.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
regresar = pygame.transform.scale(regresar, (70, 70))

# Fuente y tamaño del texto
fuentemax = pygame.font.SysFont("PixAntiqua", 60)
fuentemid = pygame.font.SysFont("PixAntiqua", 45)
fuentemin = pygame.font.SysFont("PixAntiqua", 25)


# Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Variable para controlar el clic del ratón
clic = False

# Función para el menú principal
def dificultad():
    clic = False
    while True:
        ventana.blit(fondo, (0, 0))

        # Obtener la posición del ratón
        mx, my = pygame.mouse.get_pos()

        # Dibujar el botón
        ventana.blit(jugar, (150, 130))

        # Dibujar el botón
        ventana.blit(ayuda, (580, 400))

        # Dibujar el botón
        ventana.blit(jugar2, (820, 130))

        # Dibujar el botón de regresar
        ventana.blit(regresar, (70, 70))

        # Obtener el rectángulo del botón jugar 1
        boton1_rect = jugar.get_rect(topleft=(150, 130))

        # Obtener el rectángulo del botón
        ayuda_rect = ayuda.get_rect(topleft=(580, 400))

        # Obtener el rectángulo del botón juag 2
        boton2_rect = jugar2.get_rect(topleft=(820, 130))

        # Obtener el rectángulo del botón
        regresar_rect = regresar.get_rect(topleft=(70, 70))

        if configuraciones.idioma == "español":
            texto_seleccionar = fuentemax.render("Dificultad", False, color_negro)
            ventana.blit(texto_seleccionar, (510, 43))
            texto_boton1 = fuentemid.render("Basico", False, color_negro)
            ventana.blit(texto_boton1, (210, 150))
            texto_boton2 = fuentemid.render("Avanzado", False, color_negro)
            ventana.blit(texto_boton2, (865, 150))
            texto_boton2 = fuentemid.render("Ayuda", False, color_negro)
            ventana.blit(texto_boton2, (570, 497))
           #Instrucciones Faciles
            instfacil=fuentemin.render("Objetivo: Recolectar 5 objetos",False, color_negro)
            ventana.blit(instfacil, (140,300-30))
            instfacil2=fuentemin.render("dependiendo del color del bote",False, color_negro)
            ventana.blit(instfacil2, (140,330-30))
            instfacil3=fuentemin.render("de basura.",False, color_negro)
            ventana.blit(instfacil3, (240,360-30))
            instfacil4=fuentemin.render("Tiempo: 6O segundos",False, color_negro)
            ventana.blit(instfacil4, (170,420-30))
            #Instrucciones Dificiles
            instdificil=fuentemin.render("Objetivo: Recolectar 5 objetos",False, color_negro)
            ventana.blit(instdificil, (800,300-30))
            instdificil2=fuentemin.render("dependiendo del color del bote",False, color_negro)
            ventana.blit(instdificil2, (800,330-30))
            instdificil3=fuentemin.render("de basura.",False, color_negro)
            ventana.blit(instdificil3, (900,360-30))
            instdificil4=fuentemin.render("Tiempo: 45 segundos",False, color_negro)
            ventana.blit(instdificil4, (850,420-30))
            instdificil5=fuentemin.render("*Si te equivocas 3 veces, pierdes*",False, color_negro)
            ventana.blit(instdificil5, (780,480-30))
        elif configuraciones.idioma == "inglés":
            texto_seleccionar = fuentemax.render("Difficulty", True, color_negro)
            ventana.blit(texto_seleccionar, (510, 43))
            texto_boton1 = fuentemid.render("Basic", True, color_negro)
            ventana.blit(texto_boton1, (245, 149))
            texto_boton2 = fuentemid.render("Advanced", True, color_negro)
            ventana.blit(texto_boton2, (855, 150))
            texto_boton2 = fuentemid.render("Help", False, color_negro)
            ventana.blit(texto_boton2, (580, 497))
            #Instrucciones Faciles
            instfacil=fuentemin.render("Objective: Collect 5 items",False, color_negro)
            ventana.blit(instfacil, (160,300-30))
            instfacil2=fuentemin.render("depending on the color of the trash",False, color_negro)
            ventana.blit(instfacil2, (100,330-30))
            instfacil3=fuentemin.render("can.",False, color_negro)
            ventana.blit(instfacil3, (260,360-30))
            instfacil4=fuentemin.render("Time: 6O seconds",False, color_negro)
            ventana.blit(instfacil4, (190,420-30))
            #Instrucciones Dificiles
            instdificil=fuentemin.render("Objective: Collect 5 items",False, color_negro)
            ventana.blit(instdificil, (820,300-30))
            instdificil2=fuentemin.render("depending on the color of the trash",False, color_negro)
            ventana.blit(instdificil2, (760,330-30))
            instdificil3=fuentemin.render("can",False, color_negro)
            ventana.blit(instdificil3, (930,360-30))
            instdificil4=fuentemin.render("Time: 45 seconds",False, color_negro)
            ventana.blit(instdificil4, (870,420-30))
            instdificil5=fuentemin.render("*If you are wrong 3 times, you lose*",False, color_negro)
            ventana.blit(instdificil5, (765,480-30))
        # Verificar si el ratón está sobre el botón
        if boton1_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
                selector_basico.selector()
        # Verificar si se hizo clic
        if ayuda_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
                ayudar.ayudar()

        # Verificar si el ratón está sobre el botón
        if boton2_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
                selector_avanzado.selector()

        if regresar_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
                menu.menu_principal()  # Llamar a la función de menu

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
    dificultad()