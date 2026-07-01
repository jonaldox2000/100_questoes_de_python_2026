
import os
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


print("""

██████╗░███████╗░██████╗████████╗░█████╗░██╗░░░██╗██████╗░░█████╗░███╗░░██╗████████╗███████╗
██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔════╝
██████╔╝█████╗░░╚█████╗░░░░██║░░░███████║██║░░░██║██████╔╝███████║██╔██╗██║░░░██║░░░█████╗░░
██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░██╔══██║██║░░░██║██╔══██╗██╔══██║██║╚████║░░░██║░░░██╔══╝░░
██║░░██║███████╗██████╔╝░░░██║░░░██║░░██║╚██████╔╝██║░░██║██║░░██║██║░╚███║░░░██║░░░███████╗
╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝ """)








def menu():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Adicionar avaliação")
    print("5. Adicionar item ao cardápio")
    print("6. Exibir cardápio")
    print("7. Sair")

    int(input('Escolha uma opção:'))

def cadastrar_restaurante():
    print("\n" + "="*30)
    print("CADASTRAR NOVO RESTAURANTE")
    print("="*30)

    nome = input("Digite o nome do restaurante: ").strip()
    categoria = input("Digite a categoria do restaurante (ex: Italiana, Japonesa): ").strip()
    if nome and categoria:
        restaurantes.append({"nome": nome, "categoria": categoria, "ativo": False, "avaliacoes": [], "cardapio": []})
        print("Cadastrado com sucesso!")
                  
                  

def listar_restaurantes():
    print("\n=== LISTA ===")
    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
    for i, r in enumerate(restaurantes, 1):
        status = "Ativo" if r["ativo"] else "Inativo"
        print(f"{i}. {r['nome']} ({r['categoria']}) - [{status}]")

def alternar_estado_restaurante():
    listar_restaurantes()
    try:
        idx = int(input("\nDigite o número para alterar o status: ")) - 1
        restaurantes[idx]["ativo"] = not restaurantes[idx]["ativo"]
        print(f"Status de '{restaurantes[idx]['nome']}' alterado!")
    except (ValueError, IndexError):
        print("Opção inválida.")

def adicionar_avaliacao():
    listar_restaurantes()
    try:
        idx = int(input("\nNúmero do restaurante a avaliar: ")) - 1
        nota = int(input("Nota (1 a 5): "))
        if 1 <= nota <= 5:
            comentario = input("Comentário: ")
            restaurantes[idx]["avaliacoes"].append({"nota": nota, "comentario": comentario})
            print("Avaliação adicionada!")
    except (ValueError, IndexError):
        print("Entrada inválida.")

def adicionar_item_cardapio():
    listar_restaurantes()
    try:
        idx = int(input("\nNúmero do restaurante para o cardápio: ")) - 1
        item = input("Nome do item: ")
        preco = float(input("Preço: R$ "))
        restaurantes[idx]["cardapio"].append({"item": item, "preco": preco})
        print("Item adicionado!")
    except (ValueError, IndexError):
        print("Entrada inválida.")

def exibir_cardapio():
    listar_restaurantes()
    try:
        idx = int(input("\nNúmero do restaurante para exibir: ")) - 1
        r = restaurantes[idx]
        print(f"\n=== {r['nome'].upper()} ===")
        
        # Média das notas
        notas = [av["nota"] for av in r["avaliacoes"]]
        media = sum(notas) / len(notas) if notas else 0
        print(f"Média: {media:.1f} ⭐")
        
        # Itens do cardápio
        print("CARDÁPIO:")
        for item in r["cardapio"]:
            print(f"- {item['item']}: R$ {item['preco']:.2f}")
    except (ValueError, IndexError):
        print("Opção inválida.")

    