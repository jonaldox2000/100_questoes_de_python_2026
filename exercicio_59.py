def exercicio_59():
    maior_idade = 0
    
    homens = 0
    soma_homens = 0
    
    menor_mulher = 0
    primeira_mulher = True
    
    continuar = "S"
    
    while continuar == "S":
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ").upper()
        
        if idade > maior_idade:
            maior_idade = idade
        
        if sexo == "M":
            homens += 1
            soma_homens += idade
        
        elif sexo == "F":
            if primeira_mulher:
                menor_mulher = idade
                primeira_mulher = False
            else:
                if idade < menor_mulher:
                    menor_mulher = idade
        
        continuar = input("Quer continuar? (S/N): ").upper()
    
    if homens > 0:
        media_homens = soma_homens / homens
    else:
        media_homens = 0
    
    print("Maior idade:", maior_idade)
    print("Quantidade de homens:", homens)
    
    if primeira_mulher:
        print("Nenhuma mulher foi cadastrada")
    else:
        print("Idade da mulher mais jovem:", menor_mulher)
    
    print("Média de idade dos homens:", media_homens)