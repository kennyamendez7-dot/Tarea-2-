#Constante 
MIN_STOCK = 5

# Variables
productName = ""
price = 0.0
quantity = 0
continueChoice = ""

#Acumuladores
totalInventoryValue = 0.0
totalProductsRegistered = 0
totalProductsToReplenish = 0

#Ciclo para ingresar productos al inventario
continueChoice = 's'

while continueChoice == 's':

    #Datos del producto
    productName = input("Ingrese el nombre del producto: ")
    price = float(input("Ingrese el precio unitario: "))
    

     # Validaciones del precio y cantidad
    if price <= 0:
        print("Error: El precio no puede ser negativo.")
    else:
        quantity = int(input("Ingrese la cantidad en existencia: "))

        if quantity < MIN_STOCK:
            print("La cantidad en existencia requiere reposicion.")
            totalProductsToReplenish = totalProductsToReplenish + 1
        else:
            print(f"Se estan ingresando {quantity} productos, marcados en un precio de {price} para cada unidad, se registran bajo el nombre de: {productName}.")

       #Confirmación de los datos ingresados
        if price > 0 and quantity >= 0:
            confirmChoice = input(f"¿Desea confirmar los datos ingresados para {productName}? (s/n): ")
        if confirmChoice == 's':
            print(f"Datos confirmados para {productName}, el producto ha sido registrado.")
            totalProductsRegistered = totalProductsRegistered + 1
       
            #Cálculo del valor total del inventario
            totalValue = price * quantity
            totalInventoryValue = totalInventoryValue + totalValue
            
    # Confirmación para continuar o salir del ciclo
    continueChoice = input("¿Desea continuar? (s/n): ")

#Resumen del inventario
print("Resumen del inventario:")  
print(f"Total de productos registrados: {totalProductsRegistered}")
print(f"Total de productos que requieren reposición: {totalProductsToReplenish}")
print(f"Valor total del inventario: {totalInventoryValue}")