from tkinter import *
from datetime import datetime
import pyglet


# colors
back_color: str = '#403f3e'
front_color: str = '#ede593'

# window configuration
window = Tk()
window.title('Relógio Digital')
window.geometry('440x180')
window.configure(bg=back_color)
window.resizable(width=False, height=False)
pyglet.font.add_file('alarm clock.ttf')

# time/hour


def relogio():
    tempo: datetime = datetime.now()

    hora: str = tempo.strftime('%H:%M:%S')
    dia_semana: str = tempo.strftime('%A')
    dia: tempo = tempo.day
    mes: tempo = tempo.strftime('%b')
    ano: tempo = tempo.strftime('%Y')

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + '  ' + str(dia) + '/' + str(mes) + '/' + str(ano))


# labels time
l1 = Label(window, text='hora atual', font='Arial 80', bg=back_color, fg=front_color)
l1.grid(row=0, column=0)

l2 = Label(window, text='Segunda 10/10/2022', font='Arial 20', bg=back_color, fg=front_color)
l2.grid(row=1, column=0, padx=5, sticky=NW)

relogio()
window.mainloop()

