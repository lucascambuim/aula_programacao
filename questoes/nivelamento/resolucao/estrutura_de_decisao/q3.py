import math

print("Informe a primeira nota parcial do aluno: ")
n1 = float(input())

print("Informe a segunda nota parcial do aluno: ")
n2 = float(input())

media = (n1 + n2)/2.0

if(media >= 9.0 and media <= 10.0):
    conceito = "A"
elif(media >= 7.5 and media < 9.0):
    conceito = "B"
elif(media >= 6.0 and media < 7.5):
    conceito = "C"
elif(media >= 4.0 and media < 6.0):
    conceito = "D"
else:
    conceito = "E"
    
print("O conceito do aluno é: ", conceito)
