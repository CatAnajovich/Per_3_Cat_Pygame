import pygame

print("Please choose a screen size, X Y")
X = int(input())
Y = int(input())

screen = pygame.display.set_mode((X, Y))
UL = (0, 0)
UR = (X, 0)
LL = (0, Y)
LR = (X, Y)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 140, 0)
PURPLE = (255, 0, 255)

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	screen.fill((255,228,225))
	pygame.draw.line(screen, (BLUE), (UL), (LR))
	pygame.draw.line(screen, (GREEN), (UR), (LL))
	pygame.draw.line(screen, (RED), (X/2, 0), (X/2, Y))
	pygame.draw.line(screen, (YELLOW), (0, Y/2), (X, Y/2))
	pygame.display.flip()