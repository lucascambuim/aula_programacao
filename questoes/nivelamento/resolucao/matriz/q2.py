#Lendo dados da Matriz A
A = []
for i in range(3):          
    a = [] 
    x, y, z = input("Informe os elementos da linha %d da matriz A 3x3 seperado por espaço: " % (i+1)).split()  
    a.append(int(x))
    a.append(int(y))
    a.append(int(z)) 
    A.append(a)
    
print("Informe o parâmetro de multiplicaçao k:", end = " ")
k = int(input())

#Calculando a Matriz C
C = []
for i in range(3):
    x = []
    for j in range(3):
        if(i == j):
            x.append(A[i][j]*k)
        else:
            x.append(A[i][j])       
    C.append(x)


print("Matriz antes da multiplicação",)
for i in range(3): 
    for j in range(3): 
        print(A[i][j], end = " ") 
    print()
    
print("Matriz depois da multiplicação")
for i in range(3): 
    for j in range(3): 
        print(C[i][j], end = " ") 
    print()
