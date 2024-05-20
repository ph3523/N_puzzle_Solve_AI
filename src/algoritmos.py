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
    # Initialize two priority queues for the forward and backward searches
    forward_frontier = PriorityQueue()
    backward_frontier = PriorityQueue()

    # Initialize two sets for the explored states
    forward_explored = set()
    backward_explored = set()

    # Initialize counters for the forward and backward searches
    forward_counter = 0
    backward_counter = 0

    # Add the start and goal states to the frontiers
    forward_frontier.put((startState.misplacedTiles(n) if heuristic == 'misplaced' else startState.manhattanDistance(n), forward_counter, startState))
    backward_frontier.put((goalState.misplacedTiles(n) if heuristic == 'misplaced' else goalState.manhattanDistance(n), backward_counter, goalState))

    while not forward_frontier.empty() and not backward_frontier.empty():
        # Forward search
        forward_node = forward_frontier.get()[2]
        forward_explored.add(tuple(forward_node.currentState))

        if tuple(forward_node.currentState) in backward_explored:
            return forward_node.solution() + (len(forward_explored) + len(backward_explored),)

        for child in forward_node.expand(n):
            if tuple(child.currentState) not in forward_explored:
                forward_counter += 1
                forward_frontier.put((child.misplacedTiles(n) if heuristic == 'misplaced' else child.manhattanDistance(n), forward_counter, child))

        # Backward search
        backward_node = backward_frontier.get()[2]
        backward_explored.add(tuple(backward_node.currentState))

        if tuple(backward_node.currentState) in forward_explored:
            return backward_node.solution(False) + (len(forward_explored) + len(backward_explored),)

        for child in backward_node.expand(n):
            if tuple(child.currentState) not in backward_explored:
                backward_counter += 1
                backward_frontier.put((child.misplacedTiles(n) if heuristic == 'misplaced' else child.manhattanDistance(n), backward_counter, child))

    return