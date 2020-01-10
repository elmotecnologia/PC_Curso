qalunos = int (input ("Qual a quantidade de alunos: "))
qturmas = int (input ("Informe a quantidade de turmoas: "))

if qalunos > 40:
    print ("Quantidade não permitida")
else:
    malunos = qalunos / qturmas
    print ("A quantidade média de alunos é: ", malunos)

