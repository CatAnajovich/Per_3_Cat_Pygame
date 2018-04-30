import pygame

print("Please choose a screen size, X Y")
X = int(input())
Y = int(input())

screen = pygame.display.set_mode((X, Y))

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	screen.fill((255,228,225))
	pygame.display.flip()