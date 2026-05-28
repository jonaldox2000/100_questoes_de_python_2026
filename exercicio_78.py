def exercicio_78():
    vetor = []
    
    for numero in range(15):
        num = int(input(f'Digite o {numero+1} número: '))
        vetor.append(num)
    
    print(f'Vetor completo: {vetor}')
    print('Posições com múltiplos de 10:')
    for numero in range(15):
        if vetor[numero] % 10 == 0:
            print(f'posição {numero}')