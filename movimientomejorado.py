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
	imagen1=pygame.image.load("nave2b.png").convert_alpha()
	imagenfondo=pygame.image.load("fondo2.png").convert_alpha()
	
	
	
	player1=player(imagen1)
	
	
	#variables aux
	player1=player(imagen1)
	vx,vy=0,0
	velocidad=10
	Asa,Dsa,Wsa,Ssa=False,False,False,False
	
	while salir!=True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				salir=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_w:
					Wsa=True
					vy=-velocidad
				if event.key==pygame.K_s:
					Ssa=True
					vy=velocidad
				if event.key==pygame.K_a:
					Asa=True
					vx=-velocidad
				if event.key==pygame.K_d:
					Dsa=True
					vx=velocidad
			if event.type==pygame.KEYUP:
				if event.key==pygame.K_w:
					Wsa=False
					if Ssa:vy=velocidad
					else:vy=0
				if event.key==pygame.K_s:
					Ssa=False
					if Wsa: vy=-velocidad
					else:vy=0
				if event.key==pygame.K_a:
					Asa=False
					if Dsa: vx=velocidad
					else:vx=0
				if event.key==pygame.K_d:
					Dsa=False
					if Asa: vx=-velocidad
					else:vx=0
					
				
		reloj1.tick(20)
		player1.mover(vx,vy)
		pantalla.blit(imagenfondo,(0,0))
		player1.update(pantalla)
		pygame.display.update()
	pygame.quit()
		
main()
