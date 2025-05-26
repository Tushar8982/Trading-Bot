# Trading-Bot
A simplified Binance Futures trading bot using Python. Supports market and limit orders on the Binance USDT-M Testnet with CLI, logging, and error handling.

# 🤖 Binance Futures Trading Bot (Testnet)

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Made by Tushar8982](https://img.shields.io/badge/Made%20by-Tushar8982-blue)](https://github.com/Tushar8982)

A simplified crypto trading bot using Python to place Market and Limit orders on the Binance Futures USDT-M **Testnet**. The bot is fully interactive through a CLI, supports logging, error handling, and is structured for scalability.

---

## 🚀 Features

- ✅ Place **Market** and **Limit** orders
- ✅ Support for **BUY** and **SELL** orders
- ✅ Command-line input handling and validation
- ✅ Structured logs of all API interactions
- ✅ Environment variable support for secure credentials
- ✅ Modular, extensible codebase

---

## 📂 Project Structure

trading-bot/
├── bot.py # Main trading CLI
├── config.py # Loads API keys and creates Binance client
├── utils.py # Utility functions (place order, log, etc.)
├── .env # API_KEY and API_SECRET (do not share)
├── logs/ # Logs of trades and errors
├── requirements.txt # Python dependencies


---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Tushar8982/trading-bot.git
cd trading-bot

### 2. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt

3. Add Binance API Credentials
Create a .env file in the root directory:

API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
👉 You can register and generate API keys from the Binance Futures Testnet.

▶️ How to Run
Run the bot using:

python bot.py
Then follow the on-screen prompts to place an order:

Welcome to Binance Futures Bot
Enter symbol (e.g., BTCUSDT): BTCUSDT
Enter side (BUY/SELL): BUY
Enter order type (MARKET/LIMIT): MARKET
Enter quantity: 0.01

✅ Order placed successfully!
Order ID: 123456789
Status: FILLED
