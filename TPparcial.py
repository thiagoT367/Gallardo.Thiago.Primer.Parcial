# Lista de nombres de usuarios VIP
usuarios = [
    "Lunatico_pixel", "Sombra_cristal", "Ecoerrante", "Navefantasma", "Bytesdelabahia",
    "Tintaenelviento", "Relojoxidado", "Miradacodificada", "Circuitoazul", "Fuego_niebla",
    "Teclaerrante", "Nebulosa_urbana", "Sueño_binario", "Saltofantasma", "Claveoculta"
]

# Lista de empresas a las cuales invertir
acciones = ["APPLE", "TESLA", "NVIDIA"]

# Precios de cada acción en el mismo orden
precios = [10.41, 7.71, 8.50]

# Matriz para guardar cuántas acciones compró cada usuario por empresa
inversiones = [[0, 0, 0] for _ in range(15)]

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Registrar una transacción")
    print("2. Ver matriz de inversiones")
    print("3. 📊 Consultas estadísticas")
    print("0. Salir")

def registrar_transaccion():
    print("\n--- Registrar una transacción ---")
    nombre_usuario = input("Ingrese el nombre del usuario (ej: Lunatico_pixel): ")
    if nombre_usuario not in usuarios:
        print("❌ Usuario no válido.")
        return
    nombre_accion = input("Ingrese el nombre de la acción (APPLE, TESLA o NVIDIA): ")
    if nombre_accion not in acciones:
        print("❌ Acción no válida.")
        return
    cantidad_str = input("Ingrese la cantidad de acciones (0 a 500): ")
    if not cantidad_str.isdigit():
        print("❌ Debe ingresar un número entero.")
        return
    cantidad = int(cantidad_str)
    if cantidad < 0 or cantidad > 500:
        print("❌ La cantidad debe estar entre 0 y 500.")
        return
    i = usuarios.index(nombre_usuario)
    j = acciones.index(nombre_accion)
    inversiones[i][j] += cantidad
    total_invertido = cantidad * precios[j]
    print("✅ Transacción registrada.")
    print("💰 Total invertido en USD: $", str(int(total_invertido * 100) / 100))

def ver_matriz():
    print("\n📊 Estado actual de inversiones:\n")
    print("Usuario\t\t\tAPPLE\tTESLA\tNVIDIA")
    print("-----------------------------------------------")
    for i in range(15):
        print(usuarios[i] + "\t" +
              str(inversiones[i][0]) + "\t" +
              str(inversiones[i][1]) + "\t" +
              str(inversiones[i][2]))

def consultas_estadisticas():
    while True:
        print("\n=== SUBMENÚ DE CONSULTAS ===")
        print("1. 🔢 Total de acciones por usuario")
        print("2. 📈 Promedio de acciones por empresa")
        print("3. 🔁 Usuarios Z-A con total invertido")
        print("4. 💵 Inversión total acumulada")
        print("5. 🥇 Empresa más comprada por usuario")
        print("6. 💰 Acción con mayor inversión total")
        print("7. 📉 Porcentaje de inversión por usuario")
        print("8. 🤑 Usuarios con inversión sobre el promedio")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for i in range(15):
                total = inversiones[i][0] + inversiones[i][1] + inversiones[i][2]
                print(usuarios[i], "→", total, "acciones")

        elif opcion == "2":
            for j in range(3):
                suma = 0
                for i in range(15):
                    suma += inversiones[i][j]
                promedio = suma / 15
                print(acciones[j], "→ Promedio:", int(promedio * 100) / 100, "acciones")

        elif opcion == "3":
            copia_nombres = list(usuarios)
            for i in range(14):
                for j in range(i + 1, 15):
                    if copia_nombres[i] < copia_nombres[j]:
                        copia_nombres[i], copia_nombres[j] = copia_nombres[j], copia_nombres[i]
            for nombre in copia_nombres:
                i = usuarios.index(nombre)
                total = inversiones[i][0] * precios[0] + inversiones[i][1] * precios[1] + inversiones[i][2] * precios[2]
                print(nombre, "→ $", int(total * 100) / 100)

        elif opcion == "4":
            total = 0
            for i in range(15):
                total += inversiones[i][0] * precios[0]
                total += inversiones[i][1] * precios[1]
                total += inversiones[i][2] * precios[2]
            print("💵 Inversión total acumulada: $", int(total * 100) / 100)

        elif opcion == "5":
            for i in range(15):
                mayor = inversiones[i][0]
                posicion = 0
                if inversiones[i][1] > mayor:
                    mayor = inversiones[i][1]
                    posicion = 1
                if inversiones[i][2] > mayor:
                    posicion = 2
                print(usuarios[i], "→ Más compró:", acciones[posicion])

        elif opcion == "6":
            total_apple = 0
            total_tesla = 0
            total_nvidia = 0
            for i in range(15):
                total_apple += inversiones[i][0] * precios[0]
                total_tesla += inversiones[i][1] * precios[1]
                total_nvidia += inversiones[i][2] * precios[2]
            if total_apple >= total_tesla and total_apple >= total_nvidia:
                print("💰 Acción con mayor inversión total: APPLE")
            elif total_tesla >= total_apple and total_tesla >= total_nvidia:
                print("💰 Acción con mayor inversión total: TESLA")
            else:
                print("💰 Acción con mayor inversión total: NVIDIA")

        elif opcion == "7":
            total_global = 0
            for i in range(15):
                for j in range(3):
                    total_global += inversiones[i][j] * precios[j]
            for i in range(15):
                total_usuario = 0
                for j in range(3):
                    total_usuario += inversiones[i][j] * precios[j]
                if total_global > 0:
                    porcentaje = total_usuario * 100 / total_global
                else:
                    porcentaje = 0
                print(usuarios[i], "→", int(porcentaje * 100) / 100, "%")

        elif opcion == "8":
            suma_total = 0
            totales = [0] * 15
            for i in range(15):
                for j in range(3):
                    totales[i] += inversiones[i][j] * precios[j]
                suma_total += totales[i]
            promedio = suma_total / 15
            for i in range(15):
                if totales[i] > promedio:
                    print(usuarios[i], "→ $", int(totales[i] * 100) / 100)

        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida.")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_transaccion()
    elif opcion == "2":
        ver_matriz()
    elif opcion == "3":
        consultas_estadisticas()
    elif opcion == "0":
        print("👋 Programa finalizado.")
        break
    else:
        print("❌ Opción inválida.")
