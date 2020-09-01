#Crie um programa em python que calcula o fatorial de um número fornecido pelo usuário

num = int(input("Digite um valor: "))

if num == 0 or num == 1:
    print('O fatorial é 1')

if num > 1:
    fat = 1
    while num > 1:
        fat = fat * num
        num = num - 1

    print('O fatorial é {}'.format(fat))