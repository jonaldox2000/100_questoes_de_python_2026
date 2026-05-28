def exercicio_33():
    casa = float(input('Valor da casa:'))
    salario = float(input('Qual seu salário:'))
    anos = int(input('Em quantos anos de financiamento:'))
    
    prestacao = casa / (anos * 12)
    
    limite = salario * 0.30
    
    print(f'\nPara pagar uma casa de R$ {casa:.2f} em {anos} anos')
    print(f'a prestação será de R$ {prestacao:.2f}.')
    
    if prestacao <= limite:
        print('Empréstimo pode ser APROVADO!')
    else:
        print('Empréstimo NEGADO! A prestação excede 30% do seu salário.')
        
