def exercicio_45():
    inicial = int(input('Digite o primeiro valor:'))
    final = int(input('Digite o último valor:'))
    incremento = int(input('Digite o incremento:'))
    
    print('Contagem:' , end=' ')
    
    if final > inicial:
        while inicial <= final:
            print(inicial, end=' ')
            inicial = inicial + incremento
        
    else:
        while inicial >= final:
            print(inicial, end=' ')
            inicial = inicial - incremento
        