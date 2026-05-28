def exercicio_43():
    numero = 30
    
    while numero >= 1:
        if numero % 4 == 0:
            print([numero], end = ' ')
        
        else:
            print(numero, end = ' ')
            
        numero = numero - 1