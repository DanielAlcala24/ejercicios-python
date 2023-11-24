print("bienvenido a la calculadora")

print("Selecciona la opción que deseas realizar...")
print("""1. suma
2. resta
3. multiplicacion
4. división
""")
k = int(input("->"))

numero_1 = float(input("ingresa el primer número "))
numero_2 = float(input("ingresa el segundo número "))

def Suma():
    resultado = numero_1 + numero_2
    
    return resultado

def Resta():
    resultado = numero_1 - numero_2
    
    return resultado

def Multiplicacion():
    resultado = numero_1 * numero_2
    
    return resultado

def Division ():
    resultado = numero_1 / numero_2
    
    return resultado

if k == 1 :
    resultado = Suma()
    
    print(f"el resultado de tu suma es {resultado}")

elif k == 2 :
    resultado = Resta()
    
    print(f"El rewsultadio de tu resta es {resultado}")
    
elif k == 3 :
    resultado = Multiplicacion()
    
    print(f"El resultado de tu multiplicacion es {resultado}")
    
elif k == 4 :
    resultado = Division()
    
    print(f"El resultado de tu división es {resultado}")

else :
    print("has seleccionado un valor incorrecto")
    
    
    