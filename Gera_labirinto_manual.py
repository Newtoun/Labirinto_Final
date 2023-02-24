
from Ponto import Ponto
import pygame

speed = 25
x = y = 25

# Classe responsável por:
# - Disponibilizar a plotagem de uma matriz onde o jogador pode criar seu Proprio Labirinto
# e definir seu ponto final e inicial, onde retorna os mesmos.

class Gera_labirinto_manual:
    def __init__(self,largura,altura):
        self.largura  = largura
        self.altura = altura
        self.matriz = self.inicializa_Matriz_Zero()
        self.ponto_Inicial = Ponto(None,None)
        self.ponto_Final = Ponto(None,None)

        pygame.init()
        pygame.display.set_caption("Labirinto")
        self.screen = pygame.display.set_mode((self.largura*25,self.altura*25))

    # inicializa_Matriz_Zero = inicializa matriz onde todos os seus elementos são 0    
    def inicializa_Matriz_Zero(self):
        mat = []     
        for i in range(self.altura):
            lista = [0]*self.largura
            mat.append(lista)
        return mat
    
    # imprime_Matriz = imprime matriz
    def imprime_Matriz(self):
        for i in range(self.altura):
            for j in range(self.largura):
                print(self.matriz[i][j],end=" ")
            print()

    # game_map = Plota o labirinto
    def game_map(self, instrucaoP1, instrucaoP2, instrucaoP3):

        #---carregamento das imagens utilizadas durante a construção do labirinto---#
        caminho = pygame.image.load('chaoClaro.png').convert_alpha() 
        parede = pygame.image.load('parede.png').convert_alpha() 
        chaoEscuro = pygame.image.load('chaoEscuro.png').convert_alpha() 
        casa = pygame.image.load('casa.png').convert_alpha()
        #---------------------------------------------------------------------------#

        pygame.font.init() #inicializar o módulo de fonte para plotar Instruções para o jogador

        font_instrucoes1 = pygame.font.SysFont('Stencil', 25) # objeto referente a uma fonte
        font_instrucoes2 = pygame.font.SysFont('Stencil', 18) # objeto referente a uma fonte
        aviso1 = font_instrucoes1.render(instrucaoP1, 1, (0, 0, 0)) # texto com a fonte
        aviso2 = font_instrucoes1.render(instrucaoP2, 1, (0, 0, 0)) # texto com a fonte
        aviso3 = font_instrucoes2.render(instrucaoP3, 1, (64, 64, 64)) # texto com a fonte

        for y in range(self.altura):
            for x in range(self.largura):
                if self.matriz[y][x] == 0:
                    imagem = parede
                else:
                    imagem = caminho
                self.screen.blit(imagem, [x*25, y*25]) # desenha se vai ser caminho ou imagens
                if self.ponto_Final.x is not None:
                    self.screen.blit(casa, [self.ponto_Final.x*25, self.ponto_Final.y*25]) #desenha Casa

                #--------------------------- desenha avisos-----------------------------#
                self.screen.blit(aviso1, (self.largura*12.5-220, self.altura*10.5))
                self.screen.blit(aviso2, (self.largura*12.5-220, self.altura*10.5+25))
                self.screen.blit(aviso3, (25, self.altura*25 - 22))
                #-----------------------------------------------------------------------#
                
        pygame.display.update() # atauliza Tela


    # player = localização do jogador dentro do labirinto
    def player(self):
        player = pygame.draw.rect(self.screen, (255,0,0), (x, y, 25, 25)) # desenha retangulo - posição do jogador

    # escolhe_inicio_fim = Jogador vai definir o ponto inicial na coluna 0 e o ponto final na coluna n-1
    def escolhe_inicio_fim(self): 
        global x, y
        escolhas = 0
        loop = True
        
        
        while loop:
            if escolhas==0: # seleciona a coluna 0 - Ponto inicial
                instrucaoP1 = '1 - TECLE (SPACE) PARA ESCOLHER'
                instrucaoP2 = ' O PONTO INICIAL NA PRIMEIRA COLUNA'
                x=0
            elif escolhas==1: # seleciona a coluna n-1 - Ponto Final
                instrucaoP1 = '2 - TECLE (SPACE) PARA ESCOLHER'
                instrucaoP2 = 'O PONTO FINAL NA ULTIMA COLUNA'
                x=(self.largura-1)*25
            pygame.time.delay(100)
            
            for event in pygame.event.get(): # jogador deseja sair
                if event.type == pygame.QUIT:
                    loop = False

            #player controls
            keys = pygame.key.get_pressed()
            
            pos = x, y
            
            if keys[pygame.K_UP]: #Seta Baixo = movimenta para cima
                y -= speed
            if keys[pygame.K_DOWN]: # Seta Cima =  movimento para baixo
                y += speed                
            if keys[pygame.K_s]: # Tecla S = finalizar criação do labirinto
                loop = False
            if keys[pygame.K_SPACE] and escolhas==1: # seleciona o Ponto Inicial
                escolhas+=1
                self.ponto_Final = Ponto(x//25,y//25)
                self.matriz[y//25][x//25] = 1
            if keys[pygame.K_SPACE] and escolhas==0: # seleciona o Ponto Final
                escolhas+=1
                self.ponto_Inicial = Ponto(x//25,y//25)
                self.matriz[y//25][x//25] = 1
            
            
            if y<0 or y>(self.altura-1)*25: # verificação de não infringe limites do labirinto
                x,y = pos
            
            if escolhas==2: # já realizou as duas escolhas
                loop = False
            
            self.screen.fill((255,255,255))
            Gera_labirinto_manual.game_map(self, instrucaoP1, instrucaoP2, '')
            Gera_labirinto_manual.player(self)
            pygame.display.update()


    # manual = jogador realiza a criação do seu labirinto
    def manual(self):
        global x, y
        loop = True

        Gera_labirinto_manual.escolhe_inicio_fim(self) # escolhe Ponto Inicial e Final do labirinto

        instrucaoP1 = '3 - TECLE (C) PARA CRIAR CAMINHO'
        instrucaoP2 = 'E UTILIZE SETAS PARA MOVER'
        instrucaoP3 = '-(C) MARCAR CAMINHO  -  (SETAS) MOVIMENTAR  -  (S) FINALIZAR CRIAÇÃO'
        conta_Tempo_Sumir = 0 
        x = y  = 25
        
        while loop:
            pygame.time.delay(100)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False

            #player controls
            keys = pygame.key.get_pressed()
            
            pos = x, y

            if keys[pygame.K_LEFT]: # Seta Esquerda = movimenta para esquerda
                x -= speed
            if keys[pygame.K_RIGHT]: #Seta Direita = movimenta para direita
                x += speed
            if keys[pygame.K_UP]: # Seta Cima = movimenta para cima
                y -= speed
            if keys[pygame.K_DOWN]: # Seta Baixo = movimenta para baixo
                y += speed    
            if keys[pygame.K_c]: # Tecla C = Seleciona Caminho
                row = y // 25
                column = x // 25
                self.matriz[row][column] = 1
            if keys[pygame.K_s]: # Tecla S = finalizar criação do labirinto
                loop = False

            linha = y // 25
            coluna = x // 25
            if (coluna==0 or coluna >= self.largura-1) or (linha==0 or linha >=self.altura-1): # Verifica limites
                x, y = pos

            if(conta_Tempo_Sumir == 40): # Iempo limite para Instruções aparecer
                instrucaoP1 = ' '
                instrucaoP2 = ' '

            self.screen.fill((255,255,255))
            Gera_labirinto_manual.game_map(self, instrucaoP1, instrucaoP2, instrucaoP3)
            Gera_labirinto_manual.player(self)
            pygame.display.update()
            conta_Tempo_Sumir += 1
            
        pygame.quit()




