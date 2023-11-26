print("""
Bienvenido a la calculadora 3.0
elija una opción a realizar:
1- Suma
2- Resta
3- Multiplicación
4- División
5- Módulo
6- Expomente""")
opcion = int(input("SELECCIONA UN NUMERO Y COLOCA ENTER: "))

if opcion == 1:
    print("seleccionaste suma...")
    n1 = float(input("coloca el primer número: "))
    n2 = float(input("coloca el segundo número: "))
    resultado = round(n1 + n2, 2)
    print(f"el resultado de tu suma es: {resultado}")
elif opcion == 2:
    print("seleccionaste resta...")
    n1 = float(input("coloca el primer número: "))
    n2 = float(input("coloca el segundo número: "))
    resultado = round(n1 - n2, 2)
    print(f"el resultado de tu resta es: {resultado}")
elif opcion == 3:
    print("seleccionaste multiplicación...")
    n1 = float(input("coloca el primer número: "))
    n2 = float(input("coloca el segundo número: "))
    resultado = round(n1 * n2, 2)
    print(f"el resultado de tu multiplicacion es: {resultado}")
elif opcion == 4:
    print("seleccionaste division...")
    n1 = float(input("coloca el primer número: "))
    n2 = float(input("coloca el segundo número: "))
    if n2 == 0:
        print("No puedes dividir un número entre cero")
    else:
        resultado = round(n1 / n2, 2)
        print(f"el resultado de tu división es: {resultado}")
elif opcion == 5:
    print("seleccionaste Módulo...")
    n1 = float(input("coloca el primer número: "))
    n2 = float(input("coloca el segundo número: "))
    resultado = round(n1 // n2, 2)
    print(f"el resultado de tu Módulo es: {resultado}")
elif opcion == 6:
    print("seleccionaste exponente...")
    n1 = float(input("coloca el número que quieres elevar: "))
    n2 = float(input("coloca el exponente: "))
    resultado = round(n1 ** n2, 2)
    print(f"el resultado de tu Exponente es: {resultado}")
else:
    print("Opción inválida, vuelve a ejecutar la calculadora")