import tkinter as tk
from tkinter import ttk
from services.funcs_calc_app import *  # Убедитесь, что ваша функция расчета корректна

# Основное окно
gui_calc_ipoteka = tk.Tk()
gui_calc_ipoteka.geometry("600x300+100+200")
gui_calc_ipoteka.title("Калькулятор ипотеки")

# Текст для понимания
tk.Label(gui_calc_ipoteka, text="Введите процентную ставку (%)").grid(row=0, column=0, sticky="ew")
tk.Label(gui_calc_ipoteka, text="Введите Сумму ипотеки").grid(row=1, column=0, sticky="ew")
tk.Label(gui_calc_ipoteka, text="Введите Срок ипотеки(в Месяцах)").grid(row=2, column=0, sticky="ew")

# Колонки для ввода
field_procent_stavka = ttk.Entry(gui_calc_ipoteka)
field_summa_ipoteki = ttk.Entry(gui_calc_ipoteka)
field_srok_ipoteki = ttk.Entry(gui_calc_ipoteka)

# Визуал дизайна
field_procent_stavka.grid(row=0, column=1, sticky="w")
field_summa_ipoteki.grid(row=1, column=1, sticky="w")
field_srok_ipoteki.grid(row=2, column=1, sticky="w")
gui_calc_ipoteka.columnconfigure(0, weight=1, minsize=100)
gui_calc_ipoteka.columnconfigure(1, weight=1, minsize=100)
gui_calc_ipoteka.columnconfigure(2, weight=1, minsize=100)

# Поле для вывода результатов
result_text = tk.Text(gui_calc_ipoteka, height=10, width=40)
result_text.grid(row=5, column=0, columnspan=2, pady=10)

# Функция для обработки нажатия кнопки
def on_calculate():
    obshiDolg, mesyacniPlatezh, overpayment = func_calc_ipoteka(
        field_procent_stavka.get(),
        field_summa_ipoteki.get(),
        field_srok_ipoteki.get()
    )
    result_text.delete(1.0, tk.END)  # Очистка предыдущего результата
    result_text.insert(tk.END, f"Общий долг: {obshiDolg:.2f}\n")
    result_text.insert(tk.END, f"Месячный платеж: {mesyacniPlatezh:.2f}\n")
    result_text.insert(tk.END, f"Переплата: {overpayment:.2f}\n")

    field_procent_stavka.delete(0, tk.END)
    field_summa_ipoteki.delete(0, tk.END)
    field_srok_ipoteki.delete(0, tk.END)


button = tk.Button(gui_calc_ipoteka, text='Рассчитать', command=on_calculate)
button.grid(row=4, column=0, columnspan=2, sticky="ew")

gui_calc_ipoteka.mainloop()