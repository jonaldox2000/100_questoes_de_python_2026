def exercicio_15():
    dias_trabalhados = int(input('Quantos dias o funcionário trabalhou este mês? '))
    salario_final = dias_trabalhados * 8 * 25
    print(f'O funcionário trabalhou {dias_trabalhados} dias.')
    print(f'O valor total do salário a ser pago é R${salario_final:.2f}')