

def arquivoExiste(nome):
    try:
        a = open(nome, "rt") #abrir arquivo para read e text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, "wt+") #abrir arquivo para write e se não existir arquivo criar um (+)
        a.close()
    except:
        print("Não foi possível criar o arquivo... ")
    else:
        print(f"Arquivo '{nome}' criado com sucesso!")

def lerArquivo(nome):
    try:
        a = open((nome, "rt"))
    except:
        print("Erro ao abrir o arquivo...")
