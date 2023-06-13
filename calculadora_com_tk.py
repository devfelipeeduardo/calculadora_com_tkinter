from tkinter import *

#Abre Janela
janela = Tk()
janela.title('Calculadora') #Título
janela.geometry('250x350') #Dimensão
janela.config(bg='white') #Configura a cor do Fundo
janela.iconphoto(False, PhotoImage(file='calculadora.png')) # Ícone
janela.resizable(width=False, height=False) # Não permite alteração na Largura e Altura


###

resultado_operacao = 0.0
label_fonte = ('Arial 15 bold')
label_fg = '#000000'
espaco = 10
operacoes_validas = ['+', '-', '*', '/']

###


#FUNÇÕES

def obter_dados():
    numero1 = entry_numero1.get()
    numero2 = entry_numero2.get()
    operacao = entry_operacao.get()

    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
    except ValueError:
        print("Digite um valor válido!")
    except:
        print("Erro Desconhecido")

    if operacao not in operacoes_validas:
        print("Digite uma operação válida! ")
    else:
        if operacao == '+':
            label_mostra_resultado['text'] = numero1 + numero2
        elif operacao == '-':
            label_mostra_resultado['text'] = numero1 - numero2
        elif operacao == '*':
            label_mostra_resultado['text'] = numero1 * numero2
        elif operacao == '/':
            label_mostra_resultado['text'] = numero1 / numero2
            



#Número 1
label_numero1 = Label(janela, width=10, height=2, text='Número 1: ', font=label_fonte, fg=label_fg, bg='lightgrey')
label_numero1.place(x=10, y=10)
entry_numero1 = Entry(janela, width=10, font=('Arial 12 bold'), bg='lightgrey')
entry_numero1.place(x=140, y=20)

#Número 2
label_numero2 = Label(janela, width=10, height=2, text='Número 2:', font=label_fonte, fg=label_fg, bg='lightgrey')
label_numero2.place(x=10, y=80)
entry_numero2 = Entry(janela, width=10, font=('Arial 12 bold'), bg='lightgrey')
entry_numero2.place(x=140, y=90)

#Operação
label_operacao = Label(janela, width=10, height=2, text='Operação: ', font=label_fonte, fg=label_fg, bg='lightgrey')
label_operacao.place(x=10, y=150)
entry_operacao = Entry(janela, width=10, font=('Arial 12 bold'), bg='lightgrey')
entry_operacao.place(x=140, y=160)

#Calcular
button_calcular = Button(janela, width=7, height=1, command=obter_dados, text='Calcular', relief='raised', font=label_fonte, fg='#000000', bg='lightgrey')
button_calcular.place(x=73, y=220)

#Resultado
label_resultado = Label(janela, width=9, height=2, text="Resultado:", font=label_fonte, fg=label_fg, bg='lightgrey' )
label_resultado.place(x=10, y= 280)

label_mostra_resultado= Label(janela, width=8, height=1, text=resultado_operacao, font=label_fonte, fg=label_fg, bg='lightgrey' )
label_mostra_resultado.place(x=130, y= 290)



janela.mainloop()

