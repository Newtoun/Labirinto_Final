import pygame

# Classe responsável por:
# - Gerar a imagem do botao na tela e verifica se houve ou nao o click do mouse encima do botao
class Button():
	def __init__(self, x, y, imag, escala):
		largura = imag.get_width()
		altura = imag.get_height()
		self.imagem = pygame.transform.scale(imag, (int(largura * escala), int(altura * escala)))
		self.rect = self.imagem.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
	
	# draw = verifica se há ou não click no botão plotado
	def draw(self, surface):
		action = False
		
		pos = pygame.mouse.get_pos() # pega a posicao do mouse na tela

		
		if self.rect.collidepoint(pos): # checa o mouse e as condicoes de click
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0: # caso nao seja pressionado retorna falso
			self.clicked = False

		surface.blit(self.imagem, (self.rect.x, self.rect.y))# desenha o bota na tela

		return action