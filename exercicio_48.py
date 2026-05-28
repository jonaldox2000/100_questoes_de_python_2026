def exercicio_48():
    numero = 0
    soma = 0
    
    while numero < 7:
        valor = int(input('Digite um numero: '))
        numero = numero + 1
        soma = soma + valor
    
    print(soma)