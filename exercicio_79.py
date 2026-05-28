def exercicio_79():
    vetor = []
    
    for numero in range(10):
        num = int(input(f'Digite o {numero+1} número: '))
        vetor.append(num)
        
    print('   Pares encontrados   ')
    
    for numero in range(10):
        if vetor[numero] % 2 == 0:
            print('Numero:', vetor[numero], 'Posição:', numero)
    
