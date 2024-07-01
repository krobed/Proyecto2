def format_text(text:str, maxwidth:int, file_name= '') -> List:
    ''' Este código recibe un string y un int para luego correr un algoritmo
        que se encarga de agrupar fragmentos del texto en una lista,
        dependiendo del valor de maxwidth. Retorna la lista.
    '''
    if file_name== '':
        file_name=input('Nombre del archivo: ')
    n=len(text)
	result = 0
	len_mat = np.zeros(n) 
	currRow = 0
    for j in range(n) :       
        if j==0 : 
            len_mat[currRow] = 0
            strings.append(text[j])
        
        elif (text[j - 1] != ' ') :	
            len_mat[currRow] = len_mat[currRow] + 1
            result = max(result, len_mat[currRow])
        else : 
            currRow+=1
            len_mat[currRow] = 0 
    
    

        

















