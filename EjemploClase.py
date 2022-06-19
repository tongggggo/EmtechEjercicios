from ast import Compare
import random
# [id de producto]
lista_productos = [i for i in range(1,16)]

print('lista de productos:')

print(lista_productos)

# [id de venta, id de producto]
listaventas = []

# [id de venta, cantidad vendida]
unidadesvendidas = []

for i in range(1,51):
  idprod = random.randint(1,15)
  listaventas.append([i,idprod])

  idcant = str(random.randint(1,5))
  unidadesvendidas.append([i,idcant])
  
print('lista de ventas:')
print(listaventas)

print('lista de unidades vendidas:')
print(unidadesvendidas)

sumaventa = 0
ventastotales = []

for producto in lista_productos:

        sumaventa = 0
        
        for venta in listaventas:
            
            if venta[1] == producto:

                for unidades in unidadesvendidas:

                    if venta[0] == unidades[0]:

                        sumaventa += int(unidades[1])
    
        ventastotales.append(sumaventa)

print("======================================")

cont = 0

while cont < 15:

    cont += 1

    print("Ventas totales por producto")

    print("Producto " + str(cont) + ": " + str(ventastotales[cont-1]))