def exercicio_49():
    numero = 0
    soma = 0
    pares = 0
    impares = 0
    
    while numero < 6:
        valor = int(input('Digite um numero: '))
        numero = numero + 1
        resultado = valor % 2
        
        if resultado == 0:
            print(f'O número {valor} é PAR.')
            pares = pares + 1
        else:
            print(f'O número {valor} é ÍMPAR.')
            impares += 1
    
    
    print(f'Os {pares} termos são pares')
    print(f'Os {impares} termos são impares')