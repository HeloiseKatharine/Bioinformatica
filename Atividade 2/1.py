'''
1) O arquivo toxinsNCBI.fna contém 22 sequências genômicas de mRNAs que codificam toxinas em
bactérias. Essas sequências residem na fita codificadora (5’ → 3’).
a) Crie um script python, que recebe o arquivo toxinsNCBI.fna e retorna um arquivo toxins_3-5.fna que
contém a sequência da fita molde 3’ → 5’ (lembre-se que a sequência deve ser salva na direção
5’ → 3’).
'''

import re 

filename = "toxinsNCBI.fna"
filename1 = "toxins_3-5.fna"

#lendo o arquivo de sequências
with open(filename) as fp:
    arquivo = fp.readlines() 

#transformando o arquivo em string
sequencia = ' '.join(arquivo)
sequencia = sequencia +'\n'

#dividindo cada fita
fitaCodificadora = re.split(">lcl", sequencia)

a = re.compile("A")
t = re.compile("T")
c = re.compile("C")
g = re.compile("G")

string_seq = ''

for i in range(1,len(fitaCodificadora)):#lista começa no 1 
    seq = re.split("]\n", fitaCodificadora[i])#repartindo seq com split

    letras = re.split("", seq[1])

    for j in range(len(letras)):
        if letras[j] == 'A':
           letras[j] = re.sub("A", "T",letras[j])
        elif letras[j] == 'T':
            letras[j] = re.sub("T", "A",letras[j])
        elif letras[j] == 'C':
           letras[j] = re.sub("C", "G",letras[j]) #seq[1]
        elif letras[j] == 'G':
            letras[j] = re.sub("G", "C",letras[j]) #string_seq

        string_letras = ''.join(letras)#convertendo para string

    #escrevendo no arquivo  
    with open(filename1, "a") as fp:#Insere nosvos dados no final do arquivo 
        fp.write('\n>lcl' + seq[0] + ']'+ string_letras[::-1] )
