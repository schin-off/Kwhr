kWh = float(input("Quantos kWh? "))
tipo = input("Qual o tipo de instalação? (R, C, I) \n")
tipo = tipo.upper()

if tipo == "R":
    if kWh <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif tipo == "C":
    if kWh <= 1000:
        preco = 0.55
    else:
        preco = 0.6
elif tipo == "I":
    if kWh <= 5000:
        preco = 0.55
    else:
        preco = 0.6
else:
    print('Instalação invalida!')

print(f"Total a pagar: R${kWh * preco}")