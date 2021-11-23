Algoritmo "Tarefa 4"
// Disciplina   : Programa Blastoff
// Autor(a)    : Pedro Abritta Reis
// Data atual  : 23/11/2021
Var
saldo_inicial, cheque: real

Inicio
escreva("Informe o saldo inicial: ")
leia(saldo_inicial)
escreva("Informe o valor do cheque para ser descontado: ")
leia(cheque)

se(cheque <= saldo_inicial) entao
     escreval("Cheque no valor de R$", cheque, " descontado com sucesso! ")
     escreva("O valor do saldo atual é: R$ ", saldo_inicial - cheque)
senao
     escreval("Impossibilitado de descontar o cheque!")
fimse
Fimalgoritmo