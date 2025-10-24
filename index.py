import tkinter as tk

window = tk.Tk()

label1 = tk.Label(window, text="Объединение 2 колонки", bg="lightblue")
label2 = tk.Label(window, text="Обычная ячейка", bg="lightgreen")
label3 = tk.Label(window, text="Объединение 2 строки", bg="lightyellow")

label1.grid(row=0, column=0, columnspan=2)  # Занимает 2 колонки
label2.grid(row=1, column=1)               # Обычная ячейка
label3.grid(row=1, column=0, rowspan=2)    # Занимает 2 строки

window.mainloop()