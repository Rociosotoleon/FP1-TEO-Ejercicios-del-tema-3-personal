def invierte_numero(numero_entero: int) -> int:
    '''La función recibe un número entero y devuelve el número resultante 
    al invertir sus dígitos
    
    Parámetros:
    - numero_entero(int) -> número que hay que invertir
    
    Devolución:
    (int) Número resultante al invertir las cifras del original'''

    res = 0 
    while numero_entero != 0:
        ultima_cifra = numero_entero % 10
        numero_entero = numero_entero // 10
        res = res * 10 + ultima_cifra

    return res

def convierte_binario(numero: int) -> int:
    '''La función recibe un número entero decimal, de base 10 y devuelve su conversión a
    binario, base 2 '''
    if numero == 0:
        return "0" 
    
    res = ""
    while numero > 0:
        resto = str(numero % 2)
        numero //= 2
        res = resto + res


    return res 

print(convierte_binario(0))