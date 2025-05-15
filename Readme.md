# Crypto Trading Bot — Binance Futures Testnet

A Python-based crypto trading bot for Binance Futures Testnet, supporting market, limit, stop-limit, and simulated OCO orders with both CLI and Flask web UI.

## 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)  
- [📋 Project Overview](#-project-overview)  
- [✨ Features](#-features)  
- [🔧 Prerequisites](#-prerequisites)  
- [🛠️ Installation](#️-installation)  
- [⚙️ Configuration](#️-configuration)  
- [📈 Usage](#-usage)  
  - [Command-Line Interface (CLI)](#command-line-interface-cli)  
  - [Flask Web UI](#flask-web-ui)  
- [📊 Supported Order Types](#-supported-order-types)  
- [📝 Logging](#-logging)  
- [❓ Troubleshooting](#-troubleshooting)  
- [📁 Project Structure](#-project-structure)  
- [📌 Notes](#-notes)  
- [📄 License](#-license)  
- [📧 Contact](#-contact)  

## 📋 Project Overview

This project implements a crypto trading bot for Binance Futures Testnet that allows placing market, limit, stop-limit, and simulated OCO (One-Cancels-the-Other) orders. The bot provides both a command-line interface (CLI) and a responsive Flask web interface for user-friendly order management.

The bot uses the official Binance REST API and handles order status checks and robust logging.

## ✨ Features

- Place **Market**, **Limit**, **Stop-Limit** (Stop-Market) orders  
- Simulate **OCO orders** by placing linked limit and stop-market orders  
- CLI with input validation and order status checking  
- Flask UI with dynamic form inputs and Bootstrap styling  
- Logging of API calls and errors to `logs/bot.log`  
- Fully tested on Binance Futures Testnet  

## 🔧 Prerequisites

- Python 3.8+  
- Binance Futures Testnet account with API key and secret  
- Basic familiarity with Python CLI and Flask  

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/fuzail-pixel/crypto_trading_bot.git
   cd crypto_trading_bot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

1. Create a `.env` file in the project root with your Binance Futures Testnet API credentials (this file will not be pushed to the repository):
   ```
   API_KEY=your_testnet_api_key
   API_SECRET=your_testnet_api_secret
   TESTNET=True
   ```

2. Make sure your API key has **Futures trading enabled** on Binance Testnet.

## 📈 Usage

### Command-Line Interface (CLI)

Run orders or check status directly via CLI commands:

* **Place a market order:**
  ```bash
  python -m app.cli order --symbol BTCUSDT --side buy --type market --quantity 0.001
  ```

* **Place a limit order:**
  ```bash
  python -m app.cli order --symbol BTCUSDT --side sell --type limit --quantity 0.001 --price 95000
  ```

* **Place a stop-limit order:**
  ```bash
  python -m app.cli order --symbol BTCUSDT --side sell --type stop_limit --quantity 0.002 --stop-price 95000
  ```

* **Place a simulated OCO order:**
  ```bash
  python -m app.cli order --symbol BTCUSDT --side sell --type oco --quantity 0.002 --take-profit 110000 --stop-loss 95000
  ```

* **Check order status:**
  ```bash
  python -m app.cli status --symbol BTCUSDT --order-id 123456789
  ```

### Flask Web UI

1. Start the Flask app:
   ```bash
   python main.py
   ```

2. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

3. Use the form to place orders of any supported type and view real-time responses.

## 📊 Supported Order Types

| Order Type      | Description                                           | CLI `--type` value |
| --------------- | ----------------------------------------------------- | ------------------ |
| Market          | Immediate execution at market price                   | `market`           |
| Limit           | Order placed at specific price                        | `limit`            |
| Stop-Limit      | Stop-market order triggers market order at stop price | `stop_limit`       |
| OCO (Simulated) | Two orders: Limit take-profit + Stop-market stop-loss | `oco`              |

## 📝 Logging

* Logs are stored in `logs/bot.log`.
* Logs include API request details, responses, and error messages.
* Useful for debugging and auditing trades.

## ❓ Troubleshooting

* Ensure your API key is enabled for Futures trading on Binance Testnet.
* Make sure order quantities meet Binance minimum notional and step size requirements.
* Check `logs/bot.log` for detailed error information.
* If Flask UI fails to load, verify Flask installation and environment activation.

## 📁 Project Structure

```
crypto_trading_bot/
│
├── app/
│   ├── __init__.py
│   ├── bot.py           # Core trading bot logic with Binance API integration
│   ├── cli.py           # Command-line interface for placing orders & checking status
│   ├── config.py        # Loads environment variables (API keys, testnet flag)
│   ├── logger.py        # Logger setup writing to logs/bot.log
│   ├── routes.py        # Flask route handlers for web UI
│
├── templates/
│   └── index.html       # Flask HTML template with Bootstrap-enhanced order form
│
├── main.py              # Flask app entry point
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── .gitignore           # Git ignore file
```

### Files not included in repository:
- `.env` - Environment variables file with API keys
- `logs/bot.log` - Generated log files
- `venv/` - Python virtual environment

## 📌 Notes

* This bot works exclusively on Binance Futures **Testnet**.
* Real Binance Futures **does not support native OCO orders**, so OCO is simulated by placing two linked orders.
* WebSocket live tracking is **not implemented** but can be added in future enhancements.
* The `logs/` directory will be created automatically when the bot runs, but won't be included in the repository.

## 📄 License

This project is licensed under the GPL-3.0 License.

## 📧 Contact

Feel free to reach out on [LinkedIn](https://linkedin.com/in/fuzail-rehman-31a755241/) or [GitHub](https://github.com/fuzail-pixel) if you have any questions or feedback.

---

Thanks for using the Crypto Trading Bot! 🚀