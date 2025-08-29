from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_b_label(event):
    # Получаем полное название базовой криптовалюты из словаря и обновляем метку
    code = b_combobox.get()
    name = currencies[code]
    b_label.config(text=name)

def update_t_label(event):
    # Получаем полное название целевой криптовалюты из словаря и обновляем метку
    code = t_combobox.get()
    name = currencies[code]
    t_label.config(text=name)

def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()

    if t_code and b_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status()

            data = response.json()

            if t_code in data['rates']:
                exchange_rate = data['rates'][t_code]
                base = currencies[b_code]
                target = currencies[t_code]
                mb.showinfo("Курс обмена", f"Курс {exchange_rate:.1f} {target} за 1 {base}")
            else:
                mb.showerror("Ошибка", f"Валюта {t_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")

# Словарь кодов валют и их полных названий
currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена криптовалюты")
window.geometry("360x300")

Label(text="Базовая криптовалюта:").pack(padx=10, pady=5)
b_combobox = ttk.Combobox(values=list(currencies.keys()))
b_combobox.pack(padx=10, pady=5)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Целевая криптовалюта:").pack(padx=10, pady=5)
t_combobox = ttk.Combobox(values=list(currencies.keys()))
t_combobox.pack(padx=10, pady=5)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
