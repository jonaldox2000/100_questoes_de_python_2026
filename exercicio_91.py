def exercicio_91():
    def maior(num_1 , num_2):
        if num_1 > num_2:
            print(f'O maior valor é: {num_1}')
        elif num_2 > num_1:
            print(f'O maior valor é: {num_2}')
        else:
            print('Os dois valores são iguais!')
            
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    
    
    maior(n1, n2)
