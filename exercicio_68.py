def exercicio_68():
    
    
    
    soma_mulheres = 0
    homens_mais_100 = 0
    maior_peso = 0
    mulheres = 0
    homens = 0
    
    for pessoa in range(8):
        peso = int(input('Qual o seu peso: '))
        sexo = input("Digite o sexo (M/F): ").upper()
        
        if sexo == 'F':
            mulheres += 1
            soma_mulheres += peso
        
        if sexo == 'M':
            homens += 1
            if peso > 100:
               homens_mais_100 += 1
               if pessoa == 0:
                  maior_peso = peso
        
    if mulheres > 0:
        media_mulheres = soma_mulheres / mulheres
    else:
        media_mulheres = 0
    
    print(f'foram {mulheres} mulheres que foram cadastradas.')
    print(f'{homens_mais_100} homens que pesam mais de 100KG')
    print(f'A média de peso entre as mulheres é {media_mulheres}')
    print(f'O maior peso entre os homens é {maior_peso}')
    
