peliculas = ["El planeta de los simios nuevo reino", "Godzilla y Kong el nuevo imperio", "Deadpool y Wolverine"]
precios = {"2D": 3500, "3D": 5000}

while True:
    tipo_sala = input("Ingrese el tipo de sala (2D o 3D): ")
    cantidad_entradas = int(input("Ingrese la cantidad de entradas: "))

    costo_total = precios[tipo_sala] * cantidad_entradas
    descuento = costo_total * 0.1 if cantidad_entradas >= 3 else 0
    monto_final = costo_total - descuento

    print(f"\nCosto total: ${costo_total}")
    print(f"Descuento aplicado: ${descuento}")
    print(f"Monto final a pagar: ${monto_final}\n")

    nueva_compra = input("¿Desea procesar una nueva compra? (s/n): ")
    if nueva_compra.lower() != "s":
        break

peliculas = ["El planeta de los simios nuevo reino", "Godzilla y Kong el nuevo imperio", "Deadpool y Wolverine"]
precios = {"2D": 3500, "3D": 5000}
entradas_vendidas = {"2D": 0, "3D": 0}
continuar_comprando = True

while continuar_comprando:
    print("Películas disponibles:")
    for i, pelicula in enumerate(peliculas, start=1):
        print(f"{i}. {pelicula}")

    pelicula_elegida = int(input("Ingrese el número de la película deseada: "))
    tipo_sala = input("¿Desea 2D o 3D? ")
    cantidad_entradas = int(input("Ingrese la cantidad de entradas: "))

    if tipo_sala in precios:
        entradas_vendidas[tipo_sala] += cantidad_entradas
    else:
        print("Tipo de sala no válido.")

total_sin_descuento_2D = entradas_vendidas["2D"] * precios["2D"]
total_sin_descuento_3D = entradas_vendidas["3D"] * precios["3D"]
total_sin_descuento = total_sin_descuento_2D + total_sin_descuento_3D

if entradas_vendidas["2D"] + entradas_vendidas["3D"] >= 3:
    descuento = total_sin_descuento * 0.1
else:
    descuento = 0

total_con_descuento = total_sin_descuento - descuento

print(f"costo total {total_sin_descuento}")
print(f"Descuento aplicado {descuento}")
print(f"monto final a pagar {total_con_descuento}")

continuar = input("¿Desea procesar otra compra? (s/n): ")
if continuar.lower() != "s":
    continuar_comprando = False

print("\nReporte final:")
print(f"Entradas vendidas en sala 2D: {entradas_vendidas['2D']}")
print(f"Entradas vendidas en sala 3D: {entradas_vendidas['3D']}")
print(f"Total sin descuento: ${total_sin_descuento}")
print(f"Descuento aplicado: ${descuento}")
print(f"Monto final a pagar: ${total_con_descuento}")

