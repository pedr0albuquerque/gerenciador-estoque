import tkinter as tk

janela = tk.Tk()
janela.title("Gerenciador")
janela.geometry("300x300")

rotulo_nome = tk.Label(janela, text="Nome")
rotulo_nome.pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack()

rotulo_preco = tk.Label(janela, text="Preco")
rotulo_preco.pack()

entrada_preco = tk.Entry(janela)
entrada_preco.pack()

rotulo_quantidade = tk.Label(janela, text="Preco")
rotulo_quantidade.pack()

entrada_quantidade = tk.Entry(janela)
entrada_quantidade.pack()

botao = tk.Button(janela, text="Cadastrar")
botao.pack()

botao = tk.Button(janela, text="Ver Estoque")
botao.pack()

janela.mainloop()