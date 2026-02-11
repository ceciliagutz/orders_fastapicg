from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.order import Order


class OrderRepositoryPort(ABC):

    @abstractmethod
    def get_all(self) -> List[Order]:
        pass

    @abstractmethod
    def get_by_id(self, order_id: int) -> Optional[Order]:
        pass

    @abstractmethod
    def create(self, order: Order) -> Order:
        pass

    @abstractmethod
    def update(self, order_id: int, order: Order) -> Optional[Order]:
        pass

    @abstractmethod
    def delete(self, order_id: int) -> bool:
        pass
