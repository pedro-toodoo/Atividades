import numpy as np

qnt = [1, 2, 3, 4, 5]
custo = [100, 200, 300, 400, 500]

#transformar lista em array
arr1 = np.array(qnt)
arr2 = np.array(custo)

estoque = arr2 * arr1
print("Listas transformadas em array:")
print(arr1)
print(arr2)
print(f"Multiplicando arrays: {estoque}")

print(f"Usando arange(): {np.arange(10, 20)}")
print(f"Usando arange(): {np.arange(10, 21, 2)}")
oi = np.arange(10, 101, 2, dtype=float)
print(f"Usando arange(): {oi}")

print(f"Usando inspace(): {np.linspace(1, 5, 10)}") #1 até 5 com 10 elementos

print(f"Array com 10 valores entre 0 e 1: {np.random.rand(10)}")
print(f"Array com 5 valores: {np.random.randn(5)}")
print(f"Array com 30 valores aleatórios entre 1 e 100: {np.random.randint(1, 100, 30)}")

print(f"Matriz preenchida com zeros: \n{np.zeros((3, 3))}")
print(f"Matriz preenchida com um: \n{np.ones((3, 3))}")
print(f"Matriz identidade: \n{np.eye(5)}")


print(f"Pegando valores do array: {oi[2:5]}")
print(f"Pegando primeiros valores até o índice 5: {oi[:5]}")
print(f"Pegando do índice 3 até o final: {oi[5:]}")

oi2 = np.random.randint(10, 51, size=(3,3))
print(f"Matriz: \n{oi2}")
print(oi2[1][2]) #[LINHA][COLUNA]
print(oi2[1, 2]) #igual a linha acima
print(f"Pegando valores da linha 2 e colunas 0 e 1: {oi2[2][0:2]}")

cadastro = np.random.randint(1, 101,size=(50,10))
print(cadastro)

cadatro_maior18 = cadastro > 18
print(f"Valores maiores doq 18 (bool): {cadatro_maior18}")
print(f"Apenas valores maiores doq 18: {cadastro[cadatro_maior18]}")
print(f"Quantidade acima de 18: {len(cadatro_maior18)}")
condicao = cadastro > 20

extraido = np.extract(condicao, cadastro)
print(extraido)
















