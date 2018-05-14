import pygame

x = 0
y = 0
Dir  = 1 
Width = 800
Height = 600
screen = pygame.display.set_mode((Width, Height))
linecolor = 255, 0, 0
bgcolor = 0, 0, 0

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	
	screen.fill(bgcolor)
	pygame.draw.line(screen, linecolor, (0, y), (Width-1, y))
	
	y = y + Dir
	if y == 0 or y == Height - 1:
		Dir = Dir * 1
		
	pygame.draw.line(screen, linecolor, (x, 0), (x, Height - 1))
	
	x = x + Dir
	if x == 0 or x == Width - 1:
		Dir = Dir * 1
		
	pygame.display.flip()
	