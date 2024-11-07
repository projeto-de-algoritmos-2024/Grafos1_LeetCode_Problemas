#include <stdio.h>
#include <stdlib.h>

#define MAX_NODES 101

typedef struct Vertice{
    int valor;
    int qtdVizinhos;
    struct Vertice** vizinhos;
} Vertice;

Vertice* criaVertice(int valor){
    Vertice* novoVertice = (Vertice*)malloc(sizeof(Vertice));
    novoVertice->valor = valor;
    novoVertice->qtdVizinhos = 0;
    novoVertice->vizinhos = (Vertice**)malloc(sizeof(Vertice*) * MAX_NODES);
    return novoVertice;
}

Vertice* cloneGraph(Vertice* vertice){
    if(!vertice) return NULL;
    
    Vertice* verticesVisitados[MAX_NODES] = { NULL };
    
    Vertice* fila[MAX_NODES];
    int front = 0, back = 0;
    
    Vertice* cloneVertice = criaVertice(vertice->valor);
    verticesVisitados[vertice->valor] = cloneVertice;
    fila[back++] = vertice;
    
    while(front < back){
        Vertice* verticeAtual = fila[front++];
        
        Vertice* cloneVerticeAtual = verticesVisitados[verticeAtual->valor];
        
        for(int i = 0; i < verticeAtual->qtdVizinhos; i++){
            Vertice* vizinho = verticeAtual->vizinhos[i];
            
            if(!verticesVisitados[vizinho->valor]){
                verticesVisitados[vizinho->valor] = criaVertice(vizinho->valor);
                fila[back++] = vizinho;
            }

            cloneVerticeAtual->vizinhos[cloneVerticeAtual->qtdVizinhos++] = verticesVisitados[vizinho->valor];
        }
    }
    
    return cloneVertice;
}