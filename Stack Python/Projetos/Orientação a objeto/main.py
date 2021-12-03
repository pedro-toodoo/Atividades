from pessoa import *

#criando um objeto à partir de uma classe (usando um molde para criar uma pessoa)
p1 = Pessoa("Pedro", 23)
p2 = Pessoa("Mantega", 23)

#estão em locais diferentes da memória
print(p1)
print(p2)

p1.comer("arroz")
p1.comer("terra")
p1.pararFalar()
p1.pararComer()
p1.falar("jujutsu kaisen")
p1.falar("jujutsu kaisen")
p1.comer("churrasco")
p1.pararFalar()
p1.comer("churrasco")

#variável da classe
print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)

print(p1.get_ano_nasc())