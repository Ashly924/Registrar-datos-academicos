def leer_entero(mensaje, minimo=None, maximo=None):
    valor = int(input(mensaje))
    return valor

def leer_texto(mensaje):
    texto = input(mensaje).strip()
    return texto

def confirmar_continuar(mensaje="¿Desea continuar? (S/N): "):
    rpta = input(mensaje).strip().upper()
    if rpta == "S":
        return True
    else:
        return False

def confirmar_salida():
    respuesta = input("¿Desea salir del programa? (S/N): ").upper()
    salida = False
    if respuesta == "S":
        salida = True
    if respuesta == "N":
        salida = False
    return salida

def menu_opcion():
    return int(input("Ingrese opción de menú:\t"))
