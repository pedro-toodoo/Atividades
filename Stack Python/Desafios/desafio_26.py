frase = input("Digite uma frase: ")

print(f"A letra 'A' aparece {frase.upper().count('A')} vezes")
print(f"A letra 'A' aparece pela primeira vez na posição {frase.upper().find('A')}")


print(f"A letra 'A' aparece pela última vez na posição {frase.upper().rfind('A')}")