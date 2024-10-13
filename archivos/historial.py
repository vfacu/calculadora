from utiles.funcionales import obtener_fecha


FILE_NAME = 'historial.txt'

def guardar_operacion(operacion) -> None:
    with open(FILE_NAME, 'a') as file:
        file.write(f'{obtener_fecha()} - {operacion}\n')


def mostrar_historial():
    print("\nHistorial de operaciones:")
    with open(FILE_NAME, 'r') as file:
        for line in file:
            print(line, end='')
