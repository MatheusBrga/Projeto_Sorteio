from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry('400x220')
root.maxsize(400, 220)
root.minsize(400, 220)
root.title('Sorteio')
root.configure(bg='#C0C0C0')

def sorteio():
    primeiro_numero_label = entry_primeiro_numero.get()
    numero_final_label = entry_numero_final.get()

    if primeiro_numero_label and numero_final_label:
        if primeiro_numero_label.isdigit() and numero_final_label.isdigit():
            if numero_final_label > primeiro_numero_label:
                primeiro_numero_label = int(primeiro_numero_label)
                numero_final_label = int(numero_final_label)

                rand = random.randint(primeiro_numero_label, numero_final_label)
                messagebox.showinfo('Sorteio', rand)
            else:
                messagebox.showwarning('Atenção', 'O número final deve ser maior que o primeiro número.')

        else:
            messagebox.showerror('Erro', 'Digite apenas números inteiros.')

    else:
        messagebox.showwarning('Atenção', 'Você precisa preencher todos os campos.')

sorteio_label = Label(root, text='Sorteio', bg='#C0C0C0', fg='black', font='Arial 16 bold', width=9, height=2)
sorteio_label.place(x='', y='')

primeiro_numero_label = Label(root, text='Primeiro número', bg='#C0C0C0', fg='black', font='Arial 12 bold', width=15, height=2)
primeiro_numero_label.place(x='', y=60)

numero_final_label = Label(root, text='Número final', bg='#C0C0C0', fg='black', font='Arial 12 bold', width=15, height=2)
numero_final_label.place(x=200 , y=60)

entry_primeiro_numero = Entry(root, bg='white', fg='black', font='Arial 18', width=12)
entry_primeiro_numero.place(x=11, y=95)

entry_numero_final = Entry(root, bg='white', fg='black', font='Arial 18', width=12)
entry_numero_final.place(x=226, y=95)

botao_sortear = Button(root, bg='#836FFF', fg='white', text='Sortear número', font='Arial 16 bold', width=28, command=sorteio)
botao_sortear.place(x=11, y=160)
root.mainloop()