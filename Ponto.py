# Classe resposavel por:
# - Imprimir ponto
# - Atualizar valor de um Ponto
# - Retorna Ponto com movimentação ou para direita ou para esquerda ou para cima ou para baixo
# - Distancia entre Dois Pontos

class Ponto:
    # __init__ =  É inserido o ponto x e y que representa o ponto
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # __repr__ = Imprime o Ponto
    def __repr__(self):
        return "({},{})".format(self.x, self.y)
    
     # set_x = Modifica os valor de x
    def set_x(self,num):
        self.x+=num
        
    # set_y = Modifica o valor de y
    def set_y(self,num): 
        self.y+=num
        
    # DistanciaEntreDoisPonto = Retorna a distancia entre dois pontos
    def DistanciaEntreDoisPonto(self, other): 
        return abs(self.x - other.x) + abs(self.y - other.y)

    # RetornaPonto = Retorna os pontos de possiveis movimentações a partir de um ponto
    def RetornaPonto(self, movimento):
        proxPonto = Ponto(self.x,self.y)
        if  movimento == 1:
            proxPonto.set_y(-1) # Para cima
            direcao = "up"
        elif movimento == 2 :
            proxPonto.set_y(+1) # Para baixo
            direcao = "down"
        elif movimento == 3:
            proxPonto.set_x(-1) # Para esquerda
            direcao = "left"
        elif movimento == 4:
            proxPonto.set_x(+1) # para direita
            direcao = "right"
        
        return proxPonto, direcao

    

