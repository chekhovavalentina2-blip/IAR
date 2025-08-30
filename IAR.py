from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_label(event):
    code = b_combobox.get()
    currencies_names = {
        "BTC": "Bitcoin", "ETH": "Ethereum", "USDT": "Tether", "BNB": "Binance Coin",
        "SOL": "Solana", "USDC": "USD Coin", "DOGE": "Dogecoin", "TRX": "TRON",
        "ADA": "Cardano", "LINK": "ChainLink", "HYPE": "Hyperliquid"
    }
    b_label.config(text=currencies_names.get(code, ""))

def exchange():
    b_code = b_combobox.get()
    if not b_code:
        mb.showwarning("Внимание", "Выберите криптовалюту")
        return
        
    try:
        response = requests.get('https://api.coinlore.net/api/tickers/')
        response.raise_for_status()
        
        for crypto in response.json()['data']:
            if crypto['symbol'] == b_code:
                price = float(crypto['price_usd'])
                mb.showinfo("Курс", f"1 {crypto['symbol']} ({crypto['name']}) = ${price:.2f}")
                return
                
        mb.showerror("Ошибка", f"Криптовалюта {b_code} не найдена")
    except Exception as e:
        mb.showerror("Ошибка", f"Ошибка: {e}")

currencies = ["BTC", "ETH", "USDT", "BNB", "SOL", "USDC", "DOGE", "TRX", "ADA", "LINK", "HYPE"]

# Создание графического интерфейса
window = Tk()
window.title("Курс криптовалют")
window.geometry("300x240")

Label(text="Криптовалюта:").pack(padx=10, pady=5)
b_combobox = ttk.Combobox(values=currencies)
b_combobox.pack(padx=10, pady=5)
b_combobox.bind("<<ComboboxSelected>>", update_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=5)

Button(text="Получить курс", command=exchange).pack(padx=10, pady=10)

window.mainloop()
