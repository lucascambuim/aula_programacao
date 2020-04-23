#Três lados formam um triângulo quando a soma de quaisquer dois lados
#for maior que o terceiro, ou seja:

#Dados os lados a b e c do triângulo
# a < b + c
# b < a + c
# c < a + b

print("Informe o lado a: ")
a = float(input())
print("Informe o lado b: ")
b = float(input())
print("Informe o lado c: ")
c = float(input())

#condicao1: | b - c | < a < b + c
if(a < (b+c)):
    condicao1 = True
else:
    condicao1 = False
    
#condicao2: | a - c | < b < a + c
if(b < (a+c)):
    condicao2 = True
else:
    condicao2 = False
    
#condicao3: | a - b | < c < a + b
if(c < (a+b)):
    condicao3 = True
else:
    condicao3 = False

if(condicao1 == True and condicao2 == True and condicao3 == True):
    print("É um triangulo ", end = '')
    if(a == b and b == c and a == c):
        print("Equilátero")
    elif(a == b or a == c or b == c):
        print("Isosceles")
    elif(a != b and b != c and a != c):
        print("Escaleno")
else:
    print("Não é um triangulo")

