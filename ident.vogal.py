letra = input ("Digite uma letra: ")

vogais = ["a", "e", "i", "o", "u"]

# A função len() retorna o tamanho de uma string ou lista
# isalpha veririca se é uma letra

if len(letra) == 1 and letra.isalpha():
    if letra in vogais:
        print ("É vogal")
        print (letra)
    else:
        print ("É consoante")
else:
    print ("Opção inválida")