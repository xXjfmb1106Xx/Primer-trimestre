z=()
print("""presiona 'enter' para emprezar el programa""")
while z != "off":
    z= input("$ ")
    if z == "enter":
        break

print("inicio de sesion \n")
cuenta=(input("ingrese su cuenta "))
contraseña =(input("ingrese su contraseña "))
contra=("32154")
contraseña =()
while contraseña != contra:
    contraseña=(input("contraseña incorrecta.Vuelva a intentarlo "))

print(""" SISTEMA DE CALIFICACION 
      introduzca las notas del estudiante 
      teniendo en cuenta que : 
      
      5.0 excelente promedio
      4.0 buen promedio 
      3.0 promedio regular 
      2.0 promedio perdido 
      1.0 debe mejorar 
      (el programa tomara todo promedio menor a 3.0 como perdido)
      
      EN EL BOLETIN FINAL 'TRUE'= ganado 'FALSE'= perdido \n""")

print(""" ************ SISTEMA DE CALIFICACION ************
 ************************************************* \n """)

nombre= input("Nombre y apellido del estudiante ")
grado= input("Cual es su salón ")
print(" ")
print("MATEMATICAS\n")
mnota1=float(input("Escribe la primera nota en matematicas "))
mnota2=float(input("Escribe la segunda nota en matematicas "))
mnota3=float(input("Escribe la tercera nota en matematicas "))
mpromedio=(mnota1 + mnota2 + mnota3)//3
print("")
print("INGLES\n")
inota1=float(input("Escribe la primera nota en ingles "))
inota2=float(input("Escribe la segundo nota en ingles "))
inota3=float(input("Escribe la tercera nota en ingles "))
ipromedio=(inota1 + inota2 + inota3)//3
print("")
print("ESPAÑOL\n")
enota1=float(input("Escribe la primera nota en español "))
enota2=float(input("Escribe la segunda nota en español "))
enota3=float(input("Escribe la tercera nota en español "))
epromedio = (enota1 + enota2 + enota3)//3
print("")
print("TECNOLOGIA\n")
tnota1=float(input("Escribe la primera nota en tecnologia "))
tnota2=float(input("Escribe la primera nota en tecnologia "))
tnota3=float(input("Escribe la primera nota en tecnologia "))
tpromedio= (tnota1 + tnota2 + tnota3)//3
print("")
print("HISTORIA \n")
hnota1=float(input("Escribe la primera nota en historia "))
hnota2=float(input("Escribe la primera nota en historia "))
hnota3=float(input("Escribe la primera nota en historia "))
hpromedio= (hnota1 + hnota2 + hnota3)//3

a= (mpromedio >= 3.0)
b= (ipromedio >= 3.0)
c= (epromedio >= 3.0)
d= (tpromedio >= 3.0)
e= (hpromedio >= 3.0)

print(f""" BOLETIN FINAL \n
      {nombre}
      grado: {grado}
      
      'PROMEDIO POR MATERIA'
      MATEMATICAS   {mpromedio}      GANÓ = {a}
      INGLES        {ipromedio}      GANÓ = {b}
      ESPAÑOL       {epromedio}      GANÓ = {c}
      TECNOLOGIA    {tpromedio}      GANÓ = {d}
      HISTORIA      {hpromedio}      GANÓ = {e}""")

fpromedio= (mpromedio + ipromedio + epromedio + tpromedio + hpromedio)//5
print(f"el promedio final es de {fpromedio}")

if fpromedio >= 3.0:
    print(f"el estudiante {nombre} paso el periodo \n")
else: print(f"el estudiante {nombre} debe recuperar \n")

while z != "off":
    z= input("$ ")
    if z == "again":
        def reinicio_codigo():
            print("REINICIO \n")
