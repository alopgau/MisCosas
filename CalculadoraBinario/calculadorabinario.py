import sys
def comprobarargs():
    if len(sys.argv) == 1:
        print("Faltan los dos operandos y la operación. Uso: calculadorabinario.py <operador1> <operador2> [operacion]")
        sys.exit()
    elif len(sys.argv) == 2:
        print("Falta uno de los operandos y la operación. Uso: calculadorabinario.py <operador1> <operador2> [operacion]")
        sys.exit()
def pedirnumero(mensaje):
        return input(mensaje)

def comprobarceroyuno(binario):
    contador = 0
    for digito in binario:

        if digito != "1" and digito != "0":

            contador += 1

            if contador == 0:
                return True
            else:
                return False


        
def comprobarbinarios(binario1, binario2) -> list:

    while binario1.isdigit() == False or len(binario1) != 8 or comprobarceroyuno(binario1) == False or binario2.isdigit() == False or len(binario2) != 8 or comprobarceroyuno(binario2) == False:

        if binario1.isdigit() == False or len(binario1) != 8 or comprobarceroyuno(binario1) == False:
            
            binario1 = pedirnumero("El formato del primer número es incorrecto. Por favor, vuelve a introducirlo. (Debe ser binario y de 8 dígitos):\n")

            
        elif binario2.isdigit() == False or len(binario2) != 8 or comprobarceroyuno(binario2) == False:
            
            binario2 = pedirnumero("El formato del segundo número es incorrecto. Por favor, vuelve a introducirlo.(debe ser binario y de 8 dígitos):\n")

 
    return [binario1, binario2]

def operacion(bin1,bin2):

    operacion_valida = False

    while operacion_valida is False:
        op = ""
        if len(sys.argv) == 5:
            op = sys.argv[3]

        elif op.lower() == ("+" or "suma" or "sumar"):
        
            operacion_valida = True
            suma(bin1, bin2)
        
        elif op.lower() == ("-" or "resta" or "restar"):
         
                operacion_valida = True
                resta(bin1,bin2)
        if op == "":
            operacion_valida = True
            suma(bin1, bin2)
            resta(bin1,bin2)

def suma(binario1, binario2) -> None:
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
    print("\n")

def resta(binario1, binario2) -> None:
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
    print("".join(resultado))
    if acarreo[0] == -1:
        print("(El resultado es negativo, genera desbordamiento)")



def main():
    comprobarargs()
    bin1 = sys.argv[1]
    bin2 = sys.argv[2]
    # bin1 = pedirnumero("Introduce el 1º número (debe ser binario y de 8 dígitos):\n")
    # bin2 = pedirnumero("Introduce el 2º número (debe ser binario y de 8 dígitos):\n")
    
    binarios_check = comprobarbinarios(bin1, bin2)
    bin1 = binarios_check[0]
    bin2 = binarios_check[1]

    lista_bin1 = list(bin1)
    lista_bin2 = list(bin2)

    operacion(lista_bin1,lista_bin2)

        
if __name__== "__main__":
    main()