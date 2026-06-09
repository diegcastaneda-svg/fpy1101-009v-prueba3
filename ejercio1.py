especialistas = 0
residentes = 0

while True:
    try:
        cantidad_medicos = int(input("Ingrese la cantidad de médicos a registrar: "))

        if cantidad_medicos > 0:
            break

        print("¡Registro médico invalido! Ingresa un entero positivo para continuar.")

    except ValueError:
        print("¡Registro médico invalido! Ingresa un entero positivo para continuar.")

for i in range(cantidad_medicos):

    print(f"\nRegistro médico {i + 1}")

    while True:
        nombre = input("Ingrese nombre profesional: ")

        if len(nombre) >= 6 and " " not in nombre:
            break

        print("Nombre profesional invalido. Debe tener al menos 6 caracteres y no contener espacios.")

    while True:
        try:
            experiencia = int(input("Ingrese años de experiencia clinica: "))

            if experiencia > 0:
                break

            print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")

        except ValueError:
            print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")

    if experiencia > 5:
        print("Clasificación: Especialista Senior")
        especialistas += 1
    else:
        print("Clasificación: Residente Junior")
        residentes += 1

print("\n===================================")
print(f"¡El hospital cuenta con {especialistas} Especialistas Senior y {residentes} Residentes Junior!")
print("¡Sistema listo para operar!")