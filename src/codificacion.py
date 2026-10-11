alf = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ" 
def letra_a_posicion(letra: str) -> int:
    '''Devuelve la posición de la letra en el abecedario
    
    Parámetros
    - letra(str): letra que se convierte en número
    
    Devuelve:
    (int) La posición de la letra en el alfabeto'''
    posicion = 0
    if letra in alf:
        posicion = alf.find(letra)
        return posicion
    else: 
        return None


def posicion_a_letra(posicion: int) -> str:
    
    '''A partir de una posicion, devuelve la letra que representa dicha posición
    en el alfabeto
    
    Parametros:
    - posicion(int): posicion que hay que transformar en letra
    
    Devuelve:
    (str) La letra que correpsonde en el abecedario respecto a la posición inicial'''

    letra = ""
    if 0 <= posicion < len(alf):
        letra = alf[posicion]
        return letra
    else:
        return None

def cifra_cesar(cadena: str, clave: int) -> str:
    res = ""
    posicion = 0
    for i in cadena:
        if i.isalpha():
            posicion = letra_a_posicion(i)
            posicion_clave = (posicion + clave) % len(alf)
            letra_nueva = posicion_a_letra(posicion_clave)
            res += letra_nueva
        else:
            res += i
    return res


def rompe_cesar(mensaje_cifrado: str) -> str:
    for i in range(len(alf)):
        print(i, cifra_cesar(mensaje_cifrado, -i))


print(rompe_cesar("j YÁXOÁJUJÁ ÉN JYÁNVMN yáxoájujvmx!"))

