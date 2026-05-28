def exercicio_23():
    nome = input('Qual seu nome:')
    sexo = input(' Qual sua sexualidade [F/M]:')
    valor = int(input('Qual valor das suas compras:'))
     
    if sexo == 'm':
        desconto = valor - valor * 0.05
        print(desconto)
        
    else:
        desconto = valor - valor * 0.13
        print(desconto)