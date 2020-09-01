'''
Crie um programa em python que receba do usuário uma sequência de DNA e retorne a quantidade de possíveis substrings de tamanho 4 (sem repetições).
Ex.: Entrada: actgactgggggaaa
Após a varredura de toda a sequência achamos as substrings actg, ctga, tgac, gact, ctgg, tggg, gggg, ggga, ggaa, gaaa, logo a saída do programa deve ser:
Saída: 10
'''

seq = input('Digite a sequência de DNA: ')#recebe a sequência de DNA

tam_seq = len(seq) #tamanho da string seq
tam_sub = 4 #declarando o tamanho da substring 

dic_sub = dict()

for i in range(tam_seq - tam_sub + 1): #percorre toda a string
    sub = seq[i:i+tam_sub] #percorre a sequência de acordo com o tamanho da substring
    if(sub in dic_sub):
        dic_sub[sub] += 1
    else:
        dic_sub[sub] = 1

quant = len(dic_sub.keys())
print (quant)


