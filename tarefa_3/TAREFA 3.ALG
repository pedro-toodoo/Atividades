Algoritmo "Tarefa 3"
// Disciplina   : Programa Blastoff
// Autor(a)    : Pedro Abritta Reis
// Data atual  : 23/11/2021
Var
salario, financiamento: real

Inicio
escreva("Informe seu salário: ")
leia(salario)
escreva("Informe o valor do financiamento desejado: ")
leia(financiamento)

se(financiamento <= 5*salario) entao
     escreval("Financiamento concedido!")
senao
     escreval("Financiamento negado!")
fimse
escreva("Obrigado por nos consultar!")
Fimalgoritmo