def exercicio_97():
    def Maior(valor1, valor2, valor3):
        maior = valor1
    
        if valor2 > maior:
            maior = valor2
    
        if valor3 > maior:
            maior = valor3
    
        return maior
    
    
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    
    resultado = Maior(num1, num2, num3)
    
    print("O maior número é:", resultado)