import tkinter as tk

janela = tk.Tk()
janela.title("Gerenciador")
janela.geometry("300x300")

rotulo_usuario = tk.Label(janela, text="Usuario")
rotulo_usuario.pack()

entrada_usuario = tk.Entry(janela)
entrada_usuario.pack()

rotulo_senha = tk.Label(janela, text="senha")
rotulo_senha.pack()

entrada_senha = tk.Entry(janela)
entrada_senha.pack()

botao = tk.Button(janela, text="Login")
botao.pack()

janela.mainloop()