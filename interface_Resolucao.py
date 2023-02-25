
from Estado import Estado
from Gabarito import Gabarito
import pygame
from pygame import mixer


speed = 25 #velocidade do jogador

# Classe responsável por:
# - Recebe um objeto da classe Gera_labirinto_Manual ou Gera_labirinto_Automatica 
# e plota o jogo na tela do jogador as atualizações constantes

class interface:
    def __init__(self,matriz):
        self.altura = matriz.altura
        self.largura = matriz.largura
        self.matriz = matriz.matriz
        self.ponto_Inicial = matriz.ponto_Inicial
        self.ponto_Final = matriz.ponto_Final
        self.x = matriz.ponto_Inicial.x*25
        self.y = matriz.ponto_Inicial.y*25
        pygame.init()
        self.screen = pygame.display.set_mode((self.largura*25,self.altura*25)) #inicializa Tela
        pygame.display.set_caption("Labirinto") # define nome da tela

    # game_map = Plota o labirinto
    def game_map(self, instrucao):
        
        # ---------carrega as imagens usada na tela---------------------#
        caminho = pygame.image.load('chaoClaro.png').convert_alpha()
        parede = pygame.image.load('parede.png').convert_alpha()
        chaoEscuro = pygame.image.load('chaoEscuro.png').convert_alpha()
        casa = pygame.image.load('casa.png').convert_alpha()
        # --------------------------------------------------------------#

        pygame.font.init() #inicializar o módulo de fonte para plotar Instruções para o jogador
        font_instrucoes2 = pygame.font.SysFont('Stencil', 18)  # objeto referente a uma fonte
        aviso = font_instrucoes2.render(instrucao, 1, (64, 64, 64)) # texto com a fonte

        
        for y, row in enumerate(self.matriz):#faz a plotagem na tela de acordo como a matriz é atualizada
            for x, cell in enumerate(row):
                if cell == 0:
                    image = parede
                elif cell == 1:
                    image = caminho
                else:
                    image = chaoEscuro
                # --------------------------Plota as imagens---------------------------#
                self.screen.blit(image, [x*25, y*25])
                self.screen.blit(casa, [self.ponto_Final.x*25, self.ponto_Final.y*25]) 
                self.screen.blit(aviso, (25, self.altura*25 - 22)) 
                # --------------------------Plota as imagens---------------------------#
        pygame.display.update() 

    # player = funcao que define a posicao do player na tela
    def player(self):
        player = pygame.image.load('raffChao.png').convert_alpha()
        self.screen.blit(player, [self.x, self.y])  

    # automatico = funcao responsavel pela resolucao do labirinto de forma automatica 
    def automatico(self,resposta): 

        loop = True
        i = 0
        instrucao = '-RESOLUÇÂO REALIZADA DE FORMA AUTOMÁTICA'
        while loop:
            pygame.time.delay(100)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
            
            row = self.y // 25
            column = self.x // 25
            
            if self.matriz[row][column] == 1: # atualiza o caminho que o player passou
                self.matriz[row][column] = 2
            pos = self.x, self.y
            
            #----movimentação do player de acordo o o vetor de resposta-------#
            if resposta[i]=='left':
                self.x -= speed
            if resposta[i]=='right':
                self.x += speed
            if resposta[i]=='up':
                self.y -= speed
            if resposta[i]=='down':
                self.y += speed
            #-----------------------------------------------------------------#
            
            pygame.time.delay(100)
            i+=1
            row = self.y // 25
            column = self.x // 25

            if self.matriz[row][column] == 0: # verificacao de colisao
                self.x, self.y = pos

            self.screen.fill((255,255,255))
            interface.game_map(self, instrucao)
            interface.player(self)
            pygame.display.update()
            
            if row == self.ponto_Final.y and column == self.ponto_Final.x: #verificacao se chegou no ponto final
                loop = False

        pygame.quit()

    # manual = funcao responsavel pela resolucao do labirinto de forma manual 
    def manual(self):
        loop = True
        Retorno = False
        instrucao = '- TECLE NAS (SETAS) PARA CHEGAR NO ICOMP - (X) PARA SAIR OU RESOLVER AUTOMATICAMENTE'
        movimentos = 0

        while loop:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                    movimentos = 0

            
            keys = pygame.key.get_pressed() #leitura do teclado do usuario
            
            pos = self.x, self.y

            row = self.y // 25
            column = self.x // 25

            if self.matriz[row][column] == 1: # atualiza o caminho que o player passou
                self.matriz[row][column] = 2

            if keys[pygame.K_LEFT]: # Seta Esquerda = movimenta para esquerda
                self.x -= speed
                movimentos += 1
            if keys[pygame.K_RIGHT]: #Seta Direita = movimenta para direita
                self.x += speed
                movimentos += 1
            if keys[pygame.K_UP]: # Seta Cima = movimenta para cima
                self.y -= speed
                movimentos += 1
            if keys[pygame.K_DOWN]: # Seta Baixo = movimenta para baixo
                self.y += speed
                movimentos += 1
            
            row = self.y // 25
            column = self.x // 25
            if self.matriz[row][column] == 0: # verificacao de colisao
                self.x, self.y = pos
                movimentos -=1

            self.screen.fill((255,255,255))
            interface.game_map(self, instrucao)
            interface.player(self, )
            pygame.display.update()

            if row == self.ponto_Final.y and column == self.ponto_Final.x:
                loop = False
                Retorno = True

        pygame.quit()
        return Retorno, movimentos
    
    #to_execute_Manual = funcao para executar manualmente
    def to_execute_Manual(self):
        return self.manual()
    
    # to_execute_Automatico = funcao para executar automaticamente    
    def to_execute_Automatico(self):
        estadoInicial = Estado(self.matriz,self.ponto_Inicial,self.ponto_Final,0, [])
        resposta = Gabarito.caminho_ate_Fim(estadoInicial)
        print(resposta)
        if (resposta == []):
           pygame.quit()
           return True, len(resposta)
        else:
            self.automatico(resposta)
            return False, len(resposta)

