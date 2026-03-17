tarefas = []
sair = False

while not sair:
    # Exibe o menu com a contagem de tarefas
    print(f"\n=== TASK MANAGER ({len(tarefas)} tarefas) ===")
    print("1-Criar 2-Listar 3-Deletar 4-Sair")
    
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
        # Implementação com confirmação 
        try:
            indice = input("Qual número da tarefa deseja deletar? ")
            idx = int(indice) - 1
            
            if 0 <= idx < len(tarefas):
                confirmar = input(f"Tem certeza que deseja deletar '{tarefas[idx]}'? (s/n): ")
                if confirmar.lower() == 's':
                    deletada = tarefas.pop(idx)
                    print(f"✔ '{deletada}' removida com sucesso!")
                else:
                    print("Ação cancelada.")
            else:
                print("X Índice inválido!")
        except ValueError:
            print("X Por favor, digite um número válido.")

    elif opcao == "4":
        # Confirmação de saída
        confirmacao = input("Tem certeza que deseja sair? (s/n): ")
        if confirmacao.lower() == "s":
            sair = True
            print("Até logo!")
    
    else:
        print("X Opção inválida!")

