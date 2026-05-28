def exercicio_69():
    termo = int(input(' Digite um termo: '))
    razao = int(input('Digite a razão: '))
    soma = 0
    
    for contagem in range(10):
        termo += razao
        print(termo , end=' ')
        soma += termo
        
    print()
    print(f'A soma dos termos é {soma}')