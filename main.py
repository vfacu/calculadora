import display
from operaciones import suma, resta, multiplicacion, division
from historial import mostrar_historial

def main():
    historial = []
    display.clear()
    choice = '1'    
    while True: 
        choice = input('Ingrese la operación (+, -, *, /, h(historial)) o "0" para salir:  ')

        if choice == "h":
            mostrar_historial(historial)
            continue 

        if choice == "0":
            print("Salir")
            break

        num1 = float(input("Ingrese un numero: "))  
        num2 = float(input("Ingrese el segundo numero: "))  

        if choice == '+':
            resultado = suma(num1, num2)
            operacion = f"{num1} + {num2} = {resultado}"
            historial.append(operacion) 
            print("La suma es:", operacion)
        elif choice == '-':
            resultado = resta(num1, num2)
            operacion = f"{num1} - {num2} = {resultado}"
            historial.append(operacion) 
            print("La resta es:", operacion)
        elif choice == '*':
            resultado = multiplicacion(num1, num2)
            operacion = f"{num1} * {num2} = {resultado}"
            historial.append(operacion) 
            print("La multiplicación es:", operacion)
        elif choice == '/':
            if num2 != 0:  
                resultado = division(num1, num2)
                operacion = f"{num1} / {num2} = {resultado}"
                historial.append(operacion) 
                print("La división es:", operacion)
            else:
                print("Error: No se puede dividir entre cero.")      
        elif choice == "0":            
            print('Salir')
            break        
        else:
            print('Opción inválida, vuelva a intentarlo')  

             
if __name__ == "__main__":
    main()
