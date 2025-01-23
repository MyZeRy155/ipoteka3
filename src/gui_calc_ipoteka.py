import tkinter as tk
from tkinter import ttk
from services import process_ipoteka_data

class MainInterface:
    def __init__(self):
        ## Основное окно
        self.root = tk.Tk()
        self.root.geometry("600x300+100+200")
        self.root.title("Калькулятор ипотеки")

        # Текст для понимания
        tk.Label(self.root, text="Введите процентную ставку (%)").grid(row=0, column=0, sticky="ew")
        tk.Label(self.root, text="Введите Сумму ипотеки").grid(row=1, column=0, sticky="ew")
        tk.Label(self.root, text="Введите Срок ипотеки(в Месяцах)").grid(row=2, column=0, sticky="ew")

        # Колонки для ввода
        self.field_procent_stavka = ttk.Entry(self.root)
        self.field_summa_ipoteki = ttk.Entry(self.root)
        self.field_srok_ipoteki = ttk.Entry(self.root)

        # Визуал дизайна
        self.field_procent_stavka.grid(row=0, column=1, sticky="w")
        self.field_summa_ipoteki.grid(row=1, column=1, sticky="w")
        self.field_srok_ipoteki.grid(row=2, column=1, sticky="w")
        self.root.columnconfigure(0, weight=1, minsize=100)
        self.root.columnconfigure(1, weight=1, minsize=100)
        self.root.columnconfigure(2, weight=1, minsize=100)

        # Поле для вывода результатов
        self.result_text = tk.Text(self.root, height=10, width=40)
        self.result_text.grid(row=5, column=0, columnspan=2, pady=10)

        # Кнопка расчета
        self.calculate_button = tk.Button(self.root, text="Рассчитать", command=self.on_calculate)
        self.calculate_button.grid(row=4, column=0, columnspan=2, sticky="ew")

    def on_calculate(self):
        procent_stavka = float(self.field_procent_stavka.get())
        summa_ipoteki = float(self.field_summa_ipoteki.get())
        srok_ipoteki = int(self.field_srok_ipoteki.get())

        mesyacni_platezh, obshi_dolg, overpayment = process_ipoteka_data(
            procent_stavka, summa_ipoteki, srok_ipoteki
        )
        ## Вывод результатов
        self.result_text.delete(1.0, tk.END)  # Очистка предыдущего результата
        self.result_text.insert(tk.END, f"Общий долг: {obshi_dolg:.2f}\n")
        self.result_text.insert(tk.END, f"Месячный платеж: {mesyacni_platezh:.2f}\n")
        self.result_text.insert(tk.END, f"Переплата: {overpayment:.2f}\n")
        ## Очистка полей
        self.field_procent_stavka.delete(0, tk.END)
        self.field_summa_ipoteki.delete(0, tk.END)
        self.field_srok_ipoteki.delete(0, tk.END)

if __name__ == "__main__":
    main_interface = MainInterface()
    main_interface.root.mainloop()