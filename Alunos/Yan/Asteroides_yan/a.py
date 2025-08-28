import tkinter as tk

# Função para desenhar
def desenhar(canvas):
    # Desenhar um círculo (rosto)
    canvas.create_oval(150, 100, 350, 300, outline="black", width=3)

    # Desenhar olhos
    canvas.create_oval(200, 150, 220, 170, fill="black")
    canvas.create_oval(280, 150, 300, 170, fill="black")

    # Desenhar boca
    canvas.create_arc(210, 220, 290, 260, start=0, extent=-180, style=tk.ARC)

    # Texto fictício
    canvas.create_text(250, 50, text="Imagine que é a Mona Lisa 😄", font=("Arial", 16))

# Criar janela
janela = tk.Tk()
janela.title("Desenho em Python")
janela.geometry("500x400")

# Criar canvas para desenhar
canvas = tk.Canvas(janela, width=500, height=400, bg="white")
canvas.pack()

# Chamar função de desenho
desenhar(canvas)

# Iniciar janela
janela.mainloop()
