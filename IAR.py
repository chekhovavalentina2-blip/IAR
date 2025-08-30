from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_b_label(event):
    # Получаем полное название базовой криптовалюты из словаря и обновляем метку
    code = b_combobox.get()
    name = currencies[code]
    b_label.config(text=name)

def exchange():
    b_code = b_combobox.get()

    if b_code:
        try:
            response = requests.get('https://api.coinlore.net/api/tickers/')
            response.raise_for_status()

            data = response.json()['data']
            
            # Ищем криптовалюту по символу
            crypto_data = None
            for crypto in data:
                if crypto['symbol'] == b_code:
                    crypto_data = crypto
                    break
            
            if crypto_data:
                price_usd = float(crypto_data['price_usd'])
                symbol = crypto_data['symbol']
                name = crypto_data['name']
                
                mb.showinfo("Курс обмена", f"Курс {symbol} ({name}): ${price_usd:.2f}")
            else:
                mb.showerror("Ошибка", f"Криптовалюта {b_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды криптовалют")

# Словарь кодов валют и их полных названий
currencies = {
    "BTC": "Bitcoin",
    "ETH": "Ethereum",
    "USDT": "Tether",
    "BNB": "Binance Coin",
    "SOL": "Solana",
    "USDC": "USD Coin",
    "DOGE": "Dogecoin",
    "TRX": "TRON",
    "ADA": "Cardano",
    "LINK": "ChainLink",
    "HYPE": "Hyperliquid"
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

Button(text="Получить курс", command=exchange).pack(padx=10, pady=10)

window.mainloop()
