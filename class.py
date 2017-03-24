import pygame
class player(pygame.sprite.Sprite):
	def __init__(self,imagen):
		self.imagen=imagen
		self.rect=self.imagen.get_rect()
		self.rect.top,self.rect.left=300,200
	def mover(self,vx,vy):
		self.rect.move_ip(vx,vy)
	def update(self,superficie):
		superficie.blit(self.imagen,self.rect)

def main():
	import pygame
	pygame.init()
	pantalla=pygame.display.set_mode((800,800))
	reloj1=pygame.time.Clock()
	salir=False
	negro=(0,0,0)
	imagen1=pygame.image.load("nave2b.png")
	player1=player(imagen1)
	vx,vy=0,0
	velocidad=10
	
	while salir!=True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				salir=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_w:
					vy=-velocidad
				if event.key==pygame.K_s:
					vy=velocidad
				if event.key==pygame.K_a:
					vx=-velocidad
				if event.key==pygame.K_d:
					vx=velocidad
			if event.type==pygame.KEYUP:
				if event.key==pygame.K_w:
					vy=0
				if event.key==pygame.K_s:
					vy=0
				if event.key==pygame.K_a:
					vx=0
				if event.key==pygame.K_d:
					vx=0
					
				
		reloj1.tick(20)
		player1.mover(vx,vy)
		pantalla.fill(negro)
		player1.update(pantalla)
		pygame.display.update()
	pygame.quit()
		
main()
