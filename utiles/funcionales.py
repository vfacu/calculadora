from datetime import datetime


def obtener_fecha():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def pedir_numero(mje):
    valor = input(mje)
    try:
        return float(valor)
    except ValueError:
        print("Por favor ingrese un numero válido")
        return pedir_numero(mje)
