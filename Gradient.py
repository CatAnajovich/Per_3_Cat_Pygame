import pygame

y = 0
dir = .1
running = 1
barheight = 124
Height = 600
Width = 800
ColorGrad = int((255 / barheight)*2)   #Number of color spots each line has to jump
ColorHeight = int((barheight / 2)+ 1)  #How tall the color bar is
screen = pygame.display.set_mode((Width, Height));

barcolor = []
for i in range(1, ColorHeight):
	barcolor.append((i*ColorGrad, 0, i*ColorGrad))
for i in range(1, ColorHeight):
	barcolor.append((255 - i*ColorGrad, 0, 255 - i*ColorGrad))

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0

	screen.fill((0, 0, 0))
	for i in range(0, barheight):
		pygame.draw.line(screen, barcolor[i], (0, y+i), (Width - 1, y+i))

	y += dir
	if y + barheight > (Height - 1) or y < 0:
		dir *= -1

	pygame.display.flip()
	