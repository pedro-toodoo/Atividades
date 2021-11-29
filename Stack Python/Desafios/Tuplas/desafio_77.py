tupla = ("pedro", "abritta", "reis", "engenharia", "computaçao", "python", "blastoff", "tooDoo")

for i in tupla:
    print(f"\nPalavra {i}: ", end="")
    for vogal in i:
        if vogal == "a" or vogal == "e" or vogal == "i" or vogal == "o" or vogal == "u":
            print(vogal, end=" ")