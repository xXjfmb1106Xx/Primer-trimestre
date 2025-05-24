print("REGISTRO DE PRODUCTOS ")

nombre= input("nombre del producto ")
precio= float(input("precio por unidad "))
cantidad= int(input("cantidad comprada "))
costo= (precio * cantidad)

tupla= (nombre,precio)
lista= [tupla,cantidad]

datos={ "producto": lista}
print(f"{datos}, el total a pagar es {costo}\n")

print(" FACTURA DE MULTIPLES PRODUCTOS")

nombre_producto1=input("Nombre del producto ")
precio_unidad1= float(input("Precio por unidad "))
cantidad_comprada1= int(input("Cantidad "))

nombre_producto2=input("Nombre del producto ")
precio_unidad2= float(input("Precio por unidad "))
cantidad_comprada2= int(input("Cantidad "))

nombre_producto3=input("Nombre del producto ")
precio_unidad3= float(input("Precio por unidad "))
cantidad_comprada3  = int(input("Cantidad "))

costo1= precio_unidad1 * cantidad_comprada1
costo2= precio_unidad2 * cantidad_comprada2
costo3= precio_unidad3 * cantidad_comprada3

tupla1= (nombre_producto1,precio_unidad1)
tupla2= (nombre_producto2,precio_unidad2)
tupla3= (nombre_producto3,precio_unidad3)

lista1= [tupla1,cantidad_comprada1]
lista2= [tupla2,cantidad_comprada2]
lista3= [tupla3,cantidad_comprada3]

factura= {"producto 1": lista1,
          "producto 2": lista2,
          "producto 3": lista3
          }
print(f""" FACTURA DEL CLIENTE 
            {factura}
            
            {costo1}
            {costo2}
            {costo3} \n
            Total a pagar: {(costo1+costo2+costo3)}""")




