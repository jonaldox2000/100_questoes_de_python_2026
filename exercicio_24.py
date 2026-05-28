def exercicio_24():
    distancia = int(input('Qual distâcia que percorrer em Km:'))
    
    if distancia <= 200:
        passagem = distancia * 0.50
        print(f'Você tera que pagar {passagem}')
    
    else:
        passagem = distancia * 0.45
        print(f'Você tera que pagar {passagem}')