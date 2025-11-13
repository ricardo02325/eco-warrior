import pygame
import sys
import random
import ganar 
import perder
import configuraciones

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Equipo 3")

# Cargar fondo
background = pygame.image.load("recursos/fondos/nivel11.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Cargar imágenes para el jugador y los objetos que caen
playerDerecha1 = pygame.image.load('recursos/personaje/animacionderecha/1Right1.png')
playerDerecha2 = pygame.image.load('recursos/personaje/animacionderecha/1Right2.png')
playerDerecha3 = pygame.image.load('recursos/personaje/animacionderecha/1Right3.png')
playerDerecha4 = pygame.image.load('recursos/personaje/animacionderecha/1Right4.png')
playerDerecha5 = pygame.image.load('recursos/personaje/animacionderecha/1Right5.png')
playerDerecha6 = pygame.image.load('recursos/personaje/animacionderecha/1Right6.png')


playerIzquierda1 = pygame.image.load('recursos/personaje/animacionizquierda/1Left1.png')
playerIzquierda2 = pygame.image.load('recursos/personaje/animacionizquierda/1Left2.png')
playerIzquierda3 = pygame.image.load('recursos/personaje/animacionizquierda/1Left3.png')
playerIzquierda4 = pygame.image.load('recursos/personaje/animacionizquierda/1Left4.png')
playerIzquierda5 = pygame.image.load('recursos/personaje/animacionizquierda/1Left5.png')
playerIzquierda6 = pygame.image.load('recursos/personaje/animacionizquierda/1Left6.png')

#Basura organica
extra_object1_image = pygame.image.load("recursos/basura_organica/banana.png")
extra_object1_image = pygame.transform.scale(extra_object1_image, (50, 50))

extra_object2_image = pygame.image.load("recursos/basura_organica/cascara_de_huevo.png")
extra_object2_image = pygame.transform.scale(extra_object2_image, (50, 50))

extra_object3_image = pygame.image.load("recursos/basura_organica/cascara_de_sandia.png")
extra_object3_image = pygame.transform.scale(extra_object3_image, (50, 50))

red_object_image = pygame.image.load("recursos/basura_organica/manzana.png")
red_object_image = pygame.transform.scale(red_object_image, (50, 50))

blue_object_image = pygame.image.load("recursos/basura_organica/pescao.png")
blue_object_image = pygame.transform.scale(blue_object_image, (50, 50))

green_object_image = pygame.image.load("recursos/basura_organica/hueso.png")
green_object_image = pygame.transform.scale(green_object_image, (50, 50))

#Basura reciclable
extra_object4_image = pygame.image.load("recursos/basura_recicable/bolsa_de_papel.png")
extra_object4_image = pygame.transform.scale(extra_object4_image, (50, 50))

extra_object5_image = pygame.image.load("recursos/basura_recicable/botella_de_vidrio.png")
extra_object5_image = pygame.transform.scale(extra_object5_image, (50, 50))

extra_object6_image = pygame.image.load("recursos/basura_recicable/lata.png")
extra_object6_image = pygame.transform.scale(extra_object6_image, (60, 60))

extra_object7_image = pygame.image.load("recursos/basura_recicable/libro.png")
extra_object7_image = pygame.transform.scale(extra_object7_image, (60, 60))

extra_object8_image = pygame.image.load("recursos/basura_recicable/sobre.png")
extra_object8_image = pygame.transform.scale(extra_object8_image, (60, 60))

yellow_object_image = pygame.image.load("recursos/basura_recicable/lata_refresco.png")
yellow_object_image = pygame.transform.scale(yellow_object_image, (50, 50))

purple_object_image = pygame.image.load("recursos/basura_recicable/hoja_de_periodico.png")
purple_object_image = pygame.transform.scale(purple_object_image, (50, 50))

orange_object_image = pygame.image.load("recursos/basura_recicable/botella_de_plastico.png")
orange_object_image = pygame.transform.scale(orange_object_image, (50, 50))

#Basura no reciclable
extra_object9_image = pygame.image.load("recursos/basura_no_recicable/bateria.png")
extra_object9_image = pygame.transform.scale(extra_object9_image, (50, 50))

extra_object10_image = pygame.image.load("recursos/basura_no_recicable/bolsa_de_plastico.png")
extra_object10_image = pygame.transform.scale(extra_object10_image, (50, 50))

extra_object11_image = pygame.image.load("recursos/basura_no_recicable/telefono.png")
extra_object11_image = pygame.transform.scale(extra_object11_image, (50, 50))

extra_object12_image = pygame.image.load("recursos/basura_no_recicable/tenedor.png")
extra_object12_image = pygame.transform.scale(extra_object12_image, (50, 50))

pink_object_image = pygame.image.load("recursos/basura_no_recicable/cd.png")
pink_object_image = pygame.transform.scale(pink_object_image, (50, 50))

cyan_object_image = pygame.image.load("recursos/basura_no_recicable/foco.png")
cyan_object_image = pygame.transform.scale(cyan_object_image, (50, 50))

brown_object_image = pygame.image.load("recursos/basura_no_recicable/television.png")
brown_object_image = pygame.transform.scale(brown_object_image, (50, 50))

gray_object_image = pygame.image.load("recursos/basura_no_recicable/colilla_de _cigarro.png")
gray_object_image = pygame.transform.scale(gray_object_image, (50, 50))

# Variable para poder poner el tiempo en reversa
auxiliar = 0

# Puntos y vidas
puntos = 0
vidas = 3

# Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Crear una fuente para el texto
fuente = pygame.font.SysFont(None, 35)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = False
        self.direction = "derecha"
        self.sprites = self.load_sprites("derecha")
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.speed = 5

    def load_sprites(self, direction):
        if direction == "derecha":
            return [
                pygame.transform.scale(playerDerecha1, (48, 119)),
                pygame.transform.scale(playerDerecha2, (48, 119)),
                pygame.transform.scale(playerDerecha3, (48, 119)),
                pygame.transform.scale(playerDerecha4, (48, 119)),
                pygame.transform.scale(playerDerecha5, (48, 119)),
                pygame.transform.scale(playerDerecha6, (48, 119)),
            ]
        elif direction == "izquierda":
            return [
                pygame.transform.scale(playerIzquierda1, (48, 119)),
                pygame.transform.scale(playerIzquierda2, (48, 119)),
                pygame.transform.scale(playerIzquierda3, (48, 119)),
                pygame.transform.scale(playerIzquierda4, (48, 119)),
                pygame.transform.scale(playerIzquierda5, (48, 119)),
                pygame.transform.scale(playerIzquierda6, (48, 119)),
            ]

    def update(self, speed):
        self.current_sprite += speed
        if int(self.current_sprite) >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

        # Actualizamos la posición del rectángulo según la dirección
        if self.direction == "derecha":
            self.rect.x += 5
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
        elif self.direction == "izquierda":
            self.rect.x -= 5
            if self.rect.left < 0:
                self.rect.left = 0

def show_pause_menu():
    #Texto a mostrar en la pantalla
    pause_font = pygame.font.SysFont(None, 100)
    pause_text = pause_font.render("Juego pausado", True, (255, 255, 255))
    pause_rect = pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    #Fondo trans´parente para la pantalla de pausa
    pause_background = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(pause_background, (0, 0, 0, 128), pause_background.get_rect())
    
    screen.blit(pause_background, (0, 0))
    screen.blit(pause_text, pause_rect)
    pygame.display.flip()

    #Pausar el juego cuando se presione la tecla p
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

        relojPrincipal.tick(60)

# Listas para almacenar objetos que caen
falling_objects_extra1 = []
falling_objects_extra2 = []
falling_objects_extra3 = []
falling_objects_extra4 = []
falling_objects_extra5 = []
falling_objects_extra6 = []
falling_objects_extra7 = []
falling_objects_extra8 = []
falling_objects_extra9 = []
falling_objects_extra10 = []
falling_objects_extra11 = []
falling_objects_extra12 = []
falling_objects_red = []
falling_objects_blue = []
falling_objects_green = []
falling_objects_yellow = []
falling_objects_purple = []
falling_objects_orange = []
falling_objects_pink = []
falling_objects_cyan = []
falling_objects_brown = []
falling_objects_gray = []

#Crear spreites y grupos
moving_sprites = pygame.sprite.Group()
player = Player(640, 550)
moving_sprites.add(player)

def draw_falling_objects(objects, image):
    for obj in objects:
        screen.blit(image, obj)

def draw_pause_menu():
    font = pygame.font.SysFont(None, 100)
    text = font.render("PAUSA", True, (255, 0, 0))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

def main():
    global moving_sprites, auxiliar, puntos, vidas

    running = True
    musica = pygame.mixer.music.load("recursos/musica/nivel1.mp3")
    musica = pygame.mixer.music.play(-1)
    volumen = configuraciones.volumen_actual

    tiempo_inicial = pygame.time.get_ticks()  # Obtener el tiempo inicial

    while running:
        musica = pygame.mixer.music.set_volume(volumen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.direction = "derecha"
                elif event.key == pygame.K_LEFT:
                    player.direction = "izquierda"
                elif event.key == pygame.K_p:
                    show_pause_menu()
        
        player.sprites = player.load_sprites(player.direction)
        
        # Calcular el tiempo restante
        tiempo_max = 60  # Tiempo máximo en segundos
        tiempo_juego = (pygame.time.get_ticks() - tiempo_inicial) // 1000
        tiempo = tiempo_max - tiempo_juego

        screen.blit(background, (0, 0))


        if auxiliar != tiempo:
            auxiliar = tiempo

        if puntos < 0:
            puntos = 0

        # Generar objetos que caen aleatoriamente
        if random.randint(1, 100) < 3:
            obj_width = 20
            obj_height = 20
            obj_x = random.randint(0, WIDTH - obj_width)
            obj_y = 0
            rand_num = random.randint(1, 22)
            if rand_num == 1:
                falling_objects_red.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 2:
                falling_objects_blue.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 3:
                falling_objects_green.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 4:
                falling_objects_yellow.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 5:
                falling_objects_purple.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 6:
                falling_objects_orange.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 7:
                falling_objects_pink.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 8:
                falling_objects_cyan.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 9:
                falling_objects_brown.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 10:
                falling_objects_gray.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 11:
                falling_objects_extra1.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 12:
                falling_objects_extra2.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 13:
                falling_objects_extra3.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 14:
                falling_objects_extra4.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 15:
                falling_objects_extra5.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 16:
                falling_objects_extra6.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 17:
                falling_objects_extra7.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 18:
                falling_objects_extra8.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 19:
                falling_objects_extra9.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 20:
                falling_objects_extra10.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 21:
                falling_objects_extra11.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 22:
                falling_objects_extra12.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))

        # Mover y eliminar objetos que caen
        for obj in falling_objects_red:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_red.remove(obj)

        for obj in falling_objects_blue:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_blue.remove(obj)

        for obj in falling_objects_green:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_green.remove(obj)

        for obj in falling_objects_yellow:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_yellow.remove(obj)

        for obj in falling_objects_purple:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_purple.remove(obj)

        for obj in falling_objects_orange:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_orange.remove(obj)

        for obj in falling_objects_pink:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_pink.remove(obj)

        for obj in falling_objects_cyan:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_cyan.remove(obj)

        for obj in falling_objects_brown:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_brown.remove(obj)

        for obj in falling_objects_gray:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_gray.remove(obj)

        for obj in falling_objects_extra1:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_extra1.remove(obj)

        for obj in falling_objects_extra2:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_extra2.remove(obj)

        for obj in falling_objects_extra3:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_extra3.remove(obj)

        for obj in falling_objects_extra4:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_extra4.remove(obj)

        for obj in falling_objects_extra5:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_extra5.remove(obj)

        for obj in falling_objects_extra6:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_extra6.remove(obj)

        for obj in falling_objects_extra7:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_extra7.remove(obj)

        for obj in falling_objects_extra8:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_extra8.remove(obj)

        for obj in falling_objects_extra9:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_extra9.remove(obj)

        for obj in falling_objects_extra10:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_extra10.remove(obj)

        for obj in falling_objects_extra11:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_extra11.remove(obj)

        for obj in falling_objects_extra12:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_extra12.remove(obj)

        # Detectar colisiones con objetos rojos
        for obj in falling_objects_red:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos += 1
                falling_objects_red.remove(obj)

        # Detectar colisiones con objetos azules
        for obj in falling_objects_blue:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto azul!")
                puntos += 1
                falling_objects_blue.remove(obj)

        # Detectar colisiones con objetos verdes
        for obj in falling_objects_green:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto verde!")
                puntos += 1
                falling_objects_green.remove(obj)

        for obj in falling_objects_yellow:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_yellow.remove(obj)

        for obj in falling_objects_purple:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_purple.remove(obj)

        for obj in falling_objects_orange:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_orange.remove(obj)

        for obj in falling_objects_pink:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_pink.remove(obj)

        for obj in falling_objects_cyan:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_cyan.remove(obj)

        for obj in falling_objects_brown:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_brown.remove(obj)

        for obj in falling_objects_gray:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_gray.remove(obj)

        for obj in falling_objects_extra1:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos += 1
                falling_objects_extra1.remove(obj)

        for obj in falling_objects_extra2:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos += 1
                falling_objects_extra2.remove(obj)

        for obj in falling_objects_extra3:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos += 1
                falling_objects_extra3.remove(obj)

        for obj in falling_objects_extra4:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_extra4.remove(obj)

        for obj in falling_objects_extra5:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_extra5.remove(obj)

        for obj in falling_objects_extra6:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_extra6.remove(obj)

        for obj in falling_objects_extra7:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_extra7.remove(obj)

        for obj in falling_objects_extra8:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_extra8.remove(obj)

        for obj in falling_objects_extra9:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_extra9.remove(obj)

        for obj in falling_objects_extra10:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_extra10.remove(obj)

        for obj in falling_objects_extra11:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_extra11.remove(obj)

        for obj in falling_objects_extra12:
            if player.rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                vidas -=1
                falling_objects_extra12.remove(obj)
        
        # Limpiar la pantalla
        # screen.fill((0, 0, 0))

        # Dibujar el objeto móvil y los objetos que caen
        moving_sprites.draw(screen)
        moving_sprites.update(0.25)
        draw_falling_objects(falling_objects_red, red_object_image)
        draw_falling_objects(falling_objects_blue, blue_object_image)
        draw_falling_objects(falling_objects_green, green_object_image)
        draw_falling_objects(falling_objects_yellow, yellow_object_image)
        draw_falling_objects(falling_objects_purple, purple_object_image)
        draw_falling_objects(falling_objects_orange, orange_object_image)
        draw_falling_objects(falling_objects_pink, pink_object_image)
        draw_falling_objects(falling_objects_cyan, cyan_object_image)
        draw_falling_objects(falling_objects_brown, brown_object_image)
        draw_falling_objects(falling_objects_gray, gray_object_image)
        draw_falling_objects(falling_objects_extra1, extra_object1_image)
        draw_falling_objects(falling_objects_extra2, extra_object2_image)
        draw_falling_objects(falling_objects_extra3, extra_object3_image)
        draw_falling_objects(falling_objects_extra4, extra_object4_image)
        draw_falling_objects(falling_objects_extra5, extra_object5_image)
        draw_falling_objects(falling_objects_extra6, extra_object6_image)
        draw_falling_objects(falling_objects_extra7, extra_object7_image)
        draw_falling_objects(falling_objects_extra8, extra_object8_image)
        draw_falling_objects(falling_objects_extra9, extra_object9_image)
        draw_falling_objects(falling_objects_extra10, extra_object10_image)
        draw_falling_objects(falling_objects_extra11, extra_object11_image)
        draw_falling_objects(falling_objects_extra12, extra_object12_image)

        if configuraciones.idioma == "español":
        # Pon el tiempo en pantalla
            contador = fuente.render("Tiempo: " + str(tiempo), 0, (0, 0, 0))
            screen.blit(contador, (10, 10))

        # Mostrar puntos en pantalla
            puntos_text = fuente.render("Puntos: " + str(puntos) + " /5", 0, (0, 0, 0))
            screen.blit(puntos_text, (WIDTH - 160, 10))
        
            vidas_text = fuente.render("Vidas: " + str(vidas), 0, (0,0,0))
            screen.blit(vidas_text, (WIDTH - 270, 10))
        
        elif configuraciones.idioma == "inglés":
        # Pon el tiempo en pantalla
            contador = fuente.render("Time: " + str(tiempo), 0, (0, 0, 0))
            screen.blit(contador, (10, 10))

        # Mostrar puntos en pantalla
            puntos_text = fuente.render("Points: " + str(puntos) + " /5", 0, (0, 0, 0))
            screen.blit(puntos_text, (WIDTH - 150, 10))

            vidas_text = fuente.render("Lifes: " + str(vidas), 0, (0,0,0))
            screen.blit(vidas_text, (WIDTH - 270, 10))

        # Verificar si se han alcanzado 5 puntos
        if puntos >= 5:
            ganar.ganaste()   
        if tiempo == 0:
            perder.lose()
        if vidas == 0:
            perder.lose()    

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad del juego
        relojPrincipal.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()