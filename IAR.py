# Импорт необходимых библиотек
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

# Функция обновления метки с названием криптовалюты
def update_label(event):
    code = b_combobox.get()
    # Словарь соответствия символов и полных названий
    currencies_names = {
        "BTC": "Bitcoin", "ETH": "Ethereum", "USDT": "Tether", "BNB": "Binance Coin",
        "SOL": "Solana", "USDC": "USD Coin", "DOGE": "Dogecoin", "TRX": "TRON",
        "ADA": "Cardano", "LINK": "ChainLink", "HYPE": "Hyperliquid"
    }
    # Обновляем текст метки
    b_label.config(text=currencies_names.get(code, ""))

# Функция получения курса криптовалюты
def exchange():
    b_code = b_combobox.get()
    # Проверяем, выбрана ли криптовалюта
    if not b_code:
        mb.showwarning("Внимание", "Выберите криптовалюту")
        return
        
    try:
        # Запрос к API для получения данных о криптовалютах
        response = requests.get('https://api.coinlore.net/api/tickers/')
        response.raise_for_status()
        
        # Поиск выбранной криптовалюты в данных
        for crypto in response.json()['data']:
            if crypto['symbol'] == b_code:
                price = float(crypto['price_usd'])
                # Показываем курс в окне сообщения
                mb.showinfo("Курс", f"1 {crypto['symbol']} ({crypto['name']}) = ${price:.2f}")
                return
                
        # Если криптовалюта не найдена
        mb.showerror("Ошибка", f"Криптовалюта {b_code} не найдена")
    except Exception as e:
        # Обработка ошибок при запросе к API
        mb.showerror("Ошибка", f"Ошибка: {e}")

# Список доступных криптовалют
currencies = ["BTC", "ETH", "USDT", "BNB", "SOL", "USDC", "DOGE", "TRX", "ADA", "LINK", "HYPE"]

# Создание графического интерфейса
window = Tk()
window.title("Курс криптовалют")
window.geometry("300x240")

# Создание и размещение элементов интерфейса
Label(text="Криптовалюта:").pack(padx=10, pady=5)  # Заголовок
b_combobox = ttk.Combobox(values=currencies)  # Выпадающий список криптовалют
b_combobox.pack(padx=10, pady=5)
b_combobox.bind("<<ComboboxSelected>>", update_label)  # Привязка события выбора

b_label = ttk.Label()  # Метка для отображения названия криптовалюты
b_label.pack(padx=10, pady=5)

Button(text="Получить курс", command=exchange).pack(padx=10, pady=10)  # Кнопка запроса курса

# Запуск главного цикла приложения
window.mainloop()
