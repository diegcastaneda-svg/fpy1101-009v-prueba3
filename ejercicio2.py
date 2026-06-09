stock_libros = 120
prestamos_activos = 0
historial_prestamos = 0

print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

while True:

    print("\n===MENÚ PRINCIPAL===")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Libros disponibles: {stock_libros}")

    elif opcion == "2":

        while True:
            try:
                cantidad = int(input("Ingrese cantidad de libros a prestar: "))

                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0.")
                elif cantidad > stock_libros:
                    print("No hay suficientes libros disponibles.")
                else:
                    stock_libros -= cantidad
                    prestamos_activos += cantidad
                    historial_prestamos += cantidad
                    print("Préstamo realizado correctamente.")
                    break

            except ValueError:
                print("Ingrese un numero valido.")

    elif opcion == "3":

        while True:
            try:
                cantidad = int(input("Ingrese cantidad de libros a devolver: "))

                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0.")
                elif cantidad > prestamos_activos:
                    print("No puede devolver más libros de los prestados.")
                elif stock_libros + cantidad > 120:
                    print("No se puede superar la capacidad máxima de 120 libros.")
                else:
                    stock_libros += cantidad
                    prestamos_activos -= cantidad
                    print("Devolución realizada correctamente.")
                    break

            except ValueError:
                print("Ingrese un numero valido.")

    elif opcion == "4":
        print(f"Préstamos activos: {prestamos_activos}")
        print(f"Total de préstamos realizados durante la sesión: {historial_prestamos}")

    elif opcion == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break

    else:
        print("Opción invalida.")