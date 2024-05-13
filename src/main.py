from estadoInicial import gerarEstadoInicial, solucionavel, printPuzzle, salvarResultado, salvarResultadoJson
from estado import State
from algoritmos import bfs, dfs, aStar
from time import time 

# Exemplo solucionavel [5, 6, 4, 3, 2, 7, 8, 1, 0]
n = int(input("Insira o tamanho N do puzzle\n")) # Altere o valor para tabuleiro maior
while (1):
    root, goal = gerarEstadoInicial(n)
    # root = [7, 3, 1, 6, 0, 2, 8, 5, 4]
    # goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    if (solucionavel(root)):
        break

print("Estado inicial:")
printPuzzle(root)

timeBfs = time()
resultadoBfs = bfs(State(root, None, None, 0, 0, goal), n)
timeBfs = time() - timeBfs
salvarResultado("bfs", root, resultadoBfs, timeBfs)
salvarResultadoJson("bfs", root, resultadoBfs, timeBfs)



timeDfs = time()
resultadoDfs = dfs(State(root, None, None, 0, 0, goal), n)
timeDfs = time() - timeDfs
print("Tempo de execução DFS: ", timeDfs)
print("Resultado DFS:", resultadoDfs)
