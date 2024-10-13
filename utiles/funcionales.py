from datetime import datetime


def obtener_fecha():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    