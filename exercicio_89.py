def exercicio_89():
    def gerador(mensagem, repeticoes, borda):
        if borda == 1:
            print('+-------=======--------+')
        elif borda == 2:
            print('~~~~~~~~:::::::~~~~~~~~')
        elif borda == 3:
            print('<<<<<<<<------->>>>>>>')
            
        for i in range(repeticoes):
            print(f' {mensagem}')
            
        if borda == 1:
            print('+-------=======--------+')
        elif borda == 2:
            print('~~~~~~~~:::::::~~~~~~~~')
        elif borda == 3:
            print('<<<<<<<<------->>>>>>>')
        
    gerador('Portugol Studio', 3, 2)
            