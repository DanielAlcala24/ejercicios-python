print('calculadora paga neta')

horas_trabajadas = float(input('Ingrese el número de horas trabajadas: '))
tarifa_horaria = float(input('Ingrese la tarifa horaria: '))
tasa_impuestos = float(input('Ingrese la tasa de impuestos (porcentaje): ')) / 100 

def calcular_paga_neta(horas_trabajadas, tarifa_horaria, tasa_impuestos):
    paga_bruta = horas_trabajadas * tarifa_horaria
    impuestos = paga_bruta * tasa_impuestos
    paga_neta = paga_bruta - impuestos
    return paga_neta

paga_neta = calcular_paga_neta(horas_trabajadas, tarifa_horaria, tasa_impuestos)

print(f'Paga neta del trabajador: ${paga_neta:.2f}')