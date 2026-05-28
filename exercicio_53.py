def exercicio_53():
    validador = 0
    soma_idades = 0
    homens = 0
    mulher = 0
    mulher_20 = 0
    
    while validador < 0:
        idade = int(input('Qual a sua idade: '))
        genero = input('Qual seu gênero M/F:')
        soma_idades += idade
        
        if genero == 'M':
            homens += 1
        if genero == 'F':
            mulher += 1
            if idade > 20:
               mulher_20 += 1 
        validador += 1
    media = soma_idades / 5
    media_homens = homens / 5
    print(f'São {homens} homens cadastrados.')
    print(f'São {mulher} mulheres cadastradas.')
    print(f'{mulher_20} são mulheres que tem mais de vinte anos')
    print(f'Media das idades: {media}')
    print(f'A media de homens é {media_homens}.')