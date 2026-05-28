def exercicio_85():
    nomes = []
    sexos = []
    salarios = []
    
    for i in range(5):
        nomes.append(input('Digite seu nome: '))
        sexos.append(input('Digite seu sexo M/F: ').upper())
        salarios.append(float(input('Qual o seu salario: ')))
    
    print('Mulheres que ganham mais de R$ 5.000')
    
    for i in range(5):
        if sexos[i] == 'F' and salarios[i] > 5000:
            print(f'{nomes[i]} - R$ {salarios[i]:.2f}')
    
        
        