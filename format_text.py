import word_wrap
import common_substring
import word_break

def save_to_file(text: str,name:str) -> str:
    ''' Recibe dos string 'text' y 'name', los cuales corresponden a un texto y el nombre del archivo
        donde se guardará éste. Retorna 'file saved'.
    '''
    file = open(name,'w')
    for i in text:
        file.write(i+'\n')
    return 'file saved'

def identify(file, dictionary: list) -> [list,list,list]:
    ''' Recibe un archivo tipo texto 'file' y una lista 'dictionary', luego recorre las funciones
        estudiadas, common substring, word wrap y word break. Retorna los resultados de cada una.
    '''
    text = file.readlines()
    lcs = np.empty(shape(len(dictionary), len(text))
    size = np.empty(len(text))
    for i in range(len(dictionary)):
        for j in range(len(text)):
            size[j] = len[text[j]]
            lcs[i][j] = LCSubStr(dictionary[i],text[j])
    ww = solveWordWrap(size, len(size))

    wb = wordBreak(text,dictionary)
    return lcs,ww,wb

def format_text(text:str, maxwidth:int) -> list:
    ''' Este código recibe un string y un int para luego correr un algoritmo
        que se encarga de agrupar fragmentos del texto en una lista,
        dependiendo del valor de maxwidth. Retorna la lista y la ingresa a un archivo de texto llamado 'archivo'.
    '''
    
    text = text.split(' ')
    dictionary = [text[0]]
    for i in text[1:]:
        if len(i)+len(dictionary[-1])+1 <=maxwidth:
            dictionary[-1] = dictionary[-1] + ' '+ i
        else:
            dictionary.append(i)
    save_to_file(dictionary,'archivo.txt')
    return dictionary




# Pruebas
text = 'hoy es un día con mucho calor'
print(format_text(text, 6))
text= 'this is a programming problem which demonstrates dynamic programming'
print(format_text(text,15))

















