# Quadros de leitura (+1, +2, +3, -1,-2,-3)

*Aluna: Heloise Katharine*

## Instruções de compilação/execução

Insira no arquivo **gene.fasta** uma sequência para gerar os quadros de leitura da mesma. 

Ex: 

    >gene
    ATGACCGAAAAAGAGCATTTTTTTTGGAATAAGCTCTTAGAGCTGGCCAAAGAAGAACTAACACAAGCCACTTTTGATTATTATGTCCTAGATACCAAGCTCATCAAAATTCAAGATAACGTTGCT


### Saída  

Será salvo em um arquivo denominado **orfs.fasta** os quadros de leitura da sequência 

Ex: 

    >orf +1
    ATGACCGAAAAAGAGCATTTTTTTTGGAATAAGCTCTTAGAGCTGGCCAAAGAAGAACTAACACAAGCCACTTTTGATTATTATGTCCTAGATACCAAGCTCATCAAAATTCAAGATAACGTTGCT
    >orf +2
    TGACCGAAAAAGAGCATTTTTTTTGGAATAAGCTCTTAGAGCTGGCCAAAGAAGAACTAACACAAGCCACTTTTGATTATTATGTCCTAGATACCAAGCTCATCAAAATTCAAGATAACGTTG
    >orf +3
    GACCGAAAAAGAGCATTTTTTTTGGAATAAGCTCTTAGAGCTGGCCAAAGAAGAACTAACACAAGCCACTTTTGATTATTATGTCCTAGATACCAAGCTCATCAAAATTCAAGATAACGTTGC
    >orf -1
    AGCAACGTTATCTTGAATTTTGATGAGCTTGGTATCTAGGACATAATAATCAAAAGTGGCTTGTGTTAGTTCTTCTTTGGCCAGCTCTAAGAGCTTATTCCAAAAAAAATGCTCTTTTTCGGTCAT
    >orf -2
    GCAACGTTATCTTGAATTTTGATGAGCTTGGTATCTAGGACATAATAATCAAAAGTGGCTTGTGTTAGTTCTTCTTTGGCCAGCTCTAAGAGCTTATTCCAAAAAAAATGCTCTTTTTCGGTC
    >orf -3
    CAACGTTATCTTGAATTTTGATGAGCTTGGTATCTAGGACATAATAATCAAAAGTGGCTTGTGTTAGTTCTTCTTTGGCCAGCTCTAAGAGCTTATTCCAAAAAAAATGCTCTTTTTCGGTCA