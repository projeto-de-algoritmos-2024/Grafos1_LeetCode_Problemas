#include <bits/stdc++.h>

using namespace std;

class Solution 
{
  public:
    bool isBipartite(vector<vector<int>>& graph)
    {
      //VERIFICAR TAMANHO DO GRAFO
      int tam = graph.size();

      //Criando vetor coloracao para colorir nos do grafo a fim de saber se eh bipartido ou nao
      vector<int> coloracao(tam,0);

      for(int i=0;i<tam;i++)
        if(coloracao[i]==0) if(!bfs(graph, coloracao, i)) return false;
      return true;
    }
    bool bfs(vector<vector<int>>& graph, vector<int>& coloracao, int s)
    {
      coloracao[s]=-1;
      queue<int> fila;
      fila.push(s);
     
      //Enquanto a fila NAO estiver vazia
      while(!fila.empty())
      {
        //Pega primeiro elemento da fila
        int no = fila.front();

        for(int i=0;i<graph[no].size();i++)
        {
          int vizinho = graph[no][i];
          if(coloracao[vizinho] == coloracao[no]) return false; //Mesma cor que o no vizinho
          else if(coloracao[vizinho]==0)
          {
            coloracao[vizinho] = coloracao[vizinho] - coloracao[no];
            
            fila.push(vizinho);
          }
        }
        fila.pop();
      }
      return true;
    }
};