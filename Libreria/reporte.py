def reportar(historial, resumen, nombres):
    print("\n======= REPORTE GENERAL =======")
    print(f"Total de Estudiantes Procesados: {resumen['total']}")  #DICCIONARIO
    print(f"Estudiantes con promedio alto (≥17): {resumen['altos']}")  #DICCIONARIO
    print(f"Estudiantes con promedio medio (13 a 16): {resumen['medios']}")  #DICCIONARIO
    print(f"Estudiantes con promedio bajo (<13): {resumen['bajos']}")  #DICCIONARIO
    print(f"Suma total de promedios finales: {round(resumen['suma_promedios'], 2)}")

    if resumen['total'] > 0:
        promedio_grupal = resumen['suma_promedios'] / resumen['total']
        print(f"Promedio general del grupo: {round(promedio_grupal, 2)}")

    print("\n======= INFORME DETALLADO DE LOS ESTUDIANTES =======")
    for est in historial:
        nombre, promedio, bono, final, lista_cursos = est
        print(f"\n- {nombre} - Prom: {round(promedio, 2)} | Bono: {bono} | Final: {round(final, 2)}")
        for curso, nota in lista_cursos:
            print(f"   - {curso}: {nota}")

    print("\n======= NOMBRES DE ESTUDIANTE INGRESADOS =======")
    for i, nombre in enumerate(nombres, start=1):  #CONJUNTO
        print(f"{i}. {nombre}")
