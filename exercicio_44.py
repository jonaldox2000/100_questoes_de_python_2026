def exercicio_44():
    inicial = int(input('Digite o primeiro valor:'))
    final = int(input('Digite o último valor:'))
    incremento = int(input('Digite o incremento:'))
    
    print('Contagem:' , end=' ')
    
    while inicial <= final:
        print(inicial, end=' ')
        inicial = inicial + incremento
