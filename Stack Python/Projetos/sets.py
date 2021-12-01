s = {1, 3.1415, "TooDoo", 1, 3.1415}

print(type(s))
print(s) #só armazena valores diferentes
print(f"Tipo: {type(s)} - Valores: {s}")

print("---OPERAÇÕES---")
x = {1, 2, 3, 4.15}
y = {3, 2, 1, 25}

print(f"União: {x | y}")
print(f"Diferença X - Y: {x - y}")
print(f"Diferença Y - X: {y - x}")
print(f"Interseção: {x & y}")