import re

filename = "gene.fasta" #entrada 
filename1 = "orfs.fasta" #saida

#lendo o arquivo de sequências
with open(filename) as fp:
    arquivo = fp.readlines() 

#transformando o arquivo em string
string_sequencia = ''.join(arquivo)

#dividindo cada fita
sequencia = re.split("\n", string_sequencia)

def leitura(num,sequencia, pos_neg):

    if(pos_neg == "true"):
        tam = len(sequencia[num:])
        orf = sequencia[num:]
        resto = tam % 3

        if(resto == 0):
            with open(filename1, "a") as fp:#Insere nosvos dados no final do arquivo 
                fp.write('\n'+'>orf +'+ str(num+1) +'\n'+ orf)
        else: 
            tam = len(sequencia)
            orf = sequencia[num:(tam-resto)]
            with open(filename1, "a") as fp:
                fp.write('\n'+'>orf +'+ str(num+1) +'\n'+ orf)
    else:
        sequencia = sequencia[::-1] #inverte a sequência 
        sequencia = re.split("", sequencia)

        for j in range(len(sequencia)):
                if sequencia[j] == 'A':
                    sequencia[j] = re.sub("A", "T",sequencia[j])
                elif sequencia[j] == 'T':
                    sequencia[j] = re.sub("T", "A",sequencia[j])
                elif sequencia[j] == 'C':
                    sequencia[j] = re.sub("C", "G",sequencia[j]) 
                elif sequencia[j] == 'G':
                    sequencia[j] = re.sub("G", "C",sequencia[j])

        sequencia = ''.join(sequencia)#convertendo para string

        tam = len(sequencia[num:])
        orf = sequencia[num:]
        resto = tam % 3

        if(resto == 0):
            with open(filename1, "a") as fp:#Insere nosvos dados no final do arquivo 
                fp.write('\n'+'>orf -'+ str(num+1) +'\n'+ orf)
        else: 
            tam = len(sequencia)
            orf = sequencia[num:(tam-resto)]
            with open(filename1, "a") as fp:
                fp.write('\n'+'>orf -'+ str(num+1) +'\n'+ orf)
        
#true para positiva 
#orf +1
leitura(0, sequencia[1], "true")
#orf +2
leitura(1, sequencia[1], "true")
#orf +3
leitura(2, sequencia[1], "true")

#false para negativa 
#orf -1
leitura(0, sequencia[1], "false")
#orf -2
leitura(1, sequencia[1], "false")
#orf -3
leitura(2, sequencia[1], "false")
