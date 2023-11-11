from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Numeric

class Base(DeclarativeBase):
    pass

class Menu(Base):
    __tablename__ = "Menu"

    id: Mapped[int] = mapped_column(primary_key = True, index = True)
    title: Mapped[str] = Column(String, default="Title")
    description: Mapped[str] = Column(String, default="Description")
    price: Mapped[int] = Column(Integer, default="Price")
    spicy_level: Mapped[int] = Column(Integer, default="Spiciness")

    def __repr__(self) -> str:
        return f"MenuItem(id={self.id!r}, title={self.title!r}, desciption={self.description!r}, price={self.price!r}, spicy_level={self.spicy_level!r})"
