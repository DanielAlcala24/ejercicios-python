print("""Bienvenidos a la calculadora
para salir escribe salir
las operaciones son: suma, multi, div y resta""")

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        else:
            resultado = int(resultado)
    op = input("ingresa operación: ")
    if op.lower() == "salir":
        break
    n2 = input("ingresa el segundo número: ")
    if n2.lower() == "salir":
        break
    else:
        n2 = int(n2)
        
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("operacion no válida")
        break
    
    print(f"el resultado de tu operacion es: {resultado}")
    