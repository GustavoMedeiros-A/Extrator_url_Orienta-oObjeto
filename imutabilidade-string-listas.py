# Estão alocados no mesmo espaço de memória, já que string são objetos imutáveis

x = 'abc'
y = 'abc'

print(id(x))
print(id(y))

print(id(x) == id(y))

print()

# Estão alocados em espaços diferentes na memória pois lista são objetos mutáveis

a = ['a', 'b', 'c']
b = ['a', 'b', 'c']

print(id(a))
print(id(b))

print(id(a) == id(b))