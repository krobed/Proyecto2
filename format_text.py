def format_text(text:str, maxwidth:int, file_name= '') -> List:
    ''' Este código recibe un string y un int para luego correr un algoritmo
        que se encarga de agrupar fragmentos del texto en una lista,
        dependiendo del valor de maxwidth. Retorna la lista.
    '''
    if file_name== '':
        file_name=input('Nombre del archivo: ')
    
    
