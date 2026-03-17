tarefas = []
sair = False

while not sair:
    print(f"\n=== TASK MANAGER ({len(tarefas)} tarefas) ===")
    print("1-Criar 2-Listar 3-Deletar 4-Sair 5-Buscar 6-Editar")
    
    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome da tarefa: ")
        if nome.strip():
            tarefas.append(nome)
            print("✔ Tarefa Criada!")
        else:
            print("X Nome não pode ser vazio.")

    elif opcao == "2":
        print("\n--- Lista de Tarefas ---")
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t}")

    elif opcao == "3":
        try:
            idx = int(input("Qual número deseja deletar? ")) - 1
            if 0 <= idx < len(tarefas):
                confirmar = input(f"Deletar '{tarefas[idx]}'? (s/n): ")
                if confirmar.lower() == 's':
                    tarefas.pop(idx)
                    print("✔ Removida!")
            else:
                print("X Índice inválido!")
        except ValueError:
            print("X Digite um número.")

    elif opcao == "4":
        if input("Sair? (s/n): ").lower() == "s":
            sair = True
            print("Até logo!")

    elif opcao == "5":
        termo = input("Buscar: ").lower()
        encontradas = [t for t in tarefas if termo in t.lower()]
        print(f"\n--- Resultados para '{termo}' ---")
        for t in encontradas: print(f"🔍 {t}")
        if not encontradas: print("Nada encontrado.")

    elif opcao == "6":
        try:
            idx = int(input("Número para editar: ")) - 1
            if 0 <= idx < len(tarefas):
                tarefas[idx] = input(f"Novo nome para '{tarefas[idx]}': ")
                print("✔ Editada!")
        except ValueError:
            print("X Digite um número.")
    
    else:
        print("X Opção inválida!")

