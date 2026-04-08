quantidade = int(input("digite o nimero de macas compradas:"))
if quantidade < 12:
    preco =1.30
else:
    preco = 1.00
total = quantidade * preco
print("o preço final é", total)
