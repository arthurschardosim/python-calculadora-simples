import tkinter as tk

def clicar(valor):
    entrada.insert(tk.END, valor)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "ERROR")

def limpar():
    entrada.delete(0, tk.END)

janela = tk.Tk()
janela.title("Calculadora simples")
janela.geometry("300x500")
janela.resizable(False, False)

entrada = tk.Entry(janela, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entrada.pack(fill="both", ipadx=8, ipady=15)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(expand=True, fill="both")

botoes = (
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '+'),
    ('C', '0', '=', '-')
)

for linha in botoes:
    linha_frame = tk.Frame(frame_botoes)
    linha_frame.pack(expand=True, fill="both")

    for texto in linha:
        if texto == "=":
            botao = tk.Button(linha_frame, text=texto, font=("Arial", 18), command=calcular)

        elif texto == "C":
            botao = tk.Button(linha_frame, text=texto, font=("Arial", 18), command=limpar)

        else:
            botao = tk.Button(linha_frame, text=texto, font=("Arial", 18),
                              command=lambda val=texto: clicar(val))

        botao.pack(side="left", expand=True, fill="both")

janela.mainloop()	