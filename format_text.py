import word_wrap
import common_substring
import word_break



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
    file = open('archivo.txt', 'w')
    for i in dictionary:
        file.write(i+'\n')
    return dictionary





text = 'hoy es un día con mucho calor'
print(format_text(text, 6))
text= 'this is a programming problem which demonstrates dynamic programming'
print(format_text(text,15))

















