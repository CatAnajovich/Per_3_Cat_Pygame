import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
degree = 0

while True:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		break
	
	screen.fill((40, 40, 40))
	
	surf = pygame.Surface((100, 100))
	surf.fill((255, 255, 255))
	surf.set_colorkey((255, 0, 0))
	
	bigger = pygame.Rect(0, 0, 100, 50)
	smaller = pygame.Rect(25, 50, 50, 50)
	
	pygame.draw.rect(surf, (100, 0, 0), bigger)
	pygame.draw.rect(surf, (0, 0, 100), smaller)
	
	where = 200, 200
	
	blittedRect = screen.blit(surf, where)
	
	oldCenter = blittedRect.center
	
	rotatedSurf = pygame.transform.rotate(surf, degree)
	
	rotRect = rotatedSurf.get_rect()
	rotRect.center = oldCenter
	
	screen.blit(rotatedSurf, rotRect)
	
	degree += 5
	if degree > 360:
		degree = 0
	
	pygame.display.flip()
	
	pygame.time.wait(60)