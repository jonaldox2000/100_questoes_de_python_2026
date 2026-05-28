def exercicio_66():
    numero = int(input('diga um número: '))
    
    for contador in range(11):
        valor = numero * contador
        print(f'{numero} x {contador} = {valor} ')
