# 🤖 Binance Futures Trading Bot (Testnet)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Made by Tushar8982](https://img.shields.io/badge/Made%20by-Tushar8982-blue)](https://github.com/Tushar8982)

A simplified crypto trading bot built in Python for the Binance USDT-M Futures **Testnet**. This bot allows you to place real-time **Market** and **Limit** orders via a clean and interactive CLI. It also features structured logging, error handling, and a modular codebase ready for future improvements.

---

## ⚙️ Features

- ✅ Place **Market** and **Limit** orders  
- ✅ Support both **BUY** and **SELL** sides  
- ✅ Command-line interface (CLI) for easy user interaction  
- ✅ Input validation & error handling  
- ✅ Logging of API requests, responses, and errors  
- ✅ Environment-based credential management  
- ✅ Modular code structure  

---

## 🗂 Project Structure

```
trading-bot/
├── bot.py             # Main trading interface
├── config.py          # Loads API keys and sets up Binance client
├── utils.py           # Order placement, logging, and helpers
├── .env               # Contains API_KEY and API_SECRET (do NOT share)
├── logs/              # Logs of all API requests and errors
├── requirements.txt   # Python dependencies
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Tushar8982/trading-bot.git
cd trading-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root with your Binance **Testnet** credentials:

```env
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```

> 💡 You can register and get your API key at [Binance Futures Testnet](https://testnet.binancefuture.com/)

---

## ▶️ How to Run

```bash
python bot.py
```

You'll be prompted for:

- Trading symbol (e.g., `BTCUSDT`)  
- Side (`BUY` or `SELL`)  
- Order type (`MARKET` or `LIMIT`)  
- Quantity  

Sample CLI interaction:

```
Welcome to Binance Futures Bot
Enter symbol (e.g., BTCUSDT): BTCUSDT
Enter side (BUY/SELL): BUY
Enter order type (MARKET/LIMIT): MARKET
Enter quantity: 0.01

✅ Order placed successfully!
Order ID: 12345678
Status: FILLED
```

---

## 💡 Optional Enhancements

> These are **bonus features** that you can add:

- Add **Stop-Limit**, **OCO**, or **TWAP** order types  
- Build a simple frontend or enhanced CLI  
- Integrate WebSocket for live data and updates  
- Add order status tracking and trade history  

---

## 📬 How to Apply

Send the following to **chetan@primetrade.ai** and **sonika@primetrade.ai**:

- ✅ GitHub repo link  
- ✅ Log files from the `/logs` folder  
- ✅ Your updated resume  

**Email Subject:**  
`Junior Python Developer – Crypto Trading Bot`

> 🕒 Pro tip: Apply within the first 72 hours for a better chance of selection. First come, first serve!

---

## 🧠 Ideal For

- Recent graduates  
- Python developers & automation enthusiasts  
- Bootcamp grads and crypto-native learners  
- Anyone passionate about finance + code  

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## 🙌 Connect

**Made with 💻 by [Tushar8982](https://github.com/Tushar8982)**  
Feel free to ⭐️ the repo if you find it useful!
