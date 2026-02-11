from fastapi import APIRouter
from app.application.order_service import OrderService
from app.domain.order import Order, OrderCreate
from typing import List
from fastapi import HTTPException
from app.domain.order import Order, OrderCreate, OrderUpdate

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("/", response_model=List[Order])
def get_orders():
    return OrderService.get_orders()

@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int):
    order = OrderService.get_order_by_id(order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


@router.post("/", response_model=Order)
def create_order(order: OrderCreate):
    return OrderService.create_order(order)

@router.put("/{order_id}", response_model=Order)
def update_order(order_id: int, order: OrderUpdate):
    updated_order = OrderService.update_order(order_id, order)

    if not updated_order:
        raise HTTPException(status_code=404, detail="Order not found")

    return updated_order

@router.delete("/{order_id}")
def delete_order(order_id: int):
    success = OrderService.delete_order(order_id)

    if not success:
        return {"message": "Order not found"}

    return {"message": "Order deleted successfully"}
