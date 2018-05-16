import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
degree = 0

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	
	screen.fill((40, 40, 40))  #Screen color
	
	surf = pygame.Surface((100, 100))  #Size of square
	surf.fill((255, 255, 255)) #background of square
	surf.set_colorkey((255, 0, 0))  ##???
	
	bigger = pygame.Rect(0, 0, 100, 50) #(Xlocation, Y(L), Xsize, Y(S))
	smaller = pygame.Rect(0, 50, 50, 50)
	
	pygame.draw.rect(surf, (100, 0, 0), bigger) # (surf, (color), shape)
	pygame.draw.rect(surf, (0, 0, 100), smaller)
	
	where = 200, 200  #location on screen
	
	blittedRect = screen.blit(surf, where) #actually draws???
	
	oldCenter = blittedRect.center #get the center of the shape
	
	rotatedSurf = pygame.transform.rotate(surf, degree) #rotate???
	
	rotRect = rotatedSurf.get_rect() #scrub
	rotRect.center = oldCenter #roate around the center???
	
	screen.blit(rotatedSurf, rotRect) # or maybe this draws???
	
	degree += 5  #decides how much it rotates :]
	if degree > 360:
		degree = 0
	
	pygame.display.flip() #prints to screen??? Makes it work???
	
	pygame.time.wait(60) #how long it takes to rotate