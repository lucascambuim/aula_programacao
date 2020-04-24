#Lendo dados da Matriz A
A = []
for i in range(2):          
    a = [] 
    x, y = input("Informe os elementos da linha %d da matriz A 2x2 seperado por espaço: " % (i+1)).split()  
    a.append(int(x))
    a.append(int(y)) 
    A.append(a)
    
#Lendo dados da Matriz A
B = []
for i in range(2):          
    a = [] 
    x, y = input("Informe os elementos da linha %d da matriz B 2x2 seperado por espaço: " % (i+1)).split()  
    a.append(int(x))
    a.append(int(y)) 
    B.append(a)

#Calculando a Matriz C
C = []
for i in range(2):
    x = []
    for j in range(2):
        x.append(A[i][j] + B[i][j])
    C.append(x)

# Imprimindo a Matriz A
print("MATRIZ A")
for i in range(2): 
    for j in range(2): 
        print(A[i][j], end = " ") 
    print()
    
# Imprimindo a Matriz B
print("MATRIZ B")
for i in range(2): 
    for j in range(2): 
        print(B[i][j], end = " ") 
    print() 
    
# Imprimindo a Matriz C
print("MATRIZ C")
for i in range(2): 
    for j in range(2): 
        print(C[i][j], end = " ") 
    print() 

