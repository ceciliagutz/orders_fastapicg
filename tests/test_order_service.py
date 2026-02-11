from app.application.order_service import OrderService
from app.domain.order import OrderCreate, Order


class FakeOrderRepository:
    def __init__(self):
        self.orders = []
        self.next_id = 1

    def get_all(self):
        return self.orders

    def get_by_id(self, order_id: int):
        for o in self.orders:
            if o.id == order_id:
                return o
        return None

    def create(self, order: Order):
        order.id = self.next_id
        self.next_id += 1
        self.orders.append(order)
        return order

    def update(self, order_id: int, order: Order):
        for i, o in enumerate(self.orders):
            if o.id == order_id:
                order.id = order_id
                self.orders[i] = order
                return order
        return None

    def delete(self, order_id: int):
        for i, o in enumerate(self.orders):
            if o.id == order_id:
                del self.orders[i]
                return True
        return False


def test_create_order():
    # Arrange
    fake_repo = FakeOrderRepository()
    OrderService.repository = fake_repo

    order_data = OrderCreate(
        customer_name="Cecilia",
        product="Album ARIRANG",
        quantity=3
    )

    # Act
    order = OrderService.create_order(order_data)

    # Assert
    assert order.id == 1
    assert order.total_price == 300
    assert order.customer_name == "Cecilia"
