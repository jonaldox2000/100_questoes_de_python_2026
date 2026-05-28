def exercicio_22():
    from datetime import datetime
    
    data = datetime.now()
    anoAtual = data.year
    
    ano = int(input('digite o ano q vc nasceu:'))
    
    idade = anoAtual - ano
    
    if idade < 18:
        print(f' falta {18-idade} para poder se alistar')
    
    else:
        print(f'Já se passou {idade-18} do alistamento')