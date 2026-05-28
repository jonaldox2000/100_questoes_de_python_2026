def exercicio_37():
    salario = float(input('Qual seu salário atual:'))
    genero = input('Qual seu gênero M/F:')
    anos = int(input('Quantos anos trabalha na empresa:'))
    
    if genero == 'F':
        if anos < 15:
            novo_salario = salario * 1.05
        elif 15 <= anos <=20:
            novo_salario = salario * 1.12
        else:
            novo_salario = salario * 1.23
            
    elif genero == 'M':
        if anos < 20:
            novo_salario = salario * 1.03
        elif 20 <= anos <= 30:
            novo_salario = salario * 1.13
        else:
            novo_salario = salario * 1.25
            
    else:
        print('Gênero inválido. Use M ou F.')
        
    if novo_salario > 0:
        print(f'\n--- Resultado do Reajuste ---')
        print(f'Salário antigo:R$ {salario:.2f}')
        print(f'Tempo de empresa:{anos} anos')
        print(f'Novo salário:{novo_salario:.2f}')
        