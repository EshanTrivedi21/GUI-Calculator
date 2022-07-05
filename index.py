from tkinter import *

root = Tk()
root.title("GUI Calculator")
root.configure(background='#212121')

e = Entry(root, width=26, borderwidth=5, bg="#2b292a", fg="#fff", font = ('courier', 15, 'bold'))
e.grid(row=0, column=0, columnspan=4, pady=14, padx=4, ipady=10)

button_1 = Button(root, text=1, borderwidth=1, padx=25, pady=10, bg="#343434", fg="#fff", font = ('courier', 15, 'bold'))
button_2 = Button(root, text=2, borderwidth=1, padx=25, pady=10, bg="#343434", fg="#fff", font = ('courier', 15, 'bold'))
button_3 = Button(root, text=3, borderwidth=1, padx=25, pady=10, bg="#343434", fg="#fff", font = ('courier', 15, 'bold'))
button_4 = Button(root, text=4, borderwidth=1, padx=25, pady=10, bg="#343434", fg="#fff", font = ('courier', 15, 'bold'))
button_5 = Button(root, text=5, borderwidth=1, padx=25, pady=10, bg="#343434", fg="#fff", font = ('courier', 15, 'bold'))
button_6 = Button(root, text=6, borderwidth=1, padx=25, pady=10, bg="#343434", fg="#fff", font = ('courier', 15, 'bold'))
button_7 = Button(root, text=7, borderwidth=1, padx=25, pady=10, bg="#343434", fg="#fff", font = ('courier', 15, 'bold'))
button_8 = Button(root, text=8, borderwidth=1, padx=25, pady=10, bg="#343434", fg="#fff", font = ('courier', 15, 'bold'))
button_9 = Button(root, text=9, borderwidth=1, padx=25, pady=10, bg="#343434", fg="#fff", font = ('courier', 15, 'bold'))
button_0 = Button(root, text=0, borderwidth=1, padx=25, pady=10, bg="#343434", fg="#fff", font = ('courier', 15, 'bold'))

button_add = Button(root, text= "+", borderwidth=1, padx=25, pady=10, bg="#1a454f", font = ('courier', 15, 'bold'))
button_subtract = Button(root, text= "-", borderwidth=1, padx=25, pady=10, bg="#1a454f", font = ('courier', 15, 'bold'))
button_divide = Button(root, text= "/", borderwidth=1, padx=25, pady=10, bg="#1a454f", font = ('courier', 15, 'bold'))
button_multiply = Button(root, text= "*", borderwidth=1, padx=25, pady=10, bg="#1a454f", font = ('courier', 15, 'bold'))

button_equals = Button(root, text= "=", borderwidth=1, padx=25, pady=10, bg="#77dd77", font = ('courier', 15, 'bold'))
button_clear = Button(root, text= "C", borderwidth=1, padx=25, pady=10, bg="#ff6961", font = ('courier', 15, 'bold'))

button_1.grid(row=3, column=0, pady=5)
button_2.grid(row=3, column=1, pady=5)
button_3.grid(row=3, column=2, pady=5)
button_add.grid(row=3, column=3, pady=5)

button_4.grid(row=2, column=0, pady=5)
button_5.grid(row=2, column=1, pady=5)
button_6.grid(row=2, column=2, pady=5)
button_subtract.grid(row=2, column=3, pady=5)

button_7.grid(row=1, column=0, pady=5)
button_8.grid(row=1, column=1, pady=5)
button_9.grid(row=1, column=2, pady=5)
button_divide.grid(row=1, column=3, pady=5)

button_clear.grid(row=4, column=0, pady=5)
button_0.grid(row=4, column=1, pady=5)
button_equals.grid(row=4, column=2, pady=5)
button_multiply.grid(row=4, column=3, pady=5)

root.mainloop()