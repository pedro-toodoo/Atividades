frase = " Fala cmg bb!    "

print(frase[9:11]) #Pega caracteres d 9 até 10
print(frase[3:11:2]) #Pega elementos pulando de 2 em 2
print(frase[:5]) #Começa do início até o caracter 5
print(frase[3::3]) #começa do caracter 3 e vai pulando de 3 em 3 até o final
print(len(frase)) #tamanho
print(frase.count("a")) #Conta quantas vezes a letra 'a' aparece
#com fatiamento: frase.count('a', 0, 12)
print(frase.find("bb"))
print(frase.replace("cmg", "comigo"))
print(frase.upper()) #coloca tudo maiúsculo
print(frase.lower()) #coloca tudo minúsculo
print(frase.capitalize()) #deixa a primeira letra maiúscula
print(frase.title()) #cada palavra começa com maiúsculo
print(frase.strip()) #remore espaços antes e no final da frase (rstrip e lstrip)
print(frase.split()) #divide palavras em uma lista
print("-".join(frase)) #separa todos os caracteres por "-"