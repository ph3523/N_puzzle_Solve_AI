import random

def gerar_estado_inicial(n):
  # Obter estado final
  estado_final = list(range(1, n * n ))
  estado_final.append(0)  # Peça vazia na última posição


  # Embaralhar as peças
  for _ in range(n * n * 10):
    i, j = random.randrange(n * n), random.randrange(n * n)
    estado_final[i], estado_final[j] = estado_final[j], estado_final[i]

  return estado_final

def qtd_inversoes(puzzle):
    inv = 0
    for i in range(len(puzzle)-1):
        for j in range(i+1 , len(puzzle)):
            if (( puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                inv += 1
    return inv

def solucionavel(puzzle):
    inv_counter = qtd_inversoes(puzzle)
    if (inv_counter %2 ==0):
        return True
    return False

def print_puzzle(puzzle):
    n = int(len(puzzle) ** 0.5)
    for i in range(0, len(puzzle), n):
        print(puzzle[i:i+n])