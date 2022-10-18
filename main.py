def potencia(num1, num2):
    if num2 == 0:
        return 1
    return (num1 * potencia(num1, num2 - 1))

def potencia2(num1,num2):
    pot = 1
    for i in range(num2):
        pot = pot * num1

    resultado = pot
    return resultado




def ejemplo1():
    while True:
        try:
            num1 = int(input("ingrese el primer numero\n"))
            num2 = int(input("ingrese el segundo numero\n"))
            break
        except ValueError:
            print("debe ingrese un numero\n")
            continue

    operador = input('Ingrese el operador: ')
    while operador not in ('+', '-', '*', '/', '**','***'):
        print('Ingresa un operador válido')
        operador = input('Ingrese el operador: ')

    if (operador == '+'):
        resultado = num1 + num2
    elif (operador == '-'):
        resultado = num1 - num2
    elif (operador == '*'):
        resultado = num1 * num2
    elif (operador == '/'):
        resultado = num1 // num2
    elif (operador == '**'):

        resultado =potencia(num1,num2)
    elif (operador == '***'):
        resultado=potencia2(num1,num2)

    print('el resultado es: ', resultado)
    #potencia(num1,num2)


ejemplo1()