from include.estadoInicial import gerar_estado_inicial, solucionavel, print_puzzle

# Exemplo solucionavel [5, 6, 4, 3, 2, 7, 8, 1, 0]

n = int(input("Insira o tamanho N do puzzle\n"))
while(1):
  root = gerar_estado_inicial(n) #Altere o valor para tabuleiro maior
  if(solucionavel(root)):
     break
  
print("Estado inicial:")
print_puzzle(root)

