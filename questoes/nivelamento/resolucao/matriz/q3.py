#Lendo dados da Matriz A
A = []
for i in range(6):          
    a = [] 
    x, y, z = input("Informe os elementos da linha %d da matriz A 3x3 seperado por espaço: " % (i+1)).split()  
    a.append(float(x))
    a.append(float(y))
    a.append(float(z)) 
    A.append(a)
    
#Calculando a Matriz C
primeiro_maior_valor = False
valor_maior = 0
i_maior = 0
j_maior = 0

primeiro_menor_valor = False
valor_menor = 0
i_menor = 0
j_menor = 0

for i in range(6):
    for j in range(3):
        if(not primeiro_maior_valor or valor_maior < A[i][j]):
            valor_maior = A[i][j]
            i_maior = i
            j_maior = j
            primeiro_maior_valor = True
            
        if(not primeiro_menor_valor or valor_menor > A[i][j]):
            valor_menor = A[i][j]
            i_menor = i
            j_menor = j
            primeiro_menor_valor = True

print("o maior elemento é %.2f na posição (i,j) = (%d,%d)" % (valor_maior,i_maior+1,j_maior+1))
print("o menor elemento é %.2f na posição (i,j) = (%d,%d)" % (valor_menor,i_menor+1,j_menor+1))
