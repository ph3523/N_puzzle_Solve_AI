from estado import State
from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue
# from memory_profiler import profile

# @profile
def bfs(currentState: State, n: int):
    if currentState.currentState == currentState.goalState:
        return currentState.solution(), 0

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
                    resultado = filho.solution()
                    return resultado[0], resultado[1], len(explorado)
                fronteira.put(filho)
    return

def dfs(currentState: State, n: int):
    if currentState.currentState == currentState.goalState:
        return currentState
    
    fronteira = LifoQueue()
    fronteira.put(currentState)
    explorado = set()

    while not fronteira.empty():
        estado = fronteira.get()
        max_profundidade = estado.depth
        explorado.add(tuple(estado.currentState))

        if max_profundidade == 30:
            continue

        noFilho = estado.expand(n)
        for filho in noFilho:
            if tuple(filho.currentState) not in explorado:
                if filho.checkGoal():
                    resultado = filho.solution()
                    return resultado[0], resultado[1], len(explorado)
                fronteira.put(filho)
    print("Não foi possível encontrar uma solução utlizando DFS")
    return 

def aStar(currentState: State, n: int, heuristic: str):
    frontier = PriorityQueue()
    explored = set()
    counter = 0
    root = currentState
    evaluation = root.misplacedTiles(n) if heuristic == 'misplaced' else root.manhattanDistance(n)
    frontier.put((evaluation, counter, root))
    
    while not frontier.empty():
        currentNode = frontier.get()
        currentNode = currentNode[2]
        explored.add(tuple(currentNode.currentState))

        if currentNode.checkGoal():
            return currentNode.solution() + (len(explored),)
        
        children = currentNode.expand(n)
        for child in children:
            if tuple(child.currentState) not in explored:
                counter += 1
                evaluation = child.misplacedTiles(n) if heuristic == 'misplaced' else child.manhattanDistance(n)
                frontier.put((evaluation, counter, child))
    return

def biAStar(startState: State, goalState: State, n: int, heuristic: str):
    forwardFrontier = PriorityQueue()
    backwardFrontier = PriorityQueue()

    forwardExplored = set()
    backwardExplored = set()

    forwardCounter = 0
    backwardCounter = 0

    forwardFrontier.put((startState.misplacedTiles(n) if heuristic == 'misplaced' else startState.manhattanDistance(n), forwardCounter, startState))
    backwardFrontier.put((goalState.misplacedTiles(n) if heuristic == 'misplaced' else goalState.manhattanDistance(n), backwardCounter, goalState))

    while not forwardFrontier.empty() and not backwardFrontier.empty():
        forwardNode = forwardFrontier.get()[2]
        forwardExplored.add(tuple(forwardNode.currentState))

        if tuple(forwardNode.currentState) in backwardExplored:
            return forwardNode.solution() + backwardNode.solution(False) + (len(forwardExplored) + len(backwardExplored),)

        for child in forwardNode.expand(n):
            if tuple(child.currentState) not in forwardExplored:
                forwardCounter += 1
                forwardFrontier.put((child.misplacedTiles(n) if heuristic == 'misplaced' else child.manhattanDistance(n), forwardCounter, child))

        backwardNode = backwardFrontier.get()[2]
        backwardExplored.add(tuple(backwardNode.currentState))

        if tuple(backwardNode.currentState) in forwardExplored:
            return forwardNode.solution() + backwardNode.solution(False) + (len(forwardExplored) + len(backwardExplored),)

        for child in backwardNode.expand(n):
            if tuple(child.currentState) not in backwardExplored:
                backwardCounter += 1
                backwardFrontier.put((child.misplacedTiles(n) if heuristic == 'misplaced' else child.manhattanDistance(n), backwardCounter, child))

    return