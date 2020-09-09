'''
c) Por fim crie um script que recebe o arquivo mRNA_toxins.fna e transforme suas sequências de
mRNA em sequências de aminoácidos, salvando estas no arquivo toxins.faa 
'''
import re 

filename = "mRNA_toxins.fna"
filename1 = "toxins.faa"

matriz = ["F", "L", "i", "M", "V", "S", "P", "T", "A", "Y", "H", "Q", "N", "K", "D", "E", "C", "W", "R", "G","(STOP)"] 
matriz2 = [["UUU", "UUC"], ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG" ], ["AUU", "AUC", "AUA"], ["AUG"], ["GUU", "GUC", "GUA", "GUG"], ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"], ["CCU", "CCC", "CCA", "CCG"], ["ACU", "ACC", "ACA", "ACG"], ["GCU", "GCC", "GCA", "GCG"], ["UAU", "UAC"], ["CAU", "CAC"], ["CAA", "CAG"], ["AAU", "AAC"], ["AAA", "AAG"], ["GAU", "GAC"], ["GAA", "GAG"], ["UGU", "UGC"], ["UGG"], ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"], ["GGU", "GGC", "GGA", "GGG"], ["UAA", "UAG", "UGA"] ]

#lendo o arquivo de sequências
with open(filename) as fp:
    arquivo = fp.readlines() 

#transformando o arquivo em string
sequencia = ' '.join(arquivo)

#dividindo cada fita
fitaCodificadora = re.split(">lcl", sequencia)
cont = 0

for i in range(1,len(fitaCodificadora)):#lista começa no 1 
    seq = re.split("]\n", fitaCodificadora[i])#repartindo seq com split
    string_match = [] #lista
    seq[1] = re.sub(" ", "",seq[1])

    for j in range(len(matriz2)):
        for k in range(len(matriz2[j])):

            match = re.search(matriz2[j][k], seq[1])
            if match:
                start = match.start()
                end = match.end()
                letras = seq[1][start:end]
                string_match.append(letras) #insere na lista

        for l in range(len(string_match)):
            seq[1] = re.sub(string_match[l], matriz[j],seq[1])
    
    with open(filename1, "a") as fp:#Insere nosvos dados no final do arquivo 
        fp.write('>lcl'+ seq[0]+ ']\n'+seq[1])
