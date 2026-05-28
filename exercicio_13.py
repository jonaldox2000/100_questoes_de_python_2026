def exercicio_13():
    salario = float(input('Digite seu salário atual:'))
    novo_salario = salario * 1.15
    salario_arredondado = round(novo_salario, 2)
    print(f"O salário com 15% de aumento passará a ser: R$ {salario_arredondado}")