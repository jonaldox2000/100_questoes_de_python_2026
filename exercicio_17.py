def exercicio_17():
    limite = 80
    velocidade = int(input('Qual a sua velocidade:'))
    if velocidade > limite:
        km_acima = velocidade - limite
        multa = km_acima * 5
        
        print(f"MULTADO! Você excedeu o limite de {limite}Km/h.")
        print(f"Velocidade excedente: {km_acima}Km/h.")
        print(f"Valor da multa: R${multa:.2f}")
    else:
        print("Velocidade dentro do limite. Dirija com segurança!")
        