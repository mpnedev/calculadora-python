import tkinter as tk

def somar():
    try:
        resultado = float(entrada_1.get()) + float(entrada_2.get())
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        label_resultado.config(text="Erro: Entrada inválida")

def subtrair():
    try:
        resultado = float(entrada_1.get()) - float(entrada_2.get())
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        label_resultado.config(text="Erro: Entrada inválida")

def multiplicar():
    try:
        resultado = float(entrada_1.get()) * float(entrada_2.get())
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        label_resultado.config(text="Erro: Entrada inválida")

def dividir():
    try:
        num1 = float(entrada_1.get())
        num2 = float(entrada_2.get())
        if num2 != 0:
            resultado = num1 / num2
            label_resultado.config(text="Resultado: " + str(resultado))
        else:
            label_resultado.config(text="Erro: Divisão por zero")
    except ValueError:
        label_resultado.config(text="Erro: Entrada inválida")

janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x300")
janela.config(bg="#f0f0f0")

label_1 = tk.Label(janela, text="Primeiro número:", bg="#f0f0f0")
label_1.grid(row=0, column=0, padx=10, pady=5)

entrada_1 = tk.Entry(janela)
entrada_1.grid(row=0, column=1, padx=10, pady=5)

label_2 = tk.Label(janela, text="Segundo número:", bg="#f0f0f0")
label_2.grid(row=1, column=0, padx=10, pady=5)

entrada_2 = tk.Entry(janela)
entrada_2.grid(row=1, column=1, padx=10, pady=5)

btn_soma = tk.Button(janela, text="+", width=10, command=somar)
btn_soma.grid(row=2, column=0, padx=10, pady=5)

btn_sub = tk.Button(janela, text="-", width=10, command=subtrair)
btn_sub.grid(row=2, column=1, padx=10, pady=5)

btn_mult = tk.Button(janela, text="*", width=10, command=multiplicar)
btn_mult.grid(row=3, column=0, padx=10, pady=5)

btn_div = tk.Button(janela, text="/", width=10, command=dividir)
btn_div.grid(row=3, column=1, padx=10, pady=5)

label_resultado = tk.Label(janela, text="Resultado: ", bg="#f0f0f0")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()
