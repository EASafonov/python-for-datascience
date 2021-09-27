import tkinter
from tkinter import *
from tkinter.ttk import *
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd


sizes = []
fig = ''

root = Tk()
root.title("Расчёт витаминов")
root.geometry('640x480')

# columns labels
l0_0 = Label(root, text='Продукт')
l0_1 = Label(root, text='Витамин A')
l0_2 = Label(root, text='Витамин B')
l0_3 = Label(root, text='Витамин C')
l0_4 = Label(root, text='Витамин D')
l0_5 = Label(root, text='Витамин E')

l0_0.grid(row=0, column=0, sticky=W+E, pady=10)
l0_1.grid(row=0, column=1, sticky=W+E, pady=10)
l0_2.grid(row=0, column=2, sticky=W+E, pady=10)
l0_3.grid(row=0, column=3, sticky=W+E, pady=10)
l0_4.grid(row=0, column=4, sticky=W+E, pady=10)
l0_5.grid(row=0, column=5, sticky=W+E, pady=10)

l1_0 = Label(root, text='1')
l2_0 = Label(root, text='2')
l3_0 = Label(root, text='3')
l4_0 = Label(root, text='4')
l5_0 = Label(root, text='5')

l1_0.grid(row=1, column=0, sticky=W+E, pady=10)
l2_0.grid(row=2, column=0, sticky=W+E, pady=10)
l3_0.grid(row=3, column=0, sticky=W+E, pady=10)
l4_0.grid(row=4, column=0, sticky=W+E, pady=10)
l5_0.grid(row=5, column=0, sticky=W+E, pady=10)

# Entering the data
ent1_1 = Entry(root, width=10)
ent1_2 = Entry(root, width=10)
ent1_3 = Entry(root, width=10)
ent1_4 = Entry(root, width=10)
ent1_5 = Entry(root, width=10)

ent2_1 = Entry(root, width=10)
ent2_2 = Entry(root, width=10)
ent2_3 = Entry(root, width=10)
ent2_4 = Entry(root, width=10)
ent2_5 = Entry(root, width=10)

ent3_1 = Entry(root, width=10)
ent3_2 = Entry(root, width=10)
ent3_3 = Entry(root, width=10)
ent3_4 = Entry(root, width=10)
ent3_5 = Entry(root, width=10)

ent4_1 = Entry(root, width=10)
ent4_2 = Entry(root, width=10)
ent4_3 = Entry(root, width=10)
ent4_4 = Entry(root, width=10)
ent4_5 = Entry(root, width=10)

ent5_1 = Entry(root, width=10)
ent5_2 = Entry(root, width=10)
ent5_3 = Entry(root, width=10)
ent5_4 = Entry(root, width=10)
ent5_5 = Entry(root, width=10)


ent1_1.grid(row=1, column=1, sticky=W, pady=10)
ent1_2.grid(row=1, column=2, sticky=W, pady=10)
ent1_3.grid(row=1, column=3, sticky=W, pady=10)
ent1_4.grid(row=1, column=4, sticky=W, pady=10)
ent1_5.grid(row=1, column=5, sticky=W, pady=10)

ent2_1.grid(row=2, column=1, sticky=W, pady=10)
ent2_2.grid(row=2, column=2, sticky=W, pady=10)
ent2_3.grid(row=2, column=3, sticky=W, pady=10)
ent2_4.grid(row=2, column=4, sticky=W, pady=10)
ent2_5.grid(row=2, column=5, sticky=W, pady=10)

ent3_1.grid(row=3, column=1, sticky=W, pady=10)
ent3_2.grid(row=3, column=2, sticky=W, pady=10)
ent3_3.grid(row=3, column=3, sticky=W, pady=10)
ent3_4.grid(row=3, column=4, sticky=W, pady=10)
ent3_5.grid(row=3, column=5, sticky=W, pady=10)

ent4_1.grid(row=4, column=1, sticky=W, pady=10)
ent4_2.grid(row=4, column=2, sticky=W, pady=10)
ent4_3.grid(row=4, column=3, sticky=W, pady=10)
ent4_4.grid(row=4, column=4, sticky=W, pady=10)
ent4_5.grid(row=4, column=5, sticky=W, pady=10)

ent5_1.grid(row=5, column=1, sticky=W, pady=10)
ent5_2.grid(row=5, column=2, sticky=W, pady=10)
ent5_3.grid(row=5, column=3, sticky=W, pady=10)
ent5_4.grid(row=5, column=4, sticky=W, pady=10)
ent5_5.grid(row=5, column=5, sticky=W, pady=10)

def calculate_proportion():
    global sizes
    data = np.array([
        [ent1_1, ent2_1, ent3_1, ent4_1, ent5_1],
        [ent1_2, ent2_2, ent3_2, ent4_2, ent5_2],
        [ent1_3, ent2_3, ent3_3, ent4_3, ent5_3],
        [ent1_4, ent2_4, ent3_4, ent4_4, ent5_4],
        [ent1_5, ent2_5, ent3_5, ent4_5, ent5_5],
    ])
    vfunc = np.vectorize(format_value)
    data = vfunc(data)
    targets = np.array([170, 180, 140, 180, 350]).reshape((5, 1))
    x = solve(data, targets)
    labels = ['Продукт 1', 'Продукт 2', 'Продукт 3', 'Продукт 4', 'Продукт 5']
    sizes = x.reshape(1, 5)[0].tolist()
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
    draw_plot(root, sizes, labels, colors)
    print(x)


def format_value(value):
    if value.get().isnumeric():
        formatted_value = int(value.get())
    else:
        formatted_value = 0
    return formatted_value


def draw_plot(tk_window, results, lbls, clrs):
    global fig
    # the figure that will contain the plot
    fig = Figure(figsize=(4, 3),
                 dpi=100)
    y = results

    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    plot1.pie(y,
              labels=lbls,
              colors=clrs,
              autopct='%1.1f%%',
              shadow=True,
              startangle=140)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=tk_window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(row=6, column=0, columnspan=4, rowspan=3, sticky=E, pady=10)


def save_data():
    global sizes
    df = pd.DataFrame(sizes)
    df.to_csv('results.csv', sep=';')
    pass


def save_plot():
    fig.savefig('pieplot.png')


button_calc = Button(root, text="Рассчитать", command=calculate_proportion)
button_calc.grid(row=6, column=5, sticky=W, pady=10)

save_data_button = Button(root, text="Сохранить данные", command=save_data)
save_data_button.grid(row=7, column=5, sticky=W, pady=10)

save_plot_button = Button(root, text="Сохранить диаграмму", command=save_plot)
save_plot_button.grid(row=8, column=5, sticky=W, pady=10)

root.bind('<Escape>', lambda x: root.destroy())
root.mainloop()
