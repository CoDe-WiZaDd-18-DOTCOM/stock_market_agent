# Stock Market AI Agent

## 📌 Overview
This project provides an API to fetch real-time stock market prices and analyze trends using AI.

## 🚀 Features
- Fetch the latest stock prices.
- AI-powered stock recommendations (coming soon).
- FastAPI-based public API.

## 🔧 Installation

### Prerequisites:
- Python 3.8+
- `pip` (Python package manager)

### Steps:
1. Clone this repository:
git clone https://github.com/CoDe-WiZaDd-18-DOTCOM/stock-market-agent.git cd stock-market-agent

2. Install dependencies:
pip install -r requirements.txt

3. Run the API server:
uvicorn main:app --reload

Test the API using cURL or Postman:
curl -X GET "https://stock-market-agent.onrender.com/stock/{stock_name}" 

## 📜 API Endpoints
| Method | Endpoint             | Description                      |
|--------|----------------------|----------------------------------|
| GET    | `/stock/{ticker}`    | Fetch stock price for a ticker  |

## 📦 Dependencies
- FastAPI
- Requests
- Uvicorn
