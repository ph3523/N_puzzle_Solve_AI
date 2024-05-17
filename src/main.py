from utils import gerarEstadoInicial, solucionavel, printPuzzle, salvarResultado, salvarResultadoJson
from estado import State
from algoritmos import bfs, dfs, aStar
from time import time 

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
salvarResultado("bfs", root, resultadoBfs, timeBfs)

timeDfs = time()
resultadoDfs = dfs(State(root, None, None, 0, 0, goal), n)
timeDfs = time() - timeDfs
salvarResultado("dfs", root, resultadoDfs, timeDfs)

timeAStarMisplaced = time()
resultadoAStarMisplaced = aStar(State(root, None, None, 0, 0, goal), n, "misplaced")
timeAStarMisplaced = time() - timeAStarMisplaced
salvarResultado("aStarMisplaced", root, resultadoAStarMisplaced, timeAStarMisplaced)

timeAStarManhattan = time()
resultadoAStarManhattan = aStar(State(root, None, None, 0, 0, goal), n, "manhattan")
timeAStarManhattan = time() - timeAStarManhattan
salvarResultado("aStarManhattan", root, resultadoAStarManhattan, timeAStarManhattan)