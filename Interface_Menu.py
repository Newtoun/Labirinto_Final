import pygame
import Botao
from Gera_labirinto_automatico import Gera_labirinto_automatico
from Gera_labirinto_manual import Gera_labirinto_manual
from interface import interface
from Estado import Estado
from Gabarito import Gabarito
#cria display
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
fundo_Imagem = pygame.image.load("fundo.png")
fundo_Imagem2 = pygame.image.load("fundoTarde.png")
fundo_Imagem3 = pygame.image.load("fundoEstrelado.png")


tamanho_Matriz = (None,None)

def Tela_inicial():#tela inicial
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')

	#carrega as imagens usada na tela
	falaAjuda = pygame.image.load('meajuda.png').convert_alpha()
	falaRaff = pygame.image.load('souoRafa.png').convert_alpha()
	the_maze = pygame.image.load('themaze.png').convert_alpha()
	start_img = pygame.image.load('save.png').convert_alpha()
	rafael_img = pygame.image.load('raff.png').convert_alpha()
	rafael_img2 = pygame.image.load('raffEsq.png').convert_alpha()

	#cria uma instancia de botao na classe botao
	rafael2 = Botao.Button(600,335,rafael_img2,0.8)
	rafael3 = Botao.Button(125,335,rafael_img,0.8)
	the_maze_screen = Botao.Button(100,25,the_maze,1)
	start_button = Botao.Button(300, 300, start_img, 0.8)
	
	#looping onde o jogo comeca
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem, (0, 0))
		the_maze_screen.draw(screen)
		rafael2.draw(screen)
		rafael3.draw(screen)
		screen.blit(falaRaff, (25, 275))
		screen.blit(falaAjuda, (650, 275))

		if start_button.draw(screen):
			pygame.quit()
			pygame.time.delay(100)
			Tela_Nivel()
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()



	pygame.quit()

def Tela_Nivel():
	global tamanho_Matriz
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')
	nv_Dificuldade = pygame.image.load("nivel_De_Dificuldade.png")

	#carrega a s imagens

	nivel1_img = pygame.image.load('nivel1.png').convert_alpha()
	nivel2_img = pygame.image.load('nivel2.png').convert_alpha()
	nivel3_img = pygame.image.load('nivel3.png').convert_alpha()
	fundo27_img = pygame.image.load('27fundo.png').convert_alpha()
	fundo37_img = pygame.image.load('37fundo.png').convert_alpha()
	fundo53_img = pygame.image.load('53fundo.png').convert_alpha()


	#cria uma instancia de botao na classe botao
	
	nivel1_button = Botao.Button(250, 240, nivel1_img, 0.8)
	nivel2_button = Botao.Button(250, 325, nivel2_img, 0.8)
	nivel3_button = Botao.Button(250, 410, nivel3_img, 0.8)

	
	#looping onde o jogo comeca
	interaction = 0
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem, (0, 0))
		screen.blit(nv_Dificuldade, (50, 0))
		screen.blit(fundo27_img,(450,250))
		screen.blit(fundo37_img,(450,335))
		screen.blit(fundo53_img,(450,425))


		if nivel1_button.draw(screen):
			tamanho_Matriz = (27,17)
			interaction+=1
			
		if nivel2_button.draw(screen):
			tamanho_Matriz = (37,27)
			interaction+=1		
		if nivel3_button.draw(screen):
			tamanho_Matriz = (53,27)
			interaction+=1
			

		if interaction>0:#finaliza tela
			run = False
			pygame.quit()
			pygame.time.delay(100)
			Tela_criar_labirinto()

		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
	pygame.quit()

def Tela_criar_labirinto():
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')
	criar_labirinto = pygame.image.load("criar_lab1.png")
	predio = pygame.image.load("predio.png")
	
	#carrega a s imagens
	manual_img = pygame.image.load('manuel.png').convert_alpha()
	auto_img = pygame.image.load('automaticButton.png').convert_alpha()
	#cria uma instancia de botao na classe botao
	manual_button = Botao.Button(250, 250, manual_img, 0.8)
	auto_button = Botao.Button(205, 360, auto_img, 0.8)
	#looping onde o jogo comeca
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem, (0, 0))
		screen.blit(criar_labirinto, (0, 25))
		screen.blit(predio, (600, 303))

		if manual_button.draw(screen):
			pygame.quit()
			pygame.time.delay(100)
			maze_manual = Gera_labirinto_manual(tamanho_Matriz[0],tamanho_Matriz[1])
			maze_manual.manual()
			
			tela_Resolver(maze_manual)
			return
		if auto_button.draw(screen):
			pygame.quit()
			pygame.time.delay(100)
			maze_automatico = Gera_labirinto_automatico(tamanho_Matriz[0],tamanho_Matriz[1])
			tela_Resolver(maze_automatico)
			return
		
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
	pygame.quit()

def tela_Resolver(labirinto):
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')
	criar_labirinto = pygame.image.load("resolver_lab1.png")
	predio = pygame.image.load("predio.png")
	
	#carrega a s imagens
	manual_img = pygame.image.load('manuel.png').convert_alpha()
	auto_img = pygame.image.load('automaticButton.png').convert_alpha()
	#cria uma instancia de botao na classe botao
	manual_button = Botao.Button(250, 250, manual_img, 0.8)
	auto_button = Botao.Button(205, 360, auto_img, 0.8)
	#looping onde o jogo comeca
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem, (0, 0))
		screen.blit(criar_labirinto, (0, 25))
		screen.blit(predio, (600, 303))

		if manual_button.draw(screen):
			pygame.quit()
			pygame.time.delay(100)
			jogo = interface(labirinto)
			resposta, movimentos = jogo.to_execute_Manual()
			if resposta== False:
				tela_Desistiu(labirinto)
			else:
				tela_Ganhou(movimentos)
			return
		if auto_button.draw(screen):
			pygame.quit()
			pygame.time.delay(100)
			jogo = interface(labirinto)
			resposta, movimentos = jogo.to_execute_Automatico()
			if resposta:
				pygame.quit()
				pygame.time.delay(100)
				tela_Sem_Solucao()
				return
			else:
				tela_Ganhou(movimentos)

			return
		
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
	pygame.quit()
	return

def tela_Ganhou(movimento):
	pygame.font.init() #instruções
	font_instrucoes2 = pygame.font.SysFont('Rockwell Extra Bold', 90)
	numMovimento = font_instrucoes2.render(str(movimento), 1, (0, 0, 0))
	####################################
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')
	parabens_img = pygame.image.load("parabens.png")
	raff = pygame.image.load("rafeChegou.png")  ##################FALTA DIVIDIFR NO MEIO
	trofeu = pygame.image.load("trofeu.png")
	trofeu2 = pygame.image.load("trofeu.png")
	
	#carrega a s imagens
	continuar_img = pygame.image.load('continuarButton.png').convert_alpha()
	move_img = pygame.image.load('move.png').convert_alpha()
	
	#cria uma instancia de botao na classe botao
	continuar_button = Botao.Button(225, 400, continuar_img, 0.8)
	
	#looping onde o jogo comeca
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem2, (0, 0))
		screen.blit(parabens_img, (140, 0))
		screen.blit(raff, (200,175))
		screen.blit(move_img, (215,270))
		screen.blit(numMovimento, (565,290))
		screen.blit(trofeu, (650,380))
		screen.blit(trofeu2, (75,380))

		if continuar_button.draw(screen):
			pygame.quit()
			pygame.time.delay(100)
			tela_Ganhou_Final()
			return
		
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
	pygame.quit()
def tela_Ganhou_Final():
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')
	predio = pygame.image.load("predio.png")
	
	continuar = pygame.image.load("continuar.png")
	
	#load button images
	yes_img = pygame.image.load('yes.png').convert_alpha()
	no_img = pygame.image.load('no.png').convert_alpha()
	rafael_img = pygame.image.load('raff.png').convert_alpha()

	#create button instances
	yes_button = Botao.Button(150, 190, yes_img, 0.8)
	no_button = Botao.Button(450, 190, no_img, 0.8)
	#game loop
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem, (0, 0))
		screen.blit(continuar, (170,50))
		screen.blit(rafael_img,(25,280))
		screen.blit(predio,(600,303))

		if yes_button.draw(screen):
			pygame.quit()
			pygame.time.delay(100)
			Tela_inicial()
			return
		if no_button.draw(screen):
			quit()
			run  = False
			return
		
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
	pygame.quit()

def tela_Sem_Solucao():
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')
	semSolucao_img = pygame.image.load("semSolucao.png")
	continuar = pygame.image.load("continuar.png")
	
	#carrega a s imagens
	yes_img = pygame.image.load('yes.png').convert_alpha()
	no_img = pygame.image.load('no.png').convert_alpha()
	#cria uma instancia de botao na classe botao
	yes_button = Botao.Button(150, 340, yes_img, 0.8)
	no_button = Botao.Button(450, 340, no_img, 0.8)
	#looping onde o jogo comeca
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem2, (0, 0))
		screen.blit(semSolucao_img, (140, 5))
		screen.blit(continuar, (150,200))

		if yes_button.draw(screen):
			pygame.quit()
			pygame.time.delay(100)
			Tela_inicial()
			return
		if no_button.draw(screen):
			run =  False
			quit()
			return
		
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
	pygame.quit()

################################################
def tela_Desistiu(labirinto):
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')
	semSolucao_img = pygame.image.load("rafaNaoChegou.png")
	continuar = pygame.image.load("voce.png")

	resolver_img = pygame.image.load('resolverAuto.png').convert_alpha()
	no_img = pygame.image.load('exitD.png').convert_alpha()

	resolver_button = Botao.Button(130, 310, resolver_img, 0.8)
	no_button = Botao.Button(450, 330, no_img, 0.8)

	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem2, (0, 0))
		screen.blit(semSolucao_img, (0, 5))
		screen.blit(continuar, (200,200))

		if resolver_button.draw(screen):
			pygame.quit()
			pygame.time.delay(100)
			jogo = interface(labirinto)
			resposta, movimentos = jogo.to_execute_Automatico()
			if resposta:
				pygame.quit()
				pygame.time.delay(100)
				tela_Sem_Solucao()
				return
			else:
				tela_Ganhou(movimentos)
			
		if no_button.draw(screen):
			run =  False
			quit()
		
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
	pygame.quit()
########################################

#Escolhe_Criacao_Labirinto()
#Tela_inicial()