Funcionalidades
- **Criar/Listar/Deletar** tarefas.
- **Busca inteligente** (Case Insensitive).
- **Edição** de tarefas existentes.
- **Persistência**: As tarefas são salvas em um arquivo `.txt` automaticamente.

Problema: O código não listava as tarefas devido ao erro de Case Sensitivity (variável Tarefas vs tarefas).
​Solução: Padronização de todas as variáveis

Adição de tratamento de erros com try/except para evitar que o programa feche ao digitar letras onde se pedem números.ra minúsculo (tarefas)
Implementação de filtro
