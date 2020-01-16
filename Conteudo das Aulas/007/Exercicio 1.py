"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média do aluno
"""
nota1 = int(input('Inserir a nota do Trim 1:'))
nota2 = int(input('Inserir a nota do Trim 2:'))
nota3 = int(input('Inserir a nota do Trim 3:'))
nota4 = int(input('Inserir a nota do Trim 4:'))

#Media real
print ('Sua Media é: ', (nota1 + nota2 + nota3 + nota4)/4)

#Media Inteira
print ('Sua Media é: ', (nota1 + nota2 + nota3 + nota4)//4)

