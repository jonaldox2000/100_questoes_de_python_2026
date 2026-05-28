def exercicio_8():
    M1 = float(input('Digite uma distância em metros:'))
    Km = M1 / 1000
    Hm = M1 / 100
    Dam = M1 / 10
    Dm = M1 * 10
    Cm = M1 * 100
    Mm = M1 * 1000
    print(f'A distâcia em {M1} corresponde a:')
    print(f'{Km}Km')
    print(f'{Hm}Hm')
    print(f'{Dam}Dam')
    print(f'{Dm}Dm')
    print(f'{Cm}Cm')
    print(f'{Mm}Mm')
