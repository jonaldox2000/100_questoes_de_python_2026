import importlib # essa biblioteca acessa arquivos


while True:
    n = input("\nQual questão testar? (0 para sair): ")
    if n == '0': # formar de encerrar o progama
        break
    
    try:# bloco responsavel pelos erros, se alguns dos codigos der erro, para que o progama não quebre e pule para except	
       
        modulo = importlib.import_module(f"exercicio_{n}") # transforma o texto em exercicio1 e usa importlib procurar e carregar o arquivo
        getattr(modulo, f"exercicio_{n}")() # procura o arquivo que foi carregado no modulo se e (n) for 1 ele procura uma função chamada exercicio_
    except Exception:
        print("[!] Questão não encontrada ou erro na execução.")
        
        # O erro foi que tava q_ e fui e troquei para exercicio_ e salvei nas questoes renomeadas
        