import pygame
import random
import sys

# 1. CONFIGURACIÓN INICIAL (Tamaño tipo celular)
pygame.init()
ANCHO = 400  # Mas estrecho
ALTO = 600   # Alto para que la moneda caiga más tiempo
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atrapa la Moneda Movil")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("Arial", 30, bold=True)

# 2. CARGAR IMÁGENES (Ajustadas al tamaño pequeño)
imagen_canasta = pygame.image.load("canasta.png")
imagen_canasta = pygame.transform.scale(imagen_canasta, (80, 40)) # Canasta más pequeña

imagen_moneda = pygame.image.load("moneda.png")
imagen_moneda = pygame.transform.scale(imagen_moneda, (40, 40)) # Moneda más pequeña

# 3. CREAR LOS OBJETOS Y SUS VARIABLES
area_canasta = pygame.Rect(160, 530, 80, 40)
area_moneda = pygame.Rect(200, -50, 40, 40)

velocidad_canasta = 12
velocidad_moneda = 5
puntos = 0
vidas = 5
jugando = True

# 4. BUCLE PRINCIPAL
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if jugando:
        # MOVIMIENTO DE LA CANASTA
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and area_canasta.left > 0:
            area_canasta.x = area_canasta.x - velocidad_canasta
        if teclas[pygame.K_RIGHT] and area_canasta.right < ANCHO:
            area_canasta.x = area_canasta.x + velocidad_canasta

        # MOVIMIENTO DE LA MONEDA
        area_moneda.y = area_moneda.y + velocidad_moneda

        # SI ATRAPAS LA MONEDA
        if area_canasta.colliderect(area_moneda):
            puntos = puntos + 1
            area_moneda.y = -50
            area_moneda.x = random.randint(0, ANCHO - 40)
            if velocidad_moneda < 12:
                velocidad_moneda = velocidad_moneda + 0.3

        # SI LA MONEDA TOCA EL SUELO
        if area_moneda.y > ALTO:
            vidas = vidas - 1
            area_moneda.y = -50
            area_moneda.x = random.randint(0, ANCHO - 40)
            if vidas == 0:
                jugando = False

    # 5. DIBUJAR TODO
    pantalla.fill((135, 206, 235)) 

    pantalla.blit(imagen_canasta, area_canasta)
    pantalla.blit(imagen_moneda, area_moneda)

    # Textos adaptados al tamaño de pantalla
    texto_puntos = fuente.render("Puntos: " + str(puntos), True, (0, 0, 0))
    texto_vidas = fuente.render("Vidas: " + str(vidas), True, (200, 0, 0))
    
    pantalla.blit(texto_puntos, (10, 10))
    pantalla.blit(texto_vidas, (ANCHO - 110, 10))

    if jugando == False:
        mensaje = fuente.render("¡GAME OVER!", True, (255, 0, 0))
        # Centramos el mensaje de error
        pantalla.blit(mensaje, (ANCHO // 2 - 80, ALTO // 2))

    pygame.display.flip()
    reloj.tick(60)