from pydantic import BaseModel
from typing import Optional

class Order(BaseModel):
    id: Optional[int] = None
    customer_name: str
    product: str
    quantity: int
    total_price: float


class OrderCreate(BaseModel):
    customer_name: str
    product: str
    quantity: int
