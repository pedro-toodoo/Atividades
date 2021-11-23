Algoritmo "Tarefa 2"
// Disciplina   : Programa Blastoff
// Autor(a)    : Pedro Abritta Reis
// Data atual  : 23/11/2021
Var
km_inicio, km_fim, gas, total_gas: real
opcao: inteiro
Inicio
total_gas <- 0
escreva("Qual era a quilometragem no início da viagem? ")
leia(km_inicio)
escreva("Qual era a quilometragem no fim da viagem? ")
leia(km_fim)

repita
      escreva("Quantos litros de gasolina colocou nesta parada? ")
      leia(gas)
      escreva("Parou novamente? 1-sim / 2-não: ")
      leia(opcao)
      total_gas <- total_gas + gas
ate opcao = 2

escreval("Quilometragem rodada foi de: ", km_fim - km_inicio, "Km")
escreval("Total de litros de gasolina gastos na viagem: ", total_gas, "L")
escreva("A média de gasolina gasta foi: ", (km_fim-km_inicio)/total_gas, "Km/L")
Fimalgoritmo