from src import Guerreiro, LutaEspada, LutaArco, Curar

cavaleiro = Guerreiro(LutaEspada(6))
cavaleiro.acao()
cavaleiro.atributos()

arqueiro = Guerreiro(LutaArco(8))
arqueiro.acao()
arqueiro.atributos()

curandeiro = Guerreiro(Curar(4))
curandeiro.acao()
curandeiro.atributos()