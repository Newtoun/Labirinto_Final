from Ponto import Ponto
from random import randint

# Classe responsável por:
# - Gera um labirinto e define o ponto inicial e final do Jogo

class Gera_labirinto_automatico:

    def __init__(self,largura,altura):
        self.largura = largura # x
        self.altura = altura # y
        self.matriz = self.inicializa_Matriz_Zero()
        self.ponto_Inicial = None
        self.ponto_Final = None
        self.Gera_Labirinto()
        self.Define_Inicio_Fim()

    # acessa_Elemento = Retorna O elemento referente as posições dentro de da matriz
    def acessa_Elemento(self,x,y):
        num = self.matriz[y][x]
        return num
 
    # inicializa_MAtriz_Zero = Cria uma matriz onde todos os seus elementos são 0
    def inicializa_Matriz_Zero(self):
        mat = []     
        for i in range(self.altura):
            lista = [0]*self.largura
            mat.append(lista)
        return mat
    
    # imprime_Matriz = imprime Matriz
    def imprime_Matriz(self):
        for i in range(self.altura):
            for j in range(self.largura):
                print(self.matriz[i][j],end=" ")
            print()
    
    # retorna_Corredores = Faz os 4 Pontos referente a quatro sentidos e retorna eles dentro de um vetor
    def retorna_Corredores(lista_proibida,x,y):
        lista = []
        if (x-1,y,x-2,y) not in lista_proibida : # Esquerda
            lista.append((x-1,y,x-2,y))  
            lista_proibida.add((x-1,y,x-2,y))

        if (x,y-1,x,y-2) not in lista_proibida : # cima    
            lista.append((x,y-1,x,y-2))
            lista_proibida.add((x,y-1,x,y-2))

        if (x+1,y,x+2,y) not in lista_proibida : # Direita
            lista.append((x+1,y,x+2,y))
            lista_proibida.add((x+1,y,x+2,y))

        if (x,y+1,x,y+2) not in lista_proibida : # Baixo
            lista.append((x,y+1,x,y+2))
            lista_proibida.add((x,y+1,x,y+2))

        return lista
        
    # Gera_Labirinto = Escolhe um ponto aleatorio e a partir dele, vai construindo os caminhos do labirinto 
    def Gera_Labirinto(self):
        lista_proibida = set()
        lista = []

        altura = self.altura
        largura = self.largura

        x=y=0

        while y%2==0 or x%2==0 and(y<altura-2 and x< largura-2): # define o Ponto de inicio que deve ser primo
            y = randint(3,(altura-3))
            x = randint(3,(largura-3))
        
            
        self.matriz[y][x]=1

        lista = Gera_labirinto_automatico.retorna_Corredores(lista_proibida,x,y) # retorna vetor com os possiveis caminhos a serem criados

        while len(lista)> 0 :
            escolha = randint(0,len(lista)-1)
            ponto = lista[escolha] # escolhe um dos caminhos aleatorios para ser seguido
            lista.pop(escolha)

            if (ponto[2] >= 0) and (ponto[3] >= 0) and (ponto[2]< largura -1) and (ponto[3]<altura-1): # verifica ponto referente aos limites da matriz
                if (self.matriz[ponto[3]][ponto[2]]==0): # verifica se o elemento é 0 (Parede)
                    self.matriz[ponto[1]][ponto[0]] = 1  # adiciona o valor 1 (Caminho) aquela posição na matriz
                    self.matriz[ponto[3]][ponto[2]] = 1  
                    lista += Gera_labirinto_automatico.retorna_Corredores(lista_proibida,ponto[2],ponto[3])
   
    # Define_Inicio_Fim = Defini de forma aleatoria o ponto inicial na primeira coluna e o ponto final da ultima coluna
    def Define_Inicio_Fim(self):
        inicio = randint(1,(self.altura-1)) 
        
        while self.matriz[inicio][1] != 1:
             inicio = randint(1,(self.altura-1))
        Ponto_Inicio= Ponto(0, inicio)
        
        fim = randint(1,(self.altura-1)) 
        
        while self.matriz[fim][self.largura-2] != 1:
            fim = randint(1,(self.altura-1))
        Ponto_Fim= Ponto(self.largura-1, fim)

        self.matriz[inicio][0] = 1
        self.matriz[fim][self.largura-1] = 1

        self.ponto_Inicial = Ponto_Inicio
        self.ponto_Final = Ponto_Fim



 