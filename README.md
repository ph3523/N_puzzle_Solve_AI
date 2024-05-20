# N Puzzle Solver AI
Este projeto é uma implementação de algoritmos de busca em Python. Ele contém vários algoritmos, incluindo Busca em Largura (BFS), Busca em Profundidade (DFS), A* com heurística de Manhattan e A* com heurística de peças fora do lugar.

# Como rodar o projeto
Para rodar o projeto na sua máquina, siga os passos abaixo:
```
1. Clone o repositório
2. Cheque se você tem o Python 3 instalado na sua máquina
3. Navegue até a pasta do projeto
4. Execute o comando python3 main.py ou python main.py
5. Aguarde o programa salvar os resultados
6. Os resultados serao salvos no caminho resultados/<algoritmo>.txt.
```

# Algoritmos utilizados
Os algoritmos implementados neste projeto são:

## Busca em Largura (BFS)
A busca em largura é um algoritmo de busca que explora todos os vértices de um grafo em largura, ou seja, explora todos os vértices vizinhos antes de explorar os vértices mais distantes. Este algoritmo é implementado na função bfs() em algoritmos.py.

## Busca em Profundidade (DFS)
A busca em profundidade é um algoritmo de busca que explora todos os vértices de um grafo em profundidade, ou seja, explora um vértice até que não haja mais vértices a serem explorados. Este algoritmo é implementado na função dfs() em algoritmos.py.

## A* com heurística de Manhattan
O algoritmo A* é um algoritmo de busca que utiliza uma heurística para encontrar o caminho mais curto entre dois pontos. A heurística de Manhattan calcula a distância de Manhattan entre a posição atual de uma peça e a posição final desejada. Este algoritmo é implementado na classe State em estado.py e utilizado na funcao aStar().

## A* com heurística de peças fora do lugar
O algoritmo A* é um algoritmo de busca que utiliza uma heurística para encontrar o caminho mais curto entre dois pontos. A heurística de peças fora do lugar simplesmente conta o número de peças que não estão na posição correta. Este algoritmo é implementado na classe State em estado.py e utilizado na funcao aStar().

## A* bidirecional
O algoritmo A* bidirecional é uma variação do algoritmo A* que utiliza duas buscas simultâneas, uma partindo do estado inicial e outra partindo do estado final. Este algoritmo é implementado na função aStarBi() em algoritmos.py, porem ainda em testes.

Para mais detalhes sobre os algoritmos implementados, consulte os arquivos algoritmos.py e main.py.

# Contribuições
Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

# Participantes
Este projeto foi desenvolvido por:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/FelpLiet">
        <img src="https://github.com/FelpLiet.png?size=100" width="100px;" alt="Felipe Nogueira"/>
        <br />
        <sub><b>Felipe Nogueira</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/ph3523">
        <img src="https://github.com/ph3523.png?size=100" width="100px;" alt="Pedro Henrique"/>
        <br />
        <sub><b>Pedro Henrique</b></sub>
      </a>
    </td>
  </tr>
</table>

# Licença
Este projeto esta licenciado sob a licença GPL-3.0. Para mais informações, consulte o arquivo LICENSE.