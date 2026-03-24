from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.sql import func

from database.base import Base
from .car import Car
from .user import User


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    car_description: Mapped[str] = mapped_column(String(1000), nullable=False)
    phone: Mapped[str] = mapped_column(String(50), nullable=False)

    car_id: Mapped[int] = mapped_column(
        ForeignKey("cars.id"),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship(User)
    car = relationship(Car)