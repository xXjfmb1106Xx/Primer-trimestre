print(" EJERCICIO 1 \n")
print(" LISTA DE PRODUCTOS \n")
productos= []
productos.append(input("ingresa un producto "))
productos.append(input("ingresa otro producto "))
productos.append(input("ingresa otro producto "))
print(f"su lista de productos tiene \n {productos}")

print(" EJERCICIO 2 \n")
print(" PRECIO DE 3 ARTICULOS \n")
precios=[]
precios.append(float(input("ingresa el precio del primer articulo ")))
precios.append(float(input("ingresa el precio del segundo producto")))
precios.append(float(input("ingresa el precio del tercer producto")))
op= precios[0] + precios[1] + precios[2]
print(f"El precio total a pagar es de {op}")

print(" EJERCICIO \n")
print(" NUMEROS MAYOR Y MENOR \n")
numeros=[]
numeros.append(int(input("ingresa el primer numero: ")))
numeros.append(int(input("ingresa el segundo numero: ")))
numeros.append(int(input("ingresa el tercer numero: ")))
print(f"el numero mayor es",{max(numeros)},"y el menor es",{min(numeros)})



