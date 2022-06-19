import sys
venta_productos = [
[2, 122],
[1, 89],
[1, 22],
[3, 48],
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]
]
Envio = 1500
venta = 0
cajas_Compra = 0
total_Cajas_Vendidas = 0
venta_Dia = 0

productos_Matriz = [[1, "Maíz grano", 285.55], 
        [2,"Pepino", 334.72], 
        [3,"Tomate verde", 129.00]]
print ("Introduzca el id del producto: ")
ID_Producto = int(input())
if(ID_Producto > 3):

    print("Producto inexistente")
    sys.exit()
else:

    if (ID_Producto >= 1):
        
        ID_Producto = ID_Producto-1
    productos_Matriz = productos_Matriz[ID_Producto]
    producto = productos_Matriz[1]
    precio = productos_Matriz[2]
    cajas_Compra =  int(input("Introduzca el numero de cajas a comprar: "))
    total_Cajas_Vendidas = cajas_Compra
    print("El producto es: " + producto)
    print("El precio por caja es: $" + str(precio))
    ID_Producto = ID_Producto+1
    for Cadena in venta_productos:
        if(int(Cadena[0]) == ID_Producto):
            cajas_Vendidas  = int(Cadena[1])
            total_Cajas_Vendidas = total_Cajas_Vendidas + cajas_Vendidas
if (cajas_Compra <= 100):
    venta_total_cajas = (total_Cajas_Vendidas * precio + Envio)
else:
    venta_total_cajas = (total_Cajas_Vendidas * precio) 
if(total_Cajas_Vendidas > 1500):
    print("Aplica descuento del 20%")
else:
    print("=====================================================")
    print("No aplica descuento del 20%")

print("=====================================================")
print("El total de cajas vendias es " + str(total_Cajas_Vendidas))
print("El costo total a pagar: $" + str(venta_total_cajas))
print("=====================================================")