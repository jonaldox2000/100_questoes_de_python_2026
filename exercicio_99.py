def exercicio_99():
    def Potencia(base, expoente):
        resultado = base ** expoente
        return resultado
    
    
    b = float(input('Digite o valor da base: '))
    e = float(input('Digite o valor do expoente: '))
    
    potencia_calculada = Potencia(b, e)
    
    
    print(f'O resultado de {b} elevado a {e} é: {potencia_calculada}')