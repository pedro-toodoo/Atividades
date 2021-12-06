#USA UM OBJETO
from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor("Pedro")
caneta = Caneta("BIC")
maquina = MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)
maquina.escrever()

escritor.ferramenta = caneta #associação
escritor.ferramenta.escrever()