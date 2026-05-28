def exercicio_51():
    validador = 0
    maior_preco = 0
    menor_preco = 9999999999999999999999999999999999
    
    while validador < 8:
        produto = int(input(f'Diga o valor do {validador}º produto:'))
        validador += 1
    
        if produto > maior_preco:
            maior_preco = produto
            
        if produto < menor_preco:
            menor_preco = produto
        
    print(f'O maior preço é {maior_preco}')
    print(f'O menor preço é {menor_preco}')
