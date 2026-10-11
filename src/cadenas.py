def invierte_cadena(cadena: str) -> str:
    '''Invierte la cadena que recibe por el parámetro
    
    Parámetros:
    - cadena (str): el texto que hay que invertir
    
    Devuelve:
    (str) Es el texto invertido
    '''
    res = ""
    for i in cadena:
        res = i + res
    return res 

def es_palindromo(cadena: str, ignora_espacios: bool = False, ignora_mayusculas: bool = True) -> bool:
    '''Recibe una cadena, la invierte y comprueba si la cadena invertida
    es igual a la original, es decir devuelve True si son 
    palíndromos
    
    Parámetros:
    - cadena(str): el texto que hay que invertir y comprobar si es paalíndromos
    - ignora_espacios(bool): ignora los espacios en la cadena
    - ignora_mayusculas(bool): ignora las mayusculas en la cadena
    
    Devuelve:
    (bool) True si es palindromo'''

    if ignora_espacios:
        cadena = cadena.replace(" ", "")
    if ignora_mayusculas:
        cadena = cadena.lower()

    res = ""
    for i in cadena:
        res = i + res

    return cadena == res

def estiliza_mensaje(cadena: str, alterna_may_min: bool = True, usa_dieresis: bool = False, sustituye_espacios: bool = False) -> str:
    ''' Recibe una cadena y permite obtener otra con algunos cambios estéticos
    
    Parámetros:
    - cadena(str): recibe una cadena
    - alterna_may_min(bool): hace que en la cadena se inviertan las mayuculas con las minúsculas
    - usa_dieresis(bool): añade dieresis a las vocales que no incluyan tildes
    - sustituye_espacios(bool): cambia los espacios por "*"
    
    Devuelve:
    (str) La cadena con los cambios estéticos'''
    res = ""
    toca_mayus = True
    for i in cadena:
        if alterna_may_min:
            if i.isalpha():
                if toca_mayus:
                    i = i.upper()
                    toca_mayus = False
                else: 
                    i = i.lower()
                    toca_mayus = True
            
            res += i
        else:
            res = cadena

        if usa_dieresis:
            res = res.replace("a", "ä").replace("A", "Ä").replace("E", "Ë").replace("e", "ë").replace("i", "ï").replace("I", "Ï").replace("O", "Ö").replace("o", "ö").replace("u", "ü").replace("U", "Ü")

        if sustituye_espacios:
            res = res.replace(" ", "*")

    return res


