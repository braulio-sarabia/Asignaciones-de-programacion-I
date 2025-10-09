total_compras_exitosas=0
saldo=0
monto=0
terminar=False
print("su saldo es: ",input("cual es su saldo inicial: "))

while not terminar:
    print("su inversion es: ", input("cuanto desea invertir: "))

    if monto<saldo:

        total_compras_exitosas+1
    saldo=saldo-monto
    print("se realizo la compra")
    if saldo ==0:

            terminar=True

        elif:
        print("no se pudo realizar la compra")
        terminar=True


        print("el total de compras exitosas es: "), total_compras_exitosas
        print("el saldo restante es: "), saldo 




