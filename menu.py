import pygame

pygame.init()

# Definir los colores que se van a utilizar
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Definir la fuente que se va a utilizar para el texto
fuente = pygame.font.Font(None, 36)

# Definir la pantalla y el reloj
tamaño_pantalla = (800, 600)
pantalla = pygame.display.set_mode(tamaño_pantalla)
pygame.display.set_caption("Menú de juego")
reloj = pygame.time.Clock()

# Definir los rectángulos para los botones
boton1 = pygame.Rect(170, 515, 100, 50)
boton2 = pygame.Rect(290, 515, 100, 50)
boton3 = pygame.Rect(410, 515, 100, 50)
boton4 = pygame.Rect(530, 515, 100, 50)

# Bucle principal del juego
terminado = False

while not terminado:

    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Si el usuario hace clic en un botón
            if boton1.collidepoint(evento.pos):
                print("Opción 1 seleccionada")
            elif boton2.collidepoint(evento.pos):
                print("Opción 2 seleccionada")
            elif boton3.collidepoint(evento.pos):
                print("Opción 3 seleccionada")
            elif boton4.collidepoint(evento.pos):
                print("Opción 4 seleccionada")

    # Dibujar la pantalla
    pantalla.fill(BLANCO)

    # Dibujar los botones
    pygame.draw.rect(pantalla, AZUL, boton1)
    pygame.draw.rect(pantalla, VERDE, boton2)
    pygame.draw.rect(pantalla, ROJO, boton3)
    pygame.draw.rect(pantalla, NEGRO, boton4)

    # Dibujar el texto de los botones
    texto1 = fuente.render("Opción 1", True, BLANCO)
    texto2 = fuente.render("Opción 2", True, BLANCO)
    texto3 = fuente.render("Opción 3", True, BLANCO)
    texto4 = fuente.render("Opción 4", True, BLANCO)
    pantalla.blit(texto1, (boton1.left+10, boton1.top+10))
    pantalla.blit(texto2, (boton2.left+10, boton2.top+10))
    pantalla.blit(texto3, (boton3.left+10, boton3.top+10))
    pantalla.blit(texto4, (boton4.left+10, boton4.top+10))

    # Actualizar la pantalla
    pygame.display.flip()

    # Esperar al siguiente fotograma
    reloj.tick(60)

# Salir del juego
pygame.quit()
