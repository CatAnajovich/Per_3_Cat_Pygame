import pygame

print("Please choose a screen size, X Y")
X = int(input())
Y = int(input())

screen = pygame.display.set_mode((X, Y))

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break