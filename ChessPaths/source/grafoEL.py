from collections import deque

#DEFINE GRAFO
grafo = [[] for _ in range(64)]

#ADICONA ARESTA
def adicionarAresta(grafo, u, v):
    grafo[u].append(v)
    grafo[v].append(u)

#MAPEAR COORDENADA TABULEIRO -> V GRAFO
def matrizParaVertice(x, y):
    if 0 <= x < 8 and 0 <= y < 8:
        return 8 * x + y
    else:
        return -10
    
def coordenadaParaCasa(x, y):
    coluna = chr(ord('a') + x)
    linha = 8 - y
    return f"{coluna}{linha}"
    
#recebe a posição de um cavalo e monta o grafo de como ele chega em qualquer outra casa adicionando as arestas    
def montarUmaJogada(pos_x_cavalo, pos_y_cavalo, grafo):
    #Define os movimentos possíveis do cavalo - TEMPORÁRIO
    movimentos_cavalo = [(1, 2), (1, -2), (2, 1), (2, -1), 
                         (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

    pos_inicial = matrizParaVertice(pos_x_cavalo, pos_y_cavalo)

    #Constrói o grafo com base nos movimentos do cavalo
    for dx, dy in movimentos_cavalo:
        novo_x = pos_x_cavalo + dx
        novo_y = pos_y_cavalo + dy
        
        if 0 <= novo_x < 8 and 0 <= novo_y < 8:
            target = matrizParaVertice(novo_x, novo_y)
            
            adicionarAresta(grafo, pos_inicial, target)

def caminhoMinimo(cavalo_inicial, cavalo_destino, grafo):
    #Lista para rastrear as casas visitadas e seus predecessores
    pai = [-1] * 64  # -1 significa que não tem pai
    visitadas = set()
    
    #Mapeia a posição inicial e a posição final para os vértices correspondentes
    pos_inicial = matrizParaVertice(cavalo_inicial[0], cavalo_inicial[1])
    pos_destino = matrizParaVertice(cavalo_destino[0], cavalo_destino[1])
    
    #Fila da BFS
    fila = deque([pos_inicial])
    visitadas.add(pos_inicial)
    
    while fila:
        pos_atual = fila.popleft()
        
        #Se chegou no destino, podemos reconstruir o caminho
        if pos_atual == pos_destino:
            caminho = []
            while pos_atual != pos_inicial:
                caminho.append(pos_atual)
                pos_atual = pai[pos_atual]
            caminho.append(pos_inicial)
            caminho.reverse()  # Inverte o caminho para começar de A até B
            return caminho
        
        #Explora vizinhos NÃO visitados
        for vizinho in grafo[pos_atual]:
            if vizinho not in visitadas:
                visitadas.add(vizinho)
                fila.append(vizinho)
                pai[vizinho] = pos_atual  #Registra o pai
    
    return None  #Caso não haja caminho válido

#TESTE TERMINAL:
# cavalo_inicial = (7, 6)
# cavalo_destino = (3, 7)  

#Monta o grafo com as possíveis jogadas do cavalo
# for x in range(8):
#     for y in range(8):
#         montarUmaJogada(x, y, grafo)

# caminho = caminhoMinimo(cavalo_inicial, cavalo_destino, grafo)

# caminho_convertido = [(pos // 8, pos % 8) for pos in caminho]
# print(caminho_convertido)