from sqlalchemy.orm import Session
from app.domain.order import Order
from app.infraestructure.database import SessionLocal
from app.infraestructure.order_model import OrderModel
from typing import List


class OrderRepository:

    @staticmethod
    def get_all() -> List[Order]:
        db: Session = SessionLocal()
        orders = db.query(OrderModel).all()
        db.close()

        return [
            Order(
                id=o.id,
                customer_name=o.customer_name,
                product=o.product,
                quantity=o.quantity,
                total_price=o.total_price
            )
            for o in orders
        ]

    @staticmethod
    def create(order: Order) -> Order:
        db: Session = SessionLocal()

        db_order = OrderModel(
            customer_name=order.customer_name,
            product=order.product,
            quantity=order.quantity,
            total_price=order.total_price
        )

        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        db.close()

        return Order(
            id=db_order.id,
            customer_name=db_order.customer_name,
            product=db_order.product,
            quantity=db_order.quantity,
            total_price=db_order.total_price
        )
    @staticmethod
    def get_by_id(order_id: int) -> Order | None:
        db: Session = SessionLocal()

        db_order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
        db.close()

        if not db_order:
            return None

        return Order(
            id=db_order.id,
            customer_name=db_order.customer_name,
            product=db_order.product,
            quantity=db_order.quantity,
            total_price=db_order.total_price
        )

