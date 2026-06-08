#Ejercicio 2 prueba parcial 3

#Definiendo total del libros y cantidad reservada
libros_disponibles  = 120
libros_reservados   = 0
historial_prestamos = 0

#Bienvenida
print ("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

#Menu principal
while True:
    print ("===MENÚ PRINCIPAL===")
    print ("1. Libros disponibles")
    print ("2. Realizar préstamo")
    print ("3. Devolver préstamo")
    print ("4. Historial de préstamos")
    print ("5. Salir")

#Asegurando opcion valida
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            break
        except ValueError:
            print ("¡Debe ingresar una opcion valida!")

#Funcionalidades del sistema
#Libros disponibles
    if opcion == 1:
        print ("La cantidad de libros disponibles es: ", libros_disponibles)

#Realizar prestamo
    elif opcion == 2:
        while True:
            try:
                cantidad_a_reservar = int(input("Ingrese la cantidad de libros a reservar: "))
                if cantidad_a_reservar <= 0:
                    print("La cantidad debe ser un numero positivo")
                elif cantidad_a_reservar <= libros_disponibles:
                    print("Reservando", cantidad_a_reservar, "libros")
                    libros_disponibles -= cantidad_a_reservar
                    libros_reservados += cantidad_a_reservar
                    historial_prestamos += cantidad_a_reservar
                    break
                elif libros_disponibles < cantidad_a_reservar:
                    print ("No existen suficientes libros actualmente")
            except ValueError:
                print("¡Debe ingresar una cantidad valida!")

#Devolver prestamo
    elif opcion == 3:
        while True:
            try:
                devolver_libros = int(input("Ingrese la cantidad de libros a devolver: "))
                if devolver_libros <= 0:
                    print("La cantidad debe ser un numero positivo")
                elif devolver_libros > libros_reservados:
                    print("No puede devolver más libros de los que están prestados")
                elif libros_disponibles + devolver_libros > 120:
                    print("¡No puede superar la capacidad maxima de 120 libros!")
                else:
                    print ("Devolviendo", devolver_libros, "libros")
                    libros_disponibles += devolver_libros
                    libros_reservados -= devolver_libros
                    historial_prestamos -= devolver_libros
                    break
            except ValueError:
                print ("¡Debe ingresar una cantidad valida!")
                            
#Historial de prestamos
    elif opcion == 4:
        print ("El total de prestamos realizados durante la sesion es: ", historial_prestamos)
        print ("Préstamos activos actualmente:", libros_reservados)

#Saliendo del programa
    elif opcion == 5:
        print ("Gracias por utilizar nuestro software, hasta la próxima.")
        break

#Opcion erronea
    else:
        print ("¡Error! opcion invalida")
