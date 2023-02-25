from Ponto import Ponto


# Classe responsavel por:
# - Fazer os possiveis proximos estados de um Estados Atual 
# - Calcular a Heuristica 

class Estado:
    def __init__(self,matriz, PontoAtual,PontoFinal, passos, caminho):
        self.PontoAtual = PontoAtual
        self.PontoFinal = PontoFinal
        self.matriz = matriz
        self.caminho = caminho #Caminho realizado desde o Ponto Inical até o Ponto Atual

        #calcula f, g, h
        self.g = passos
        self.h = self.calcula_Heurística()
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f
    
    # calcula_Heurística = |Ponto Atual - Ponto Final|
    def calcula_Heurística(self): 
        return int(Ponto.DistanciaEntreDoisPonto(self.PontoAtual, self.PontoFinal))
    
    # Retorna As possiveis Transições (Estados) a partir de um Estado
    def transicoes(self, estados_Passados):
        saida = []

        for i in range(1,5):
            proxEstado, direcao = Ponto.RetornaPonto(self.PontoAtual, i) # retorna proximo ponto e qual direção foi realizada para chegar nesse ponto

            if (self.matriz[proxEstado.y][proxEstado.x] != 0) and ((proxEstado.x, proxEstado.y) not in estados_Passados):
                caminho = self.caminho + [direcao] # adicionando movimento no caminho 
                saida.append(Estado(self.matriz, proxEstado, self.PontoFinal, self.g + 1, caminho))
        return saida
    
    
    def __repr__(self):
        return "({})".format(self.PontoAtual)



