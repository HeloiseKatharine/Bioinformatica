'''
 Crie um programa em python que leia o arquivo sequence.fasta (disponível no moodle), e retorne uma lista de tuplas (header,sequência), onde header é o cabeçalho da sequência (linha iniciada por “>”) e a sequência é aquela composto por nucleotídeos (a, c, t, g)
'''

#lendo um arquivo .fasta
filename = "sequence.fasta"

#colocando o arquivo em uma lista 
with open(filename) as fp:
    arquivo = fp.readlines()

#Separando as informações do arquivo em duas listas
for i in arquivo :
    
    lista1 = arquivo[::2] #lista de nomes
    lista2 = arquivo[1::2]#lista de sequência

#convertendo a lista1 em string para tirar os ">"
lista1_string = ' '.join(lista1)
lista1_string = lista1_string.replace('>', '')

#convertendo a lista2 em string para tirar os "\n"
lista2_string = ' '.join(lista2)
lista2_string = lista2_string.replace('\n', '')


#convertendo de string para lista
lista1 = lista1_string.split()
lista2 = lista2_string.split()

#convertendo para uma lista de tuplas
lista = list(zip(lista1, lista2)) #criando uma lista de tuplas 

#formatando a saida
for nome, seq in lista:
    print("(" +nome+" , " +seq+")" )
