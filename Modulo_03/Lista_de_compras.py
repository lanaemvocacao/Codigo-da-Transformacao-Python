'''


'''

lista_compras = []

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Ver lista")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        item = input("Digite o nome do item: ")
        lista_compras.append(item)
        print(f"'{item}' adicionado com sucesso!")
    elif opcao == '2':
        item = input("Digite o nome do item para remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"'{item}' removido!")
        else:
            print("Item não encontrado.")
    elif opcao == '3':
        print("\nSua lista atual:", lista_compras)
    elif opcao == '4':
        break
    else:
        print("Opção inválida.")