import pygame, random

WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galactic Warriors")
clock = pygame.time.Clock()

def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_shield_bar(surface, x, y, percentage):
	BAR_LENGHT = 200
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("resources/player.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH // 2
		self.rect.bottom = HEIGHT - 10
		self.speed_x = 0
		self.shield = 100

	def update(self):
		self.speed_x = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -5
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0

	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet)
		bullets.add(bullet)
		laser_sound.play()

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(meteor_images)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-140, -100)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > HEIGHT + 10 or self.rect.left < -40 or self.rect.right > WIDTH + 40:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-140, - 100)
			self.speedy = random.randrange(1, 10)


class BigFigure(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((200, 200))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("resources/laser1.png")
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()

class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = explosion_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center 
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50 # VELOCIDAD DE LA EXPLOSION

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_anim):
				self.kill()
			else:
				center = self.rect.center
				self.image = explosion_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center


# Definir los rectángulos para los botones
boton1 = pygame.Rect(170, 515, 100, 50)
boton2 = pygame.Rect(290, 515, 100, 50)
boton3 = pygame.Rect(410, 515, 100, 50)
boton4 = pygame.Rect(530, 515, 100, 50)

def show_go_screen():
	screen.blit(background, [0,0])
	draw_text(screen, "Galactic Warriors", 65, WIDTH // 2, HEIGHT // 4)
	draw_text(screen, "Mueve tu nave de un lado a otro con las teclas de izquierda y derecha.", 22, WIDTH // 2, HEIGHT // 2.3)
	draw_text(screen, "Usa la barra espaciadora para disparar láseres a las naves enemigas.", 22, WIDTH // 2, HEIGHT // 2)
	draw_text(screen, "¡Consigue la mayor puntuación!", 22, WIDTH // 2, HEIGHT // 1.6)
	draw_text(screen, "", 27, WIDTH // 2, HEIGHT * 3/4)
	draw_text(screen, "MODO 1       MODO 2       MODO 3       MODO 4", 22, WIDTH // 2, HEIGHT // 1.15)
	
	mode1 = False
	mode2 = False
	mode3 = False
	mode4 = True
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# Si el usuario hace clic en un botón
				if boton1.collidepoint(event.pos):
					print("Opción 1 seleccionada")
					mode1 == True
					waiting = False
					
				elif boton2.collidepoint(event.pos):
					print("Opción 2 seleccionada")
					mode2 == True
					waiting = False
					
				elif boton3.collidepoint(event.pos):
					print("Opción 3 seleccionada")
					mode3 == True
					waiting = False
					
				elif boton4.collidepoint(event.pos):
					print("Opción 4 seleccionada")
					mode4 == True
					waiting = False
     
	return mode1, mode2, mode3, mode4

# Cargar imagen de fondo
background = pygame.image.load("resources/background.png").convert()

mode1, mode2, mode3, mode4 = show_go_screen()

meteor_images = []
meteor_list = []
if mode1:
	meteor_list = ["resources/meteorGrey_big1p.png", "resources/meteorGrey_big2p.png", "resources/meteorGrey_big3p.png",
					"resources/meteorGrey_med1p.png", "resources/meteorGrey_med2p.png", "resources/meteorGrey_small1.png",
					"resources/meteorGrey_small2.png", "resources/meteorGrey_tiny1p.png", "resources/meteorGrey_tiny2.png"]
elif mode2:
	meteor_list = ["resources/meteorGrey_big3.png", "resources/meteorGrey_med1.png", "resources/meteorGrey_med2.png"]
elif mode3:
	meteor_list = ["resources/meteorGrey_big1.png", "resources/meteorGrey_big2.png", "resources/meteorGrey_big1p.png",
				"resources/meteorGrey_med2p.png", "resources/meteorGrey_small1.png", "resources/meteorGrey_small2.png",
				"resources/meteorGrey_tiny1.png", "resources/meteorGrey_tiny2.png", "resources/meteorGrey_big4.png",
				"resources/meteorGrey_med1p.png", "resources/meteorGrey_med2.png", "resources/meteorGrey_small1.png", "resources/meteorGrey_small2.png",
				"resources/meteorGrey_tiny1p.png"]
elif mode4:
	meteor_list = ["resources/meteorGrey_big1.png", "resources/meteorGrey_big2.png", "resources/meteorGrey_big3.png", "resources/meteorGrey_big4.png",
				"resources/meteorGrey_med1.png", "resources/meteorGrey_med2.png", 
				"resources/meteorGrey_tiny1.png"]

for img in meteor_list:
	meteor_images.append(pygame.image.load(img).convert())


####----------------EXPLOSTION IMAGENES --------------
explosion_anim = []
for i in range(9):
	file = "resources/regularExplosion0{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(BLACK)
	img_scale = pygame.transform.scale(img, (70,70))
	explosion_anim.append(img_scale)



# Cargar sonidos
laser_sound = pygame.mixer.Sound("resources/laser5.ogg")
explosion_sound = pygame.mixer.Sound("resources/explosion.wav")
pygame.mixer.music.load("resources/music.ogg")
pygame.mixer.music.set_volume(0.2)

all_sprites = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(8):
	meteor = Meteor()
	all_sprites.add(meteor)
	meteor_list.add(meteor)

#Marcador / Score
score = 0
pygame.mixer.music.play(loops=-1)


#### ----------GAME
game_over = True

running = True
while running:
	if game_over:
		
		show_go_screen()

		game_over = False
		all_sprites = pygame.sprite.Group()
		meteor_list = pygame.sprite.Group()
		bullets = pygame.sprite.Group()

		player = Player()
		all_sprites.add(player)
		for i in range(8):
			meteor = Meteor()
			all_sprites.add(meteor)
			meteor_list.add(meteor)

		score = 0

	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()


	all_sprites.update()

	#colisiones - meteoro - laser
	hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)

	score_options = [50, 100, 200, -50, -25, 75]

	for hit in hits:
		random_score = random.choice(score_options)
		score += random_score
		#explosion_sound.play()
		explosion = Explosion(hit.rect.center)
		all_sprites.add(explosion)
		explosion_sound.play()
		meteor = Meteor()
		all_sprites.add(meteor)
		meteor_list.add(meteor)

	# Checar colisiones - jugador - meteoro
	hits = pygame.sprite.spritecollide(player, meteor_list, True)
	for hit in hits:
		player.shield -= 10
		meteor = Meteor()
		all_sprites.add(meteor)
		meteor_list.add(meteor)
		if player.shield <= 0:
			game_over = True

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	#Marcador
	draw_text(screen, str(score), 25, WIDTH // 2, 10)

	# Escudo.
	draw_shield_bar(screen, 10, 10, player.shield)

	pygame.display.flip()

#-------------------------------------------------SAMANTHA----------------------------
