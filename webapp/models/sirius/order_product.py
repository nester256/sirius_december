from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from webapp.models.meta import Base


class OrderProduct(Base):
    __tablename__ = 'order_product'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    order_id: Mapped[int] = mapped_column(Integer, ForeignKey('order.id'), nullable=False)

    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('product.id'), nullable=False)

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
