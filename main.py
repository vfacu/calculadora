import display

def main():
    historial = []
    display.clear()
    choice = '1'    
    while True:      
        choice = input("Ingrese 'h' si quiere ver el Historial, sino presiones Inter para seguir ") 
        if choice == "h":
            print("\nHistorial de operaciones:")
            for operacion in historial:
                print(operacion)
            print()  # Línea en blanco para mejor formato  
            break
        else:
            choice = input('Ingrese la operación (+, -, *, /, h(historial)) o "0" para salir:  ')
            num1 = float(input("Ingrese un numero: "))  
            num2 = float(input("Ingrese el segundo numero: "))            
        
            if choice == '+':
                resultado = num1 + num2
                operacion = f"{num1} + {num2} = {resultado}"
                historial.append(operacion) 
                print("La suma es:", operacion)
            elif choice == '-':
                resultado = num1 - num2
                operacion = f"{num1} - {num2} = {resultado}"
                historial.append(operacion)  # Guardar en historial
                print("La resta es:", operacion)
            elif choice == '*':
                resultado = num1 * num2
                operacion = f"{num1} * {num2} = {resultado}"
                historial.append(operacion)  # Guardar en historial
                print("La multiplicación es:", operacion)
            elif choice == '/':
                if num2 != 0:  # Asegúrate de no dividir entre cero
                    resultado = num1 / num2
                    operacion = f"{num1} / {num2} = {resultado}"
                    historial.append(operacion)  # Guardar en historial
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
