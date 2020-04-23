import math  

print("Informe o coeficiente a: ")
a = float(input())
if(a == 0):
    print("O coeficiente 'a' tem que ser diferente de zero para que a equação seja de segundo grau")
else:
    print("Informe o coeficiente b: ")
    b = float(input())
    print("Informe o coeficiente c: ")
    c = float(input())

    delta = b**2 - 4*a*c

    if(delta < 0):
        print("A equação não possui raízes reais")
    elif(delta == 0):
        print("A equação só possui uma raiz com valor ", end = '')
        x = -b/(2*a)
        print(x)
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("As raízes da equação são: %.2f e %.2f" % (x1, x2))

