from Libreria.procesamiento import procesar
from Libreria.reporte import reportar

def ejecutar():
    historial_estudiantes = []  #LISTA
    resumen = {  #DICCIONARIO
        "total": 0,
        "altos": 0,
        "bajos": 0,
        "medios": 0,
        "suma_promedios": 0
    }
    nombres_unicos = set()

    while True:
        print("\n========= MENÚ OPCIONES =========")
        print("1. Procesar Estudiante")
        print("2. Ver Reporte General")
        print("3. Salir")

        op = int(input("Ingrese opción de menú:\t"))

        if op == 1:
            procesar(historial_estudiantes, resumen, nombres_unicos)
        elif op == 2:
            reportar(historial_estudiantes, resumen, nombres_unicos)
        elif op == 3:
            rpta = input("¿Desea salir del programa? (S/N): ").upper()
            if rpta == "S":
                print("Hasta Pronto :D")
                break

ejecutar()
