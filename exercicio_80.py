def exercicio_80():
    import random
    
    vetor = []
    for numero in range(30):
        vetor.append(random.randint(1, 15))
        
    chave = int(input('Digite um número entre (1 e 15): '))
    
    total = 0
    
    print(' Posições encontradas ')
    
    for numero in range(30):
        if vetor[numero] == chave:
            print('Posição:', numero)
            total += 1
    print(f'O número apareceu {total} vezes.')