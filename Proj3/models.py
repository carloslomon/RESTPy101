import pydantic as pydan
from typing import Optional, List 
from uuid import UUID, uuid4
import uuid 
from enum import Enum



class stock_status(str, Enum):
    sell = "sell"
    hold = "hold"
    buy = "buy"

class Stock(pydan.BaseModel):
    id: Optional[UUID] = pydan.Field(default_factory=uuid4)
    company_name: str
    stock_ticker: str 
    comments: Optional[str]
    price: float
    change: float
    stock_status: stock_status






