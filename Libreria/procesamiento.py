from Libreria.promedio import promedio_recursivo_guardado

def procesar(historial, resumen, nombres):
    while True:
        nombre = input("Ingrese nombre del estudiante:\t")
        cursos = int(input("Ingrese número de cursos:\t"))

        lista_cursos = promedio_recursivo_guardado(cursos)
        suma = sum(nota for _, nota in lista_cursos)
        promedio = suma / cursos

        bono = 1 if promedio >= 18 else 0.5 if promedio >= 16 else 0
        promedio_final = promedio + bono

        resumen["total"] += 1
        resumen["suma_promedios"] += promedio_final

        if promedio_final >= 17:
            resumen["altos"] += 1
        elif 13 <= promedio_final < 17:
            resumen["medios"] += 1
        else:
            resumen["bajos"] += 1

        nombres.add(nombre)  #CONJUNTO

        estudiante = (nombre, promedio, bono, promedio_final, lista_cursos)  #LISTA
        historial.append(estudiante)  #LISTA

        print("\n======= REPORTE DEL ESTUDIANTE =======")
        print(f"Nombre: {nombre}")
        print(f"Promedio: {round(promedio, 2)}")
        print(f"Bonificación: {bono}")
        print(f"Promedio Final: {round(promedio_final, 2)}")

        print("\n--- Detalle de cursos ---")
        for curso, nota in lista_cursos:
            print(f"{curso}: {nota}")

        continuar = input("\n¿Desea ingresar otro estudiante? (S/N): ").upper()
        if continuar != "S":
            break

