Costo = 0
TotalC = 0
CostoEnv = 1500
total = 0
Id = 0

total = input("¿Cuántas cajas se van vender? ")
Id = input("¿Cuál es la Id del producto? ")
total = int(total)
Id = int(Id)

if total <= 100:
    if Id == 1:
        Costo = 285.55
        TotalC = int(total) * int(Costo)
        TotalC = TotalC+CostoEnv
        print("El producto es Maíz grano")
        print("El precio por caja es " + str(Costo))
        print("El costo total a pagar es " + str(TotalC))
    elif Id == 2:
        Costo = 334.72
        TotalC = int(total) * int(Costo)
        TotalC = TotalC+CostoEnv
        print("El producto es Pepino")
        print("El precio por caja es " + str(Costo))
        print("El costo total a pagar es " + str(TotalC))
    elif Id == 3:
        Costo = 129.00
        TotalC = int(total) * int(Costo)
        TotalC = TotalC+CostoEnv
        print("El producto es Tomate verde")
        print("El precio por caja es " + str(Costo))
        print("El costo total a pagar es " + str(TotalC))        
else:
    print("No se puede realizar la venta")