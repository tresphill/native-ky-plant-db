from typing import Optional
from pydantic import BaseModel, EmailStr
from models import Base

class Base(BaseModel):
    pass

class NativePlantSchema(Base):
    id: int
    bot_name: str | None
    com_name: str | None
    exposure: int | None
    zone: int | None
