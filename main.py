import display.menu as menu
from operaciones.basicas import suma, resta, multiplicacion, division
from archivos.historial import guardar_operacion, mostrar_historial
from utiles.funcionales import pedir_numero


def main():
    operaciones_validas = ['+', '-', '*', '/', 'h', '0'] 
    menu.clear()
    choice = '1'    

    while True:
        try:
            choice = input('Ingrese la operación (+, -, *, /, h(historial)) o "0" para salir:  ')

            if choice == "h":
                mostrar_historial()
                continue 

            if choice == "0":
                print("Salir")
                break
            
            if choice not in operaciones_validas:
                raise Exception('Opción inválida, vuelva a intentarlo')  

            num1 = pedir_numero("Ingrese un numero: ") 
            num2 = pedir_numero("Ingrese el segundo numero: ")

            if choice == '+':
                resultado = suma(num1, num2)
                operacion = f"{num1} + {num2} = {resultado}"
                guardar_operacion(operacion)    
                print("La suma es:", operacion)         
            
            elif choice == '-':
                resultado = resta(num1, num2)
                operacion = f"{num1} - {num2} = {resultado}"
                guardar_operacion(operacion)
                print("La resta es:", operacion)
            
            elif choice == '*':
                resultado = multiplicacion(num1, num2)
                operacion = f"{num1} * {num2} = {resultado}"
                guardar_operacion(operacion)
                print("La multiplicación es:", operacion)
            
            elif choice == '/':
                if num2 == 0:
                    raise ZeroDivisionError("No se puede dividir por 0")                
                resultado = division(num1, num2)
                operacion = f"{num1} / {num2} = {resultado}"
                print("La división es:", operacion)                               
               
        except ZeroDivisionError as error:
            print('Error: ', error)
        except Exception as error:
            print(error)


if __name__ == "__main__":
    main()
