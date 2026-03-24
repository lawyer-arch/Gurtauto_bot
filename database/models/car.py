from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from database.base import Base


class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True)
    marka: Mapped[str] = mapped_column(String(250))
    model: Mapped[str] = mapped_column(String(250))
    modification: Mapped[str] = mapped_column(String(250), nullable=True)
    body_type: Mapped[str] = mapped_column(String(250), nullable=True)
    generation: Mapped[str] = mapped_column(String(250), nullable=True)