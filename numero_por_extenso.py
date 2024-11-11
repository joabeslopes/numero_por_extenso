tab_numeros = {
    1: 'UM',
    2: 'DOIS',
    3: 'TRÊS',
    4: 'QUATRO',
    5: 'CINCO',
    6: 'SEIS',
    7: 'SETE',
    8: 'OITO',
    9: 'NOVE',
    10: 'DEZ',
    20: 'VINTE',
    30: 'TRINTA',
    40: 'QUARENTA',
    50: 'CINQUENTA',
    60: 'SESSENTA',
    70: 'SETENTA',
    80: 'OITENTA',
    90: 'NOVENTA',
    100: 'CENTO',
    200: 'DUZENTOS',
    300: 'TREZENTOS',
    400: 'QUATROCENTOS',
    500: 'QUINHENTOS',
    600: 'SEISSENTOS',
    700: 'SETESSENTOS',
    800: 'OITOSSENTOS',
    900: 'NOVECENTOS'
}


tab_excessoes = {
    0: 'ZERO',
    11: 'ONZE',
    12: 'DOZE',
    13: 'TREZE',
    14: 'QUATORZE',
    15: 'QUINZE',
    16: 'DEZESSEIS',
    17: 'DEZESSETE',
    18: 'DEZOITO',
    19: 'DEZENOVE',
    100: 'CEM'
}


def pequeno_filtro(num, divisor=100):
    if num in tab_excessoes:
        return tab_excessoes[num]
    else:
        quociente = num // divisor
        resto = num % divisor

        if quociente > 0 and resto > 0:
            return tab_numeros[quociente * divisor] + ' E ' + pequeno_filtro(resto, divisor//10)

        elif quociente == 0 and resto > 0:
            return pequeno_filtro(resto, divisor//10)

        elif quociente > 0 and resto == 0:
            return tab_numeros[quociente * divisor]


def grande_filtro(num, divisor=1000000000):
    if num == 0:
        return tab_excessoes[num]

    elif num >= 1000000000000 or num < 0 or not isinstance(num, int):
        return 'Erro: O parâmetro deve ser um número inteiro entre 0 e 1 trilhão'
        
    else:
        quociente = num // divisor
        resto = num % divisor
        multi = ''

        if divisor == 1000000000:
            multi = ' BILHÃO '
            if quociente > 1:
                multi = ' BILHÕES '
        elif divisor == 1000000:
            multi = ' MILHÃO '
            if quociente > 1:
                multi = ' MILHÕES '
        elif divisor == 1000:
            multi = ' MIL '
            if (resto > 0) and (resto < 100 or resto % 100 == 0):
                multi = ' MIL E '

        if quociente > 0 and resto > 0:
            return pequeno_filtro(quociente) + multi + grande_filtro(resto, divisor//1000)

        elif quociente == 0 and resto > 0:
            return grande_filtro(resto, divisor//1000)

        elif quociente > 0 and resto == 0:
            return pequeno_filtro(quociente) + multi


result = grande_filtro(1900)
print( result )