import tkinter as tk

# Criar uma janela
windowMain = tk.Tk()
windowMain.title("Gerenciador")

# Adicionar um rótulo
label = tk.Label(windowMain, text="Olá!")
label.pack()

# Executar o loop principal
windowMain.mainloop()