def exercicio_90():
    def Somador(num_1, num_2):
        soma = num_1 + num_2
        print(f'A soma entre {num_1} e {num_2} é: {soma}')
        
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    
    Somador(n1, n2)