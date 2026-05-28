def exercicio_19():
    nome = input('Nome do aluno: ')
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    media = (n1 + n2) / 2
    
    print(f'A média de {nome} foi {media:.1f}.')
    
    if media >= 7.0:
        print('Resultado: Teve um BOM APROVEITAMENTO!')
    else:
        print('Resultado: Não teve um bom aproveitamento.')