def exercicio_92():
    def ParOuImpar(numero):
        if numero % 2 == 0:
            print(f'O número {numero} é PAR.')
        else:
            print(f'O número {numero} é ÌMPAR.')
    
    
    num = int(input('Digite um número inteiro: '))
    
    ParOuImpar(num)