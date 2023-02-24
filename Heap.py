class Heap:
    
    # min_heapify = Transforma uma quase heap Minima em uma heap Minima
    def min_heapify(vetor, raiz, tam):
        mini = raiz
        esq = (raiz*2)+1 # filho esquerdo
        if esq < tam and (vetor[mini] > vetor[esq]):
            mini = esq
            
        dire = (raiz*2)+2 # filho direito
        if dire < tam and (vetor[mini] > vetor[dire]):
            mini = dire
            
        if(raiz != mini):
            vetor[raiz], vetor[mini] = vetor[mini], vetor[raiz] # troca
            vetor = Heap.min_heapify(vetor, mini, tam)
        
        return vetor
    
    # aumenta_Chave = Insere um elemento na Heap
    def aumentar_chave(heap, pos, novo):
        tam = len(heap)

        if pos == tam:
            heap.append(novo)
        else:
            heap[pos] = novo

        pai = (pos-1)//2

        while (pos > 0 ) and heap[pos].__lt__(heap[pai]):
            heap[pai],heap[pos] = heap[pos],heap[pai]
            pos = pai
            pai = (pos-1)//2
            
        return heap
    
    # atualizar_Heap = Atualiza a Fila de Prioridade juntamente com o vetor de Estados de transições
    def atualizar_Heap(heap, vetor): 
        for i in vetor:
            tam = len(heap)
            heap = Heap.aumentar_chave(heap, tam , i)
        
        return heap
        
    # remover_Primeiro_Elemento = Remove primeiro Elemento da Heap
    def remover_Primeiro_Elemento(heap):
        tam = len(heap)
        heap[0] = heap[tam-1]
        heap.pop()
        heap = Heap.min_heapify(heap, 0, tam-1)
        
        return heap
