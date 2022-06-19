Cemento = 40
Yeso = 30
Camion = 3254

CantC = input("Cuántos costales de cemento se entregarán? ")
CantY = input("Cuántos costales de yeso se entregarán? ")

TotalC = int(CantC) * int(Cemento)
TotalY = int(CantY) * int(Yeso)

TotalCY = TotalC + TotalY

if TotalCY > Camion:
    print("El viaje no se puede realizar ya que supera la carga")
elif TotalCY > Camion/2:
    print("El viaje se puede realizar")
elif TotalCY < Camion/2:
    print("El viaje no se puede realizar porque no llega al 50% de la capacidad")
    
print("El total del peso es de " + str(TotalCY))