import tkinter as tk

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)

def remover_tarefa():
    try:
        selecao = lista_tarefas.curselection()
        if selecao:
            indice = selecao[0]
            lista_tarefas.delete(indice)
    except:
        pass

# Crie uma instância da janela
janela = tk.Tk()
janela.title("To-Do List")

# Crie uma entrada de texto e um botão para adicionar tarefas
entrada_tarefa = tk.Entry(janela, width=40)
entrada_tarefa.pack(pady=10)
botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack()

# Crie uma lista para exibir as tarefas
lista_tarefas = tk.Listbox(janela, width=40)
lista_tarefas.pack()

# Crie um botão para remover tarefas selecionadas
botao_remover = tk.Button(janela, text="Remover Tarefa Selecionada", command=remover_tarefa)
botao_remover.pack(pady=10)

# Inicie o loop principal da aplicação
janela.mainloop()
