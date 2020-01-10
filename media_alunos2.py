qtdTurma = int (input ("Qual a quantidade de turma? "))

contador = 0
media = 0

while contador < qtdTurma:
    alunos = int (input ("Qual a quantidade de alunos? "))

    if alunos > 40 or alunos <= 0:
        print ("Quantidade acima do permitido")
    else:    
        media = media + alunos
        contador = contador + 1

#media = media / qtdTurma

print ("A média é {}".format (media/qtdTurma))