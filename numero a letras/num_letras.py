import math

def numPalabras(num):
    # Los primeros 15. acá no se sigue ningún patrón ==========================*/
    primeros15 = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco',
                'seis', 'siete', 'ocho', 'nueve', 'diez', 'once',
                'doce', 'trece', 'catorce', 'quince']

    if (num <= 15):
        return primeros15[num]
    
    elif (num <= 19):
        unidades = num - 10
        return 'dieci' + numPalabras(unidades)

    elif num == 20: 
        return 'veinte'

    elif num <= 29:         # Estos son los veinti "algo"
        unidades = num - 20
        return 'veinti' + numPalabras(unidades)

    #  Estos van desde el 30 al 100 
    elif num <= 100:      
        decenas = num / 10
        decenas = math.floor(decenas)
    
        unidades = num - (decenas * 10)

        nombreDecenas = ['treinta', 'cuarenta', 'cincuenta',
                        'sesenta', 'setenta', 'ochenta', 'noventa', 'cien']

        if unidades == 0:
            return nombreDecenas[decenas - 3] 

        return nombreDecenas[decenas - 3] +' y ' +  numPalabras(unidades)

    #  Estos van del 101, 999
    elif num <= 1000:
        centenas = num / 100
        centenas = math.floor(centenas)

        resto = num - (centenas * 100)

        nombreCentenas = ['ciento ', 'doscientos ', 'trescientos ', 'cuatrocientos ',
                        'quinientos ', 'seiscientos ', 'setecientos ', 'ochocientos ',
                        'novecientos ', 'mil ']

        if resto == 0:
            return nombreCentenas[centenas - 1]

        return nombreCentenas[centenas - 1] + numPalabras(resto)

    # Estos van desde el 1001 hasta el 1999
    elif num < 2000: 
        resto = num - 1000
        return 'mil ' + numPalabras(resto)

    #  Estos van desde el 2000 hasta el 999999
    elif num < 1000000: 
        miles = num / 1000
        miles = math.floor(miles)

        resto = num - (miles * 1000)

        if resto == 0:
            return numPalabras(miles) + ' mil '

        return numPalabras(miles) + ' mil ' + numPalabras(resto)

    #  Estos van desde el 1000000 hasta el 999999999999
    elif num < 1000000000000:
        if num == 1000000:
            return 'un millón '
        millon = math.floor(num / 1000000)
        resto2 = num - (millon * 1000000)
        # console.log('millón: '+ millon, 'resto2: '+resto2);
        if millon == 1:
            if millon != 1 and resto2 == 0:
                return numPalabras(millon) + ' millones '

            return 'un millón ' + numPalabras(resto2)

        return numPalabras(millon) + ' millones, ' + numPalabras(resto2);

    
    return "no implementado"

def iniciar():
    print("llegamos")
    while True:
        # solicitamos al usuario que ingrese un numero
        num = input("ingrese un número (o 'q' para salir): ")
        if num == 'q':
            break

        # transformar el valor a numero
        try:
            num = int(num)
        except ValueError:
            print("valor no válido")
            continue

        # transforma el numero a palabras
        palabras = numPalabras(num)

        # finalmente imprimimos el valor 
        print(palabras)

    print("gracias por participar")


if __name__ == "__main__":
    iniciar()

