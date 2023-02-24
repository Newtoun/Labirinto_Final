from Estado import Estado
from Heap import Heap


# Classe responsavel por:
# - retornar vetor com o caminho desde o Ponto incial até o Ponto Final

class Gabarito:
    #caminho_ate_Fim = Responsavel por Realizar o Processo de encontrar o Caminho com menos movimentos até o Ponto Final
    def caminho_ate_Fim(estado):
        
        fila_De_Prioridade = [] # heapMinima
        estados_Passados = set() # Pontos que já foram Escolhidos Anteriormente 
        estado_Atual = estado # Começa com o Estado Inicial (Ponto Inicial)
        fila_De_Prioridade.append(estado_Atual)
        vetor = [] # vai receber os Possiveis Proximos estados a serem escolhidos
        #self.numero_Tentativas = len(estados_Passados) 

        while len(fila_De_Prioridade) > 0:
            if (estado_Atual.PontoAtual.x == estado_Atual.PontoFinal.x) and  (estado_Atual.PontoAtual.y == estado_Atual.PontoFinal.y):
                return estado_Atual.caminho # Retorna Caminho até o Ponto final, caso tenha chegado nele

            estados_Passados.add((estado_Atual.PontoAtual.x, estado_Atual.PontoAtual.y))

            vetor = Estado.transicoes(estado_Atual, estados_Passados) # retorna vetor com candidatos a serem o proximo escolhido
            
            fila_De_Prioridade = Heap.remover_Primeiro_Elemento(fila_De_Prioridade) # renome da fila de prioridade estado Atual
            
            fila_De_Prioridade = Heap.atualizar_Heap(fila_De_Prioridade, vetor) # reorganiza Heap Minima

            

            if len(fila_De_Prioridade) != 0: 
                estado_Atual = fila_De_Prioridade[0] # Seleciona o Proximo Estado
        
        return [] # retorna um vetor Vazio caso não tenha solução
    
