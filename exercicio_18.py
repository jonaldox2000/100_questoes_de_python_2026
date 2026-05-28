def exercicio_18():
    a = int(input())
    b = 2026 - a
    print('Qual ano você nasceu?')
    if b >= 16:
        print('Você pode votar')
    else:
        print('Não pode votar')