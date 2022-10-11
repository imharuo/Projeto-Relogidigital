from tkinter import *
from datetime import datetime
import pyglet


# colors
back_color: str = '#403f3e'
front_color: str = '#ede593'

# window configuration
window = Tk()
window.title('Relógio Digital')
window.geometry('460x180')
window.configure(bg=back_color)
window.resizable(width=False, height=False)
pyglet.font.add_file('alarmclock.ttf')
pyglet.font.add_file('digital-7.ttf')

# time/hour
dias = {'Monday': 'Segunda', 'Tuesday': 'Terca', 'Wednesday': 'Quarta', 'thursday': 'Quinta',
        'Friday': 'Sexta', 'Saturday': 'Sabado', 'Sunday': 'Domingo'}

def relogio():
    tempo: datetime = datetime.now()

    hora: str = tempo.strftime('%H:%M:%S')
    dia_semana: str = tempo.strftime('%A') # a retorna o dia da semana por extenso
    dia: tempo = tempo.day
    mes: str = tempo.strftime('%b')  # b abrevia nome do mes
    ano: str = tempo.strftime('%Y')

    
    if dia_semana == 'Monday':
       dia_semana = dias['Monday']
    elif dia_semana == 'Tuesday':
        dia_semana = dias['Tuesday']
    elif dia_semana == 'Wednesday':
        dia_semana = dias['Wednesday']
    elif dia_semana == 'Thursday':
        dia_semana = dias['Thursday']
    elif dia_semana == 'Friday':
        dia_semana = dias['Friday']
    elif dia_semana == 'Saturday':
        dia_semana = dias['Saturday']
    elif dia_semana == 'Sunday':
        dia_semana = dias['Sunday']    

    if mes == 'Feb':
        mes = 'Fev'
    elif mes =='Apr':
        mes = 'Abr'
    elif mes =='May':
        mes = 'Maio'
    elif mes =='Aug':
        mes = 'Ago'
    elif mes =='Sep':
        mes = 'Set'
    elif mes =='Oct':
        mes = 'Out'
    elif mes =='Dec':
        mes = 'Dez'
    

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + '  ' + str(dia) + '/' + str(mes) + '/' + str(ano))


# labels time
l1 = Label(window, text='hora atual', font=('"alarm clock" 80'), bg=back_color, fg=front_color)
l1.grid(row=0, column=0, sticky=W)

l2 = Label(window, text='Segunda 10/10/2022', font=('digital-7 20'), bg=back_color, fg=front_color)
l2.grid(row=1, column=0, sticky=S)



relogio()
window.mainloop()

