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

Vertice* BFSclona(Vertice* vertice){
    Vertice* verticesVisitados[MAX_NODES] = { NULL };
    
    Vertice* fila[MAX_NODES];
    int front = 0, back = 0;

    //Clona o nó inicial
    Vertice* cloneVertice = criaVertice(vertice->valor);
    verticesVisitados[vertice->valor] = cloneVertice;
    fila[back++] = vertice;

    // Enquanto a fila não está vazia
    while(front < back){
        Vertice* verticeAtual = fila[front++]; //Desenfilera primeiro vértice na fila
        Vertice* cloneVerticeAtual = verticesVisitados[verticeAtual->valor]; //Clona verticeAtual

        //Passa por todos os vizinhos de verticeAtual
        for(int i = 0; i < verticeAtual->qtdVizinhos; i++){
            Vertice* vizinho = verticeAtual->vizinhos[i];

            //Se o vizinho ainda não foi visitado, ele é clonado
            if(!verticesVisitados[vizinho->valor]){
                verticesVisitados[vizinho->valor] = criaVertice(vizinho->valor);
                fila[back++] = vizinho;
            }
            //Adiciona  a aresta
            cloneVerticeAtual->vizinhos[cloneVerticeAtual->qtdVizinhos++] = verticesVisitados[vizinho->valor];
        }
    }
    return cloneVertice;
}

Vertice* cloneGraph(Vertice* vertice){ return !vertice ? NULL : BFSclona(vertice); }