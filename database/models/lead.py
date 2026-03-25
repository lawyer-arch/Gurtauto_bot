from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime, LargeBinary

from sqlalchemy.sql import func

from database.base import Base
from .user import User


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )
    phone: Mapped[str] = mapped_column(String(50), nullable=True)
    marka: Mapped[str] = mapped_column(String(100), nullable=True)
    model: Mapped[str] = mapped_column(String(100), nullable=True)
    color: Mapped[str] = mapped_column(String(100), nullable=True)

    engine: Mapped[str] = mapped_column(String(100), nullable=True)
    drive: Mapped[str] = mapped_column(String(20), nullable=True)
    fuel: Mapped[str] = mapped_column(String(50), nullable=True)

    mileage: Mapped[str] = mapped_column(String(50), nullable=True)
    year: Mapped[str] = mapped_column(String(50), nullable=True)

    budget: Mapped[str] = mapped_column(String(100), nullable=True)
    repairs: Mapped[str] = mapped_column(String(250), nullable=True)
    
    url: Mapped[str | None] = mapped_column(String(250), nullable=True)
    image_data: Mapped[bytes | None] = mapped_column(
        LargeBinary,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship(User)
