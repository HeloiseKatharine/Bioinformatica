#Crie um programa em python que receba do usuário uma sequência de DNA e calcule o seu conteúdo GC:

seq = input('Digite a sequência de DNA: ')

seq = seq.lower() #trasnforma em minúsculo 

a = seq.count('a')
g = seq.count('g')
c = seq.count('c')
t = seq.count('t')

resultado = (((g + c) / (a + t + g + c)) * 100)

print(resultado, "%")
