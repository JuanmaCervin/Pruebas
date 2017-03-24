import pygame
pygame.init()

def main():
	pantalla=pygame.display.set_mode((800,800))
	reloj1=pygame.time.Clock()
	salir=False 
	blanco=(255,255,255)
	negro=(0,0,0)
	imagen1=pygame.image.load("nave2b.png")
	sprite1=pygame.sprite.Sprite()
	sprite1.image=imagen1
	sprite1.rect=imagen1.get_rect()
	sprite1.rect.top=50
	sprite1.rect.left=50
	(x,y)=(20,20)
	vx=0
	vy=0
	r1=pygame.Rect(250,70,25,500)
	
	
	
	while salir!=True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				salir=true
			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_s:
					vy+=10
				if event.key == pygame.K_w:
					vy-=10
				if event.key == pygame.K_a:
					vx-=10
				if event.key == pygame.K_d:
					vx+=10
				##if event.key == pygame.K_j:
					##disparo=pygame.rect(
					
			if event.type==pygame.KEYUP:
				if event.key == pygame.K_s:
					vy=0
				if event.key == pygame.K_w:
					vy=0
				if event.key == pygame.K_a:
					vx=0
				if event.key == pygame.K_d:
					vx=0
					
					
		(oldx,oldy)=(sprite1.rect.left,sprite1.rect.top)
		sprite1.rect.move_ip(vx,vy)
		if sprite1.rect.colliderect(r1):
			(sprite1.rect.left,sprite1.rect.top)=(oldx,oldy)
		reloj1.tick(20)
		pantalla.fill(negro)
		pygame.draw.rect(pantalla,(100,100,100),r1)
		pantalla.blit(sprite1.image,sprite1.rect)
		pygame.display.update()
		
main()

