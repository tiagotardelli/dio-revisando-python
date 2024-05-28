preco = 10
print(preco)
#>>> 10
preco = float(preco)
print(preco)
#>>> 10.0
preco = 10 / 2
print(preco)
#>>> 10.0
preco = 10 // 2
print(preco)
#>>> 10
preco = 10.30
print(preco)
#>>> 10.30
preco = int(preco)
print(preco)
#>>> 10
preco = 10.50
idade = 28
print(str(preco))
#>>> 10.5
print(str(idade))
#>>> 28
texto = f"idade {idade} preco {preco}"
print(texto)
#>>> idade 28 preco 10.5

preco = "10.50"
idade = "28"
print(float(preco))
#>>> 10.50
print(int(idade))
#>>> 28

preco = "python"
print(float(preco))
#>>> erro na conversão


print(type(str(10.10)))
#>>> <class 'str'>
