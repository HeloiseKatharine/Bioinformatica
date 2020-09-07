'''
b) Agora crie um script que receba toxins_3-5.fna e transforme as sequências genômicas em
sequências de mRNA (na direção 5’-3’) que devem ser salvas no arquivo mRNA_toxins.fna.
'''
import re 

filename = "toxins_3-5.fna"
filename1 = "mRNA_toxins.fna"

#lendo o arquivo de sequências
with open(filename) as fp:
    arquivo = fp.readlines() 

#transformando o arquivo em string
sequencia = ' '.join(arquivo)

#dividindo cada fita
fitaCodificadora = re.split(">lcl", sequencia)

for i in range(1,len(fitaCodificadora)):#lista começa no 1 
    seq = re.split("]\n", fitaCodificadora[i])#repartindo seq com split

    letras = re.split("", seq[1])

    for j in range(len(letras)):
        if letras[j] == 'A':
           letras[j] = re.sub("A", "T",letras[j])
        elif letras[j] == 'T':
            letras[j] = re.sub("T", "U",letras[j])
        elif letras[j] == 'C':
           letras[j] = re.sub("C", "G",letras[j]) #seq[1]
        elif letras[j] == 'G':
            letras[j] = re.sub("G", "C",letras[j]) #string_seq
        elif letras[j] == ' ':
            letras[j] = re.sub(" ", "",letras[j])

        string_letras = ''.join(letras)#convertendo para string

    with open(filename1, "a") as fp:#Insere nosvos dados no final do arquivo 
        fp.write( '>lcl'+ seq[0]+ ']\n' + string_letras[::-1])