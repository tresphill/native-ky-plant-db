from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table, Numeric

class Base(DeclarativeBase):
    pass

class PlantDb(Base):
    __tablename__ = "plants"

    id: Mapped[int] = mapped_column(primary_key = True, index = True, autoincrement="True")
    bot_name: Mapped[str] = Column(String, default="Botanical Name")
    com_name: Mapped[str] = Column(String, default="Common Name")
    exposure: Mapped[int] = Column(Integer, default="Exposure")
    climate_zone: Mapped[int] = Column(Integer, default="Zone")

    def __repr__(self) -> str:
        return f"PlantDb(id={self.id!r}, bot_name={self.bot_name!r}, com_name={self.com_name!r}, exposure={self.exposure!r}, climate_zone={self.climate_zonezone!r})"
