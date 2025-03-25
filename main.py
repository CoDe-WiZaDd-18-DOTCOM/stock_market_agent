from fastapi import FastAPI
from stock_service import get_stock_price
# from ai_agent import analyze_stock

app = FastAPI()

@app.get("/stock/{ticker}")
async def get_stock_info(ticker: str):
    stock_price = get_stock_price(ticker)
    if stock_price is None:
        return {"error": "Stock not found"}

    # recommendation = analyze_stock(stock_price)
    return {
        "ticker": ticker.upper(),
        "price": stock_price,
        "recommendation": "currently its not implemented as using ai agent is not free..."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
