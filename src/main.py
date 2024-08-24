# src/main.py
from utils import gerarEstadoInicial, solucionavel, printPuzzle, salvarResultado, executarERegistrar
from estado import State
from algoritmos import bfs, dfs, aStar, biAStar
from time import time 

n = int(input("Insira o tamanho N do puzzle\n")) # Altere o valor para tabuleiro maior
while (1):
    root, goal = gerarEstadoInicial(n)
    if (solucionavel(root)):
        break

print("Estado inicial:")
printPuzzle(root)

resultados = []
resultados.append(executarERegistrar("bfs", bfs, root, goal, n))
resultados.append(executarERegistrar("dfs", dfs, root, goal, n))
resultados.append(executarERegistrar("aStarMisplaced", aStar, root, goal, n, "misplaced"))
resultados.append(executarERegistrar("aStarManhattan", aStar, root, goal, n, "manhattan"))
resultados.append(executarERegistrar("biAStar", biAStar, root, goal, n, "misplaced"))

# Comparar resultados
for resultado in resultados:
    print(f"Algoritmo: {resultado['algoritmo']}")
    print(f"Tempo: {resultado['tempo']:.4f} segundos")
    print(f"Memória: {resultado['memoria']:.2f} KB")
    # print(f"Resultado: {resultado['resultado']}\n")