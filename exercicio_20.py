def exercicio_20():
    numero = int(input('Digite um número inteiro qualquer: '))
    resultado = numero % 2
    
    if resultado == 0:
        print(f'O número {numero} é PAR.')
    else:
        print(f'O número {numero} é ÍMPAR.')