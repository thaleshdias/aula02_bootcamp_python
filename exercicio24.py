#Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else 
# para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

try:
    numero = int(input("Digite um número: "))

    if numero == 0:
        print("O número informado é zero. Consequentemente é um número par.")
    elif numero < 0 and numero % 2 == 0:
        print(f"O número {numero} é negativo e par.")
    elif numero < 0 and numero % 2 != 0:    
        print(f"O número {numero} é negativo e impar.")
    elif numero > 0 and numero % 2 == 0:        
        print(f"O número {numero} é positivo e par.")
    else:
        print(f"O número {numero} é positivo e impar.")
except ValueError:
    print("O valor informado não é um número.")