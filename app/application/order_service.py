from app.infraestructure.order_repository import OrderRepository
from typing import List
from app.domain.order import Order, OrderCreate, OrderUpdate
from app.domain.order_repository_port import OrderRepositoryPort
from app.infraestructure.order_repository import OrderRepository

class OrderService:
    repository: OrderRepositoryPort =OrderRepository()

    @staticmethod
    def get_orders() -> List[Order]:
        return OrderService.repository.get_all()

    @staticmethod
    def create_order(order_data: OrderCreate) -> Order:
        price_per_unit = 100

        total_price = order_data.quantity * price_per_unit

        order = Order(
            customer_name=order_data.customer_name,
            product=order_data.product,
            quantity=order_data.quantity,
            total_price=total_price
        )

        return OrderService.repository.create(order)
    
    @staticmethod
    def get_order_by_id(order_id: int) -> Order | None:
        return OrderService.repository.get_by_id(order_id)
    
    @staticmethod
    def update_order(order_id: int, order_data: OrderUpdate) -> Order | None:
        price_per_unit = 100
        total_price = order_data.quantity * price_per_unit

        order = Order(
            customer_name=order_data.customer_name,
            product=order_data.product,
            quantity=order_data.quantity,
            total_price=total_price
        )

        return OrderService.repository.update(order_id, order)

    @staticmethod
    def delete_order(order_id: int) -> bool:
        return OrderService.repository.delete(order_id)