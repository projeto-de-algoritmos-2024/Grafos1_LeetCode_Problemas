#include <iostream>
#include <vector>
#include <climits>
#include <queue>

using namespace std;

class Solution{
public:
    vector<vector<int>> copiaGrafo(int nVertices, const vector<vector<int>>& matrizAdj){
        vector<vector<int>> novoGrafo(nVertices);
        for(const auto& aresta : matrizAdj){
            int u = aresta[0], v = aresta[1];
            novoGrafo[u].push_back(v);
            novoGrafo[v].push_back(u);
        }
        return novoGrafo;
    }

    int ciclo(int pai, int vizinho){ return pai != vizinho; }

    int tamanhoCiclo(const vector<int>& distancia, int vAtual, int vizinho){ return distancia[vAtual] + distancia[vizinho] + 1; }

    int BFS(int numVertices, int vInicio, const vector<vector<int>>& grafo){
        vector<int> distancia(numVertices, -1);
        vector<int> pai(numVertices, -1);
        distancia[vInicio] = 0;

        queue<pair<int, int>> fila;
        fila.push({vInicio, -1});

        int tamanhoMenorCiclo = INT_MAX;

        while(!fila.empty()){
            int vAtual = fila.front().first;
            int vPai = fila.front().second;
            fila.pop();

            for(int vizinho : grafo[vAtual]){
                if(distancia[vizinho] == -1){
                    distancia[vizinho] = distancia[vAtual] + 1;
                    pai[vizinho] = vAtual;
                    fila.push({vizinho, vAtual});
                }else if(ciclo(vPai, vizinho))
                    tamanhoMenorCiclo = min(tamanhoMenorCiclo, tamanhoCiclo(distancia, vAtual, vizinho));
            }
        }
        return tamanhoMenorCiclo;
    }

    int findShortestCycle(int n, const vector<vector<int>>& edges){
        vector<vector<int>> grafo = copiaGrafo(n, edges);
        int tamanhoMenorCiclo = INT_MAX;

        for(int v = 0; v < n; v++){
            int tamanhoCiclo = BFS(n, v, grafo);
            if(tamanhoCiclo != INT_MAX) 
                tamanhoMenorCiclo = min(tamanhoMenorCiclo, tamanhoCiclo);
        }
        return tamanhoMenorCiclo == INT_MAX ? -1 : tamanhoMenorCiclo;
    }
};