def promedio_recursivo_guardado(n, i=1, lista=None):
    if lista is None:
        lista = []

    if i > n:
        return lista

    nombre_curso = input(f"Ingrese nombre del curso {i}:\t")
    nota = float(input(f"Ingrese nota para '{nombre_curso}':\t"))
    lista.append((nombre_curso, nota))

    return promedio_recursivo_guardado(n, i + 1, lista)
