'''
Usando o mesmo arquivo de entrada, sequence.fasta , Crie um programa em python que armazena, no arquivo results.txt, o header de cada sequência, a substring de tamanho 3 mais frequente em sua sequência e a quantidade de vezes que ela ocorreu.
Obs.: caso haja empate na substring mais frequente, escolher qualquer uma entre as mais frequentes.
'''

filename = "sequence.fasta"
filename1 = "results.txt"
tam_sub = 3 #tamanho da substring

#lendo um arquivo .fasta
with open(filename) as fp:
    arquivo = fp.readlines() 

#Separando as informações do arquivo em duas listas
for i in arquivo :
    
    header = arquivo[::2] #lista de nomes
    linha = arquivo[1::2]#lista de sequência
    
    #convertendo para string
    linha = ' '.join(linha)
    linha =  linha.replace('\n', ' ')
    header = ' '.join(header)
    header =  header.replace('\n', ' ')

    #convertendo de string para lista
    lista = linha.split()
    header = header.split()

    resp = list()
    lista_sub = list()
    lista_quant = list()

    #procurando as substrings
    for i in range(len(lista)): 
        
        maior = 0
        dic_sub = dict()
        
        for j in range(len(lista[i]) - tam_sub + 1):
            
            sub = lista[i][j:j+tam_sub]
            
            if(sub in dic_sub):
                dic_sub[sub] += 1
            else:
                dic_sub[sub] = 1
            
            quant = len(dic_sub.keys())

            if(dic_sub[sub] >= maior):
                
                maior = dic_sub[sub]
                letra = sub
    
        maior = str(maior) #transformando int em string
        lista_sub.append(letra)#lista sub
        lista_quant.append(maior)#lista de quantidade

#escrevendo no arquivo
with open(filename1, "w") as fp:

    for k in range(len(header)):

        resultado  = (header[k] , lista_sub[k], lista_quant[k])
        resultado = "".join(str(resultado)).strip('[]')
        #formatando as strings
        resultado =  resultado.replace(',', ' ')
        resultado =  resultado.replace('(', '')
        resultado =  resultado.replace(')', '')
        resultado =  resultado.replace('\'', '')
        fp.write(resultado + '\n')
