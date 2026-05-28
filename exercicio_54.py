def exercicio_54():
    validador = 0
    pesa_90 = 0
    menos_50_160 = 0
    medem_190_100 = 0
    soma_altura = 0
    
    while validador < 7:
        peso = int(input('Qual o seu peso: '))
        altura = float(input('Qual a sua altura: '))
        soma_altura += altura
        
        if peso > 90:
            pesa_90 += 1
        if peso < 50:
            if altura < 1.60:
                menos_50_160 += 1
        if altura > 1.90:
            if peso > 100:
                medem_190_100 += 1
              
        validador += 1
    media = soma_altura / 7
    print(f'Media de altura:{media:.2f}.')
    print(f'{pesa_90} pessoas que pesam mais de 90KG')
    print(f'{menos_50_160} pessoas que pesam menos de 50KG e tem menos de 1.60')
    print(f'{medem_190_100} pessoas que medem mais de 1.90 e pesam mais de 100KG')
