#Validar se os objetos estão na mesma região de memória
curso - "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
#>>> True
curso in not nome_curso
#>>> False
saldo is limite
#>>> True

saldo = 10000
limite = 500
print(saldo is limite)
#>>> False
print(saldo is not limite)
#>>> True