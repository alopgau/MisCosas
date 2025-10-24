import sys
def comprobarargs():
    """Función que comprueba si falta/n algun/os argumento/s"""
    if len(sys.argv) == 1:
        print("Faltan los dos operandos. Uso: calculadorabinario.py <operador1> <operador2> [operacion]")
        sys.exit()
    elif len(sys.argv) == 2:
        print("Falta uno de los operandos. Uso: calculadorabinario.py <operador1> <operador2> [operacion]")
        sys.exit()

def comprobarceroyuno(binario):
    """Función que comprueba si todos los digitos de los binarios son 0 o 1"""
    contador = 0
    for digito in binario:

        if digito != "1" and digito != "0":

            contador += 1

            if contador == 0:
                return True
            else:
                return False


        
def comprobarbinarios(binario1, binario2) -> list:
    """Función que termina de validar el formato de los binarios e informa al usuario si encuentra algún error"""

    if (binario2.isdigit() == False or len(binario2) > 8 or comprobarceroyuno(binario2) == False) and (binario1.isdigit() == False or len(binario1) > 8 or comprobarceroyuno(binario1) == False):

        print("El formato de ambos números es incorrecto. Por favor, vuelve a introducirlos.(Deben ser binario y de 8 dígitos como máximo):\n")
        sys.exit()

    elif binario1.isdigit() == False or len(binario1) > 8 or comprobarceroyuno(binario1) == False:

        print("El formato del primer número es incorrecto. Por favor, vuelve a introducirlo. (Debe ser binario y de 8 dígitos como máximo):\n")
        sys.exit()

    elif binario2.isdigit() == False or len(binario2) > 8 or comprobarceroyuno(binario2) == False:

        print("El formato del segundo número es incorrecto. Por favor, vuelve a introducirlo. (Debe ser binario y de 8 dígitos como máximo):\n")
        sys.exit()

 
    return [binario1, binario2]

def operacion(bin1,bin2):
    """Función que elige la operación"""
    if len(sys.argv) < 4:
        suma(bin1, bin2)
        print("\n")
        resta(bin1, bin2)
    else:
            op = sys.argv[3]

            if op.lower() == "+":

                suma(bin1, bin2)

            elif op.lower() == "-":

                resta(bin1,bin2)
            else:
                print("Introduce una operación válida , o ninguna para realizar ambas (suma y resta, usando sus respectivos símbolos)")

def suma(binario1, binario2) -> None:
    """Función que hace la suma de los dos operandos"""
    resultado = []
    acarreo = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range (len(binario1)-1,-1,-1):

        suma = int(binario1[i]) + int(binario2[i]) + int(acarreo[i+1])

        if suma == 0:
            resultado.append("0")

        elif suma == 1:
            resultado.append("1")

        elif suma == 2:
            resultado.append("0")
            acarreo[i] = 1

        elif suma == 3:
            resultado.append("1")
            acarreo[i] = 1

    if acarreo[0] == 1:
        resultado.append("1")

    
    resultado.reverse()


    print("".join(binario1))
    print("+")
    print("".join(binario2))
    print("---------")
    print("".join(resultado))

def resta(binario1, binario2) -> None:
    """Función que hace la resta de los dos operandos"""
    resultado = []
    acarreo = [0,0,0,0,0,0,0,0,0]
    for i in range (len(binario1)-1,-1,-1):

        resta = int(binario1[i])-int(binario2[i])+(acarreo[i+1])
        if resta == 1:
            resultado.append("1")

        elif resta == 0:
            resultado.append("0")

        elif resta == -1:
            resultado.append("1")
            acarreo[i] = -1
        elif resta == -2:
            resultado.append("0")
            acarreo[i] = -1

    resultado.reverse()
    print("".join(binario1))
    print("-")
    print("".join(binario2))
    print("--------")
    print("".join(resultado).zfill(8))
    if acarreo[0] == -1:
        print("(El resultado es negativo, genera desbordamiento)")



def main():
    comprobarargs()
    bin1 = sys.argv[1].zfill(8)
    bin2 = sys.argv[2].zfill(8)

    
    binarios_check = comprobarbinarios(bin1, bin2)
    bin1 = binarios_check[0]
    bin2 = binarios_check[1]

    lista_bin1 = list(bin1)
    lista_bin2 = list(bin2)

    operacion(lista_bin1,lista_bin2)

        
if __name__== "__main__":
    main()