#Ejercicio 1 prueba parcial 3

#Contadores
especialistas_senior = 0
residentes_junior    = 0

#Registrando cantidad de medicos
while True:
    try:
        cantidad_medicos = int(input("¡Bienvenido al sistema! Por favor, ingrese la cantidad de medicos que desea registrar: "))
        if cantidad_medicos <= 0:
            print ("¡Registro médico inválido! Ingresa un entero positivo para continuar")
        else:
            print ("Se han agregado", cantidad_medicos, "medicos")
            break
    except ValueError:
        print ("¡Registro médico inválido! Ingresa un entero positivo para continuar")

#Registro por medico
for i in range(cantidad_medicos):
    print ("Ingresando al medico", (i+1))
    while True:
        nombre = input("Ingrese el nombre del profesional (min. 6 caracteres, sin espacio): ").strip()
        if len(nombre) >=6 and " " not in nombre:
            print ("Nombre profesional valido")
            break
        else:
            print ("¡Nombre profesional incorrecto! su nombre debe tener al menos 6 letras y no tener espacios")

#Experiencia clinica
    while True:
        try:
            experiencia_clinica = int(input("Por favor, ingresar los años de experiencia del médico: "))
            if experiencia_clinica <= 0:
                print ("¡Error clínico! Ingresa un número entero positivo para la experiencia.")
            else:
                break
        except ValueError:
            print ("¡Error clínico! Ingresa un número entero positivo para la experiencia")

#Clasificacion del medico
    if experiencia_clinica >5:
        especialistas_senior +=1
    elif experiencia_clinica <=5:
        residentes_junior +=1

#Salida final
print ("¡El hospital cuenta con", especialistas_senior, "Especialistas Senior y", residentes_junior, "Residentes Junior! ¡Sistema listo para operar!")