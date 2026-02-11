from fastapi import APIRouter
from app.application.order_service import OrderService
from app.domain.order import Order, OrderCreate
from typing import List

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("/", response_model=List[Order])
def get_orders():
    return OrderService.get_orders()


@router.post("/", response_model=Order)
def create_order(order: OrderCreate):
    return OrderService.create_order(order)
