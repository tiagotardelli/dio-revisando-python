saldo, saque, limite = 1000, 200, 100
print(saldo >= saque)
#>>> True
print(saque <= limite)
#>>> False
print(saldo >= saque and saque <= limite)
#>>> False
print(saldo >= saque and saque <= limite)
#>>> True
print(not 1000 > 500)
#>>> False

#Lista vazia em python é considerado falso
contato_emergencia = []
print(not contato_emergencia)
#>>> True
not "saque 1500"
#>>> False
not ""
#>>> True
conta_especial = True
print((saldo >= saque and saque <= limite) or (conta_especial == True and saldo >= saque))

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)