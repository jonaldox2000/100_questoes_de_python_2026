def exercicio_29():
    print('Qual seu nome?')
    a = input()
    print('Qual é o seu salário?')
    b = float(input())
    print('Quantos anos de empresa?')
    c = float(input())
    a1 = b + b*0.03
    a2 = b + b*0.125
    a3 = b + b*0.20
    if c <= 3:
        print(f' Seu salário agora é {a1}')
    elif c < 10:
        if c > 3:
            print(f'Seu salário agora é {a2}')
    elif c >=10:
        print(f'Seu salário agora é {a3}')