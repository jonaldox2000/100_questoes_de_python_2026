def exercicio_84():
    nomes = []
    idades = []
    
    
    
    for num in range(9):
        nomes.append(input('Digite seu nome: '))
        idades.append(int(input('Digite sua idade: ')))
        
        
    print('Menores de idade: ')
    for num in range(9):
        if idades[num] < 18:
            print(f'{nomes[num]} - {idades[num]} anos')