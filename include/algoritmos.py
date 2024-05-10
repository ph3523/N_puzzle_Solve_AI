from estado import State
from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue

def bfs(currentState: State, n: int):
    # Fila de prioridade
    if currentState.currentState == currentState.goalState:
        return currentState

    fronteira = Queue()
    fronteira.put(currentState)
    explorado = set()

    while not fronteira.empty():
        estado = fronteira.get()
        explorado.add(tuple(estado.currentState))

        noFilho = estado.expand(n)
        for filho in noFilho:
            if tuple(filho.currentState) not in explorado:
                if filho.checkGoal():
                    return filho.solution(), len(explorado)
                fronteira.put(filho)
    return

def dfs():

    return

def aStar():

    return


