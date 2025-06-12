# print("ejercicio 1")
# num= int(input("ingrese numero "))
# if num == 0:
#     print("es cero")
# elif num > 0:
#     print("es positivo")
# elif num < 0:
#     print("es negativo")
    
# print("ejercicio 2")
# num1= int(input("ingrese un numero "))
# num2= int(input("ingrese otro numero "))
# if num1 > num2:
#     print("el primer numero es mayor")
# elif num1 < num2 :
#     print("el segundo numero es mayor")
# else: print("los dos son iguales")

# print("ejercicio 3")
# num3= int(input("ingrese un numero "))
# ope= num3 %2
# if ope == 0:
#     print("es par")
# else: print("es impar")


# print("ejercicio 4")
# num4= int(input("ingrese un numero "))
# if num4 > 10 and num4 < 20:
#     print("el numero esta entre 10 y 20")
# else: print("el numero es mayor a 20")

# print("ejercicio 5")
# num5= int(input("ingrese un numero "))
# num5_1= int(input("ingrese otro numero "))
# num5_2= int(input("ingrese otro numero "))

# if num5 > num5_1 and num5 > num5_2:
#     print("el primer numero es el mayor")
# elif num5_1 > num5 and num5_1 > num5_2:
#     print("el segundo numero es el mayor")
# elif num5_2 > num5 and num5_2 > num5_1:
#     print("el tercer numero es el mayor")
# else: print("todos son iguales")

# print("ejercicio 6")
# precio1= int(input("cual es el precio del producto? "))
# descuento= precio1 * 0.10
# if precio1 > 100:
#     print(f"el precio del producto mas un 10% de descuento es {descuento}")

# print("ejercicio 7")
# edad= int(input("ingrese su edad "))
# if edad >= 18:
#     print("puede votar")
# else: print("no puede votar")

# print("ejercicio 8")
# membresia= input("cual es su tipo de membresia ").upper()
# precio= int(input("cual es el precio del producto? "))
# descuento1= precio * 0.20
# if membresia == "VIP":
#     print(f"el precio del producto mas 10% de descuento es {descuento}")
# else: print("no aplica para descuento del 10%")

# print("ejercicio 9")
# num9= int(input("ingrese un numero"))
# if num9 %5 and num9 %3:
#     print("el numero es multiplo de 5 y de 3")
# else: print("el numero no es multiplo de 5 y 3")

# print("ejercicio 10")
# num10= int(input("ingresa un numero"))
# num10_1= int(input("ingresa otro numero"))
# num10_2= int(input("ingresa otro numero"))

# if num10 // num10_1 and num10 // num10_2:
#     print("el primer numero es divisible en los otros dos")
# else: print("el primer numero no es divisible en los otros dos")

# print("ejercicio 11")
# num11= int(input("ingrese numero 1"))
# num11_1= int(input("ingrese numero 2"))
# num11_2= int(input("ingrese numero 3"))
# num11_3= int(input("ingrese numero 4"))
# num11_4= int(input("ingrese numero 5"))
# lista= [num11,num11_1,num11_2,num11_3,num11_4]
# if lista[2] > 10 :
#     print(" es mayor a 10")
# else: print("es menor a 10")

# print("ejercicio 12")
# lista2=[3,5,7,9]
# if lista2[0:] == 7:
#     print("esta en la lista")
# else:  print("no esta en la lista")

# print("ejercicio 13")
# lista3=[4,6,2,8]
# operacion= lista3[0] + lista3[1]
# if operacion > 10:
#     print("suma alta")
# else: print("suma baja")

# print("ejercicio 14")
# lista4= ["Ana","Luis","Pedro","Marta"]
# if lista4[-1] == "Marta":
#     print("Nombre correcto")
# else: print("nombre diferente")

# print("ejercicio 15")
# color1= input("ingrese primer color")
# color2= input("ingrese segundo color")
# color3= input("ingrese tercer color")
# lista5=[color1,color2,color3]
# if lista5[1] == "azul":
#     color2= input("debes cambiar el color ")
# print(f"la lista actualizada es {lista5}")

# print("ejercicio 16")
# tupla= (5,8,12,20)
# if tupla[0] > tupla[-1]:
#     print("oreden descendente")
# elif tupla[0] < tupla[-1]:
#     print("orden ascendente")
# else: print("son iguales")

# print("ejercicio 17")
# tupla1=(25,32,28)
# if tupla1[1] > 30:
#     print("edad mayor a 30")
# else: print(" edad menor o igual a 30")

# print("ejercicio 18")
# tupla3= (1,2,3)
# tupla3= list
# if tupla3[1] == 2:
#     tupla3[1]= 10
# tupla3= tuple
# print(tupla3)

# print("ejercicio 19")
# tupla4= (4,9)
# if tupla4[1] > 5:
#     print("coordenada alta")
# else: print("coordenada baja")

# print("ejercicio 20")
# tupla5=(3,4)
# tupla6=(3,5)
# comp= tupla5 == tupla6
# if comp == False:
#     print("tuplas diferentes")
# elif comp == True:
#     print("tuplas iguales")

# print("ejercicion 21")
# diccionario={
#     "nombre": "juan",
#     "edad": 17
# }
# if diccionario[edad] >= 18:
#     print("es  mayor de edad")
# else: print("es menor de edad")

# print("ejercicio 22")
# diccionario1= {
#     "nombre": "Lucia",
#     "edad": 20
# }
# if diccionario1[edad] >= 18:
#     diccionario1[edad]= 21
# print(diccionario1)

# print("ejercicio 23")
# diccionario2={"nombre": "carlos"}
# if "ciudad" in diccionario2:
#     print(diccionario2)
# else:
#     diccionario2["ciudad"]= "bogota"

# print("ejercicio 24")
# diccionario3= {
#     "producto":"pan",
#     "precio": 1200
# }
# if "precio" in diccionario3:
#     print(diccionario3[1])
# else: print("no hay precio")

# print("ejercicio 25")
# diccionario4={
#     "pan": 1200,
#     "leche": 2000
# }
# if "pan" in diccionario4:
#     print(diccionario4)
# else: print("producto no disponible")

