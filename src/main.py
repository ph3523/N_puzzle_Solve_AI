from estadoInicial import gerarEstadoInicial, solucionavel, printPuzzle
from estado import State
from algoritmos import bfs, dfs, aStar
from time import time

# Exemplo solucionavel [5, 6, 4, 3, 2, 7, 8, 1, 0]
n = int(input("Insira o tamanho N do puzzle\n")) # Altere o valor para tabuleiro maior
while (1):
    root, goal = gerarEstadoInicial(n)
    if (solucionavel(root)):
        break

print("Estado inicial:")
printPuzzle(root)

timeBfs = time()
resultadoBfs = bfs(State(root, None, None, 0, 0, goal), n)
timeBfs = time() - timeBfs
print("Tempo de execução BFS: ", timeBfs)
print("Resultado BFS:", resultadoBfs)

