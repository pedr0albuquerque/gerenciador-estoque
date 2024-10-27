import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()

class Application():
    def __init__(self):
        self.janela = janela
        self.tela()
        janela.mainloop()
        
    def tela(self):
        self.janela.title("Gerenciador") 
        self.janela.configure(background="red")
        self.janela.geometry("300x200")

        tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        entry_nome = tk.Entry(janela)
        entry_nome.grid(row=0, column=1, padx=5, pady=5)

        #  Preço
        tk.Label(janela, text="Preço:").grid(row=1, column=0, padx=5, pady=5)
        entry_preco = tk.Entry(janela)
        entry_preco.grid(row=1, column=1, padx=5, pady=5)

        # Quantidade
        tk.Label(janela, text="Quantidade:").grid(row=2, column=0, padx=5, pady=5)
        entry_quantidade = tk.Entry(janela)
        entry_quantidade.grid(row=2, column=1, padx=5, pady=5)

        # Botão 
        botao_cadastrar = tk.Button(janela, text="Cadastrar")
        botao_cadastrar.grid(row=3, column=0, columnspan=2, pady=10)

Application()    