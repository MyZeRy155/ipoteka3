import tkinter as tkgui
from tkinter import ttk, messagebox


from repository.ipoteka import *
from services import mortgage_calculation

class AuthWindow:
    def __init__(self, auth_root):
        self.root = auth_root
        self.auth_window = tkgui.Toplevel(auth_root)
        self.auth_window.title("Авторизация")

        # Поле для логина
        tkgui.Label(self.auth_window, text="Логин:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_username = ttk.Entry(self.auth_window)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        # Поле для пароля
        tkgui.Label(self.auth_window, text="Пароль:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_password = ttk.Entry(self.auth_window, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        # Кнопка авторизации
        tkgui.Button(self.auth_window, text="Войти", command=self.login).grid(row=2, column=0, padx=10, pady=10)

        # Кнопка перехода к регистрации
        tkgui.Button(self.auth_window, text="Зарегистрироваться", command=self.open_registration).grid(row=2, column=1, padx=10, pady=10)

    def login(self):
        bool_flag = login_in(self.entry_username.get(), self.entry_password.get())
        if not bool_flag:
            messagebox.showerror(title="Ошибка", message="Неверный логин или пароль")
        else:
            messagebox.showinfo(title="Авторизация", message="Авторизация прошла успешно!")
            self.auth_window.destroy()  # Закрыть окно авторизации
            calc_window = CalcMortgageInterface(tkgui.Tk())
            calc_window.root.mainloop()



    def open_registration(self):
        self.auth_window.destroy()  # Закрыть окно авторизации

        RegistrationWindow(self.root)  # Открыть окно регистрации


class RegistrationWindow:
    def __init__(self, register_root):
        self.root = register_root
        self.registration_window = tkgui.Toplevel(register_root)
        self.registration_window.title("Регистрация")

        # Поле для логина
        tkgui.Label(self.registration_window, text="Логин:").grid(row=0,
                                                                  column=0,
                                                                  padx=10,
                                                                  pady=10)
        self.entry_username = ttk.Entry(self.registration_window)
        self.entry_username.grid(row=0,
                                 column=1,
                                 padx=10,
                                 pady=10)
        # Поле для пароля
        tkgui.Label(self.registration_window, text="Пароль:").grid(row=1,
                                                                  column=0,
                                                                  padx=10,
                                                                  pady=10)
        self.entry_password = ttk.Entry(self.registration_window)
        self.entry_password.grid(row=1,
                                 column=1,
                                 padx=10,
                                 pady=10)
        tkgui.Button(self.registration_window, text="Зарегистрироваться", command=self.registration).grid(row=2,
                                                                               column=0,
                                                                               columnspan=2,
                                                                               padx=10,
                                                                               pady=10)

    def registration(self):
        register(self.entry_username.get(),self.entry_password.get())
        self.registration_window.destroy()  # Закрыть окно авторизации
        AuthWindow(self.root)


class CalcMortgageInterface:
    def __init__(self, root3):
        self.root = root3
        self.root.geometry("600x300+100+200")
        self.root.title("Калькулятор ипотеки")

        # Текст для понимания
        tkgui.Label(self.root, text="Введите процентную ставку (%)").grid(row=0, column=0, sticky="ew")
        tkgui.Label(self.root, text="Введите Сумму ипотеки").grid(row=1, column=0, sticky="ew")
        tkgui.Label(self.root, text="Введите Срок ипотеки(в Месяцах)").grid(row=2, column=0, sticky="ew")

        # Колонки для ввода
        self.field_interest_rate = ttk.Entry(self.root) ## Поле процентной ставки
        self.field_mortgage_amount = ttk.Entry(self.root) ## Поле суммы ипотеки
        self.field_mortgage_term = ttk.Entry(self.root) ## Поле срока ипотеки

        # Визуал дизайна
        self.field_interest_rate.grid(row=0, column=1, sticky="w")
        self.field_mortgage_amount.grid(row=1, column=1, sticky="w")
        self.field_mortgage_term.grid(row=2, column=1, sticky="w")
        self.root.columnconfigure(0, weight=1, minsize=100)
        self.root.columnconfigure(1, weight=1, minsize=100)
        self.root.columnconfigure(2, weight=1, minsize=100)

        # Поле для вывода результатов
        self.result_text = tkgui.Text(self.root, height=10, width=40)
        self.result_text.grid(row=5, column=0, columnspan=2, pady=10)

        # Кнопка расчета
        self.calculate_button = tkgui.Button(self.root, text="Рассчитать", command=self.on_calculate)
        self.calculate_button.grid(row=4, column=0, columnspan=2, sticky="ew")

    def on_calculate(self):
        interest_rate = float(self.field_interest_rate.get()) ## Процентная ставка
        mortgage_amount = float(self.field_mortgage_amount.get()) ## Сумма ипотеки
        mortgage_term = int(self.field_mortgage_term.get()) ## Срок ипотеки

        monhly_payment, total_debt, overpayment = mortgage_calculation(
            interest_rate, mortgage_amount, mortgage_term
        )
        ## Вывод результатов
        self.result_text.delete(1.0, tkgui.END)  # Очистка предыдущего результата
        self.result_text.insert(tkgui.END, f"Общий долг: {total_debt:.2f}\n")
        self.result_text.insert(tkgui.END, f"Месячный платеж: {monhly_payment:.2f}\n")
        self.result_text.insert(tkgui.END, f"Переплата: {overpayment:.2f}\n")
        ## Очистка полей
        self.field_interest_rate.delete(0, tkgui.END)
        self.field_mortgage_amount.delete(0, tkgui.END)
        self.field_mortgage_term.delete(0, tkgui.END)


if __name__ == "__main__":
    root = tkgui.Tk()
    root.withdraw()
    auth_window = AuthWindow(root)
    root.mainloop()