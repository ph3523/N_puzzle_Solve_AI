from utils import gerarEstadoInicial, solucionavel, printPuzzle, salvarResultado, salvarResultadoJson
from estado import State
from algoritmos import bfs, dfs, aStar
from time import time 
import psutil
import os

n = int(input("Insira o tamanho N do puzzle\n")) # Altere o valor para tabuleiro maior
while (1):
    root, goal = gerarEstadoInicial(n)
    if (solucionavel(root)):
        break

print("Estado inicial:")
printPuzzle(root)

process = psutil.Process(os.getpid())

memBfsInicial = process.memory_info().rss/1024.0
timeBfs = time()
resultadoBfs = bfs(State(root, None, None, 0, 0, goal), n)
memBfsFinal = process.memory_info().rss/1024.0
timeBfs = time() - timeBfs
salvarResultado("bfs", root, resultadoBfs, timeBfs, memBfsFinal - memBfsInicial)

memDfsInicial = process.memory_info().rss/1024.0
timeDfs = time()
resultadoDfs = dfs(State(root, None, None, 0, 0, goal), n)
memDfsFinal = process.memory_info().rss/1024.0
timeDfs = time() - timeDfs
salvarResultado("dfs", root, resultadoDfs, timeDfs, memDfsFinal - memDfsInicial)

memAstarInicial = process.memory_info().rss/1024.0
timeAStarMisplaced = time()
resultadoAStarMisplaced = aStar(State(root, None, None, 0, 0, goal), n, "misplaced")
memAstarFinal = process.memory_info().rss/1024.0
timeAStarMisplaced = time() - timeAStarMisplaced
salvarResultado("aStarMisplaced", root, resultadoAStarMisplaced, timeAStarMisplaced, memAstarFinal - memAstarInicial)

memAstarInicial = process.memory_info().rss/1024.0
timeAStarManhattan = time()
resultadoAStarManhattan = aStar(State(root, None, None, 0, 0, goal), n, "manhattan")
memAstarFinal = process.memory_info().rss/1024.0
timeAStarManhattan = time() - timeAStarManhattan
salvarResultado("aStarManhattan", root, resultadoAStarManhattan, timeAStarManhattan, memAstarFinal - memAstarInicial)