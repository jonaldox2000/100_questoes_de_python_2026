def exercicio_95():
    def somador(num_1, num_2):
        soma = num_1 + num_2
        return soma
    
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    
    print(somador(n1, n2))