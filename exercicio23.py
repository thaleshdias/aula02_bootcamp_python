try:
    num01 = float(input("Digite o primeiro número: "))
    num02 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador: ") 
    
    if operador == "+":
        resultado = num01 + num02
        print(f"O resultado da operação de soma é: {resultado}")

    elif operador == "-":
        resultado = num01 - num02
        print(f"O resultado da operação de subtração é: {resultado}")

    elif operador == "*" or operador == "x":
        resultado = num01 * num02
        print(f"O resultado da operação de multiplicação é: {resultado}")

    elif operador == "/" and num02 != 0:
            resultado = num01 / num02
            print(f"O resultado da operação de divisão é: {resultado}")

    elif operador == "/" and num02 == 0:
            print("O calculo não pode ser realizado pois você informou zero no divisor")
    
    else:
         print("O operador informado não pode ser utilizado.")

except ValueError:
     print("O valor informado não se aplica.")


