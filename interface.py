
from Estado import Estado
from Gabarito import Gabarito
import pygame
from pygame import mixer


speed = 25
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
        self.screen = pygame.display.set_mode((self.largura*25,self.altura*25))
        pygame.display.set_caption("Labirinto")

    def game_map(self, instrucao):
        
        #caminho
        caminho = pygame.image.load('chaoClaro.png').convert_alpha()

        #parede
        parede = pygame.image.load('parede.png').convert_alpha()
        #tracante
        chaoEscuro = pygame.image.load('chaoEscuro.png').convert_alpha()
        #casa
        casa = pygame.image.load('casa.png').convert_alpha()

        pygame.font.init() #instruções
        font_instrucoes2 = pygame.font.SysFont('Stencil', 18)
        aviso = font_instrucoes2.render(instrucao, 1, (64, 64, 64))

        for y, row in enumerate(self.matriz):
            for x, cell in enumerate(row):
                if cell == 0:
                    image = parede
                elif cell == 1:
                    image = caminho
                else:
                    image = chaoEscuro
                self.screen.blit(image, [x*25, y*25])
                self.screen.blit(casa, [self.ponto_Final.x*25, self.ponto_Final.y*25]) 
                self.screen.blit(aviso, (25, self.altura*25 - 22)) 
        pygame.display.update() 


    def player(self):
        player = pygame.image.load('raffChao.png').convert_alpha()
        self.screen.blit(player, [self.x, self.y])  

    def automatico(self,resposta): ####mudar

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
            
            if self.matriz[row][column] == 1:
                self.matriz[row][column] = 2
            pos = self.x, self.y

            if resposta[i]=='left':
                self.x -= speed
            if resposta[i]=='right':
                self.x += speed
            if resposta[i]=='up':
                self.y -= speed
            if resposta[i]=='down':
                self.y += speed

            pygame.time.delay(100)
            i+=1
            row = self.y // 25
            column = self.x // 25
            if self.matriz[row][column] == 0:
                self.x, self.y = pos

            self.screen.fill((255,255,255))
            interface.game_map(self, instrucao)
            interface.player(self)
            pygame.display.update()
            
            if row == self.ponto_Final.y and column == self.ponto_Final.x:
                loop = False

        pygame.quit()

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

            #player controls
            keys = pygame.key.get_pressed()
            
            pos = self.x, self.y

            row = self.y // 25
            column = self.x // 25
            if self.matriz[row][column] == 1:
                self.matriz[row][column] = 2

            if keys[pygame.K_LEFT]:
                self.x -= speed
                movimentos += 1
            if keys[pygame.K_RIGHT]:
                self.x += speed
                movimentos += 1
            if keys[pygame.K_UP]:
                self.y -= speed
                movimentos += 1
            if keys[pygame.K_DOWN]:
                self.y += speed
                movimentos += 1
            
            row = self.y // 25
            column = self.x // 25
            if self.matriz[row][column] == 0:
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

    def to_execute_Manual(self):
        return self.manual()
        
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

