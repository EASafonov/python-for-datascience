import tkinter
from tkinter import *
from tkinter.ttk import *
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

root = Tk()
root.title("Расчёт витаминов")
#root.geometry('640x480')

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
    data = np.array([
        [format_value(ent1_1), format_value(ent2_1), format_value(ent3_1), format_value(ent4_1), format_value(ent5_1)],
        [format_value(ent1_2), format_value(ent2_2), format_value(ent3_2), format_value(ent4_2), format_value(ent5_2)],
        [format_value(ent1_3), format_value(ent2_3), format_value(ent3_3), format_value(ent4_3), format_value(ent5_3)],
        [format_value(ent1_4), format_value(ent2_4), format_value(ent3_4), format_value(ent4_4), format_value(ent5_4)],
        [format_value(ent1_5), format_value(ent2_5), format_value(ent3_5), format_value(ent4_5), format_value(ent5_5)],
    ])
    targets = np.array([170, 180, 140, 180, 350]).reshape((5, 1))
    x = solve(data, targets)

    labels = ['Продукт 1', 'Продукт 2', 'Продукт 3', 'Продукт 4', 'Продукт 5']
    sizes = x.reshape(1, 5)[0].tolist()
    print(type(sizes))
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()
    #draw_plot(root, x, labels, colors)
    print(x)


def format_value(value):
    if value.get().isnumeric():
        formatted_value = int(value.get())
    else:
        formatted_value = 0
    return formatted_value


def draw_plot(tk_window, results, lbls, clrs):
    # the figure that will contain the plot
    fig = Figure(figsize=(5, 5),
                 dpi=100)

    # list of squares
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
    canvas.get_tk_widget().grid(row=6, column=2, sticky=W, pady=10)

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   tk_window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().grid(row=6, column=1, sticky=W, pady=10)


button_calc = Button(root, text="Рассчитать", command=calculate_proportion)
button_calc.grid(row=6, column=5, sticky=W, pady=10)

root.bind('<Escape>', lambda x: root.destroy())
root.mainloop()






'''
def make_ent(window, row_num, col_num):
    new_ent = Entry(window, width=10)
    new_ent.grid(row=row_num, column=col_num, sticky=W, pady=10)
    return new_ent.get()

proportion_list = []

for row in range(1, 6):
    row_list = []
    for column in range(0, 6):
        vitamine_num = make_ent(root, row, column)
        row_list.append(vitamine_num)
    proportion_list.append(row_list)
print(proportion_list)
'''#ent.pack()

#frame1 = Frame(root, width=100, height=100, bg="darkred")
#frame1['padding'] = (5, 10)
#frame1['borderwidth'] = 1
#frame1['relief'] = 'sunken'
#frame2 = Frame(root, width=100, height=100, bg="green")
#frame3 = Frame(root, width=100, height=100, bg="darkred")
#frame4 = Frame(root, width=100, height=100, bg="green")
#frame5 = Frame(root, width=100, height=100, bg="darkred")

#frame1.pack()
#frame2.pack()
#frame3.pack()
#frame4.pack()
#frame5.pack()


