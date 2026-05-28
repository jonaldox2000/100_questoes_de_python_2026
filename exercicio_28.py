def exercicio_28():
    largura = float(input('Digite a largura:'))
    comprimento = float(input('Digite o comprimento:'))
    area = largura * comprimento
    print(f'Área do terreno: {area:.2f} m²')
    
    if area < 100:
        print('Classificação: TERRENO POPULAR')
        
    elif 100 <= area <= 500:
        print('Classificação: TERRENO MASTER')
        
    else:
        print('Classificação: TERRENO VIP')