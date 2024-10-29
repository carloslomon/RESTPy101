import fastapi as fp 
from uuid import uuid4
from typing import Optional, List
from models import Stock, stock_status
app = fp.FastAPI()

db_portfolio1: List[Stock] = [
    Stock(
        id=uuid4(),
        company_name="NVIDIA Corporation",
        stock_ticker="NVDA",
        price=140.33,
        change=-0.01,
        stock_status=stock_status.hold
        ),
    Stock(
        id=uuid4(),
        company_name="First Solar Incorporated",
        stock_ticker="FSLR",
        price=223.46,
        change=0.1537,
        stock_status=stock_status.buy
        ),
        Stock(
        id=uuid4(),
        company_name="AMC Entertainment Holdings Incorporated",
        stock_ticker="AMC",
        price=4.44,
        change=0.0278,
        stock_status=stock_status.sell
        )
]


def foo()-> dict:
    return {"Foo":"My Foo"}
@app.get("/") #the backslash just signifies we are getting the root 
async def root():
    foo()
    return {"Name": "Carlos"}

@app.get("/portfolio1")
async def fetch_portfolio1_stocks():
    return db_portfolio1

@app.post("/portfolio1")
async def buy_stock_portfolio1(stock: Stock):
    db_portfolio1.append(stock)
    return {"id": stock.id}
"""
Use the json body below as a post template

"""

"""
{
    "company_name": "Microsoft",
    "stock_ticker": "MSFT",
    "price": 426.56,
    "change": -0.0156,
    "stock_status": "hold"
 }
"""
@app.delete("/portfolio1/{stock_tck}")
async def sell_stock_portfolio1(stock_tck: str):
    
    for stock in db_portfolio1:
        if stock.stock_ticker == stock_tck:
            tmp = stock
            db_portfolio1.remove(stock)
            return tmp
    raise fp.HTTPException(
        status_code=404,
        detail=f"The stock with ticker {stock_tck} is not in portfolio 1"
    )

