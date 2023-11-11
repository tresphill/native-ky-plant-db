from typing import Optional
from pydantic import BaseModel, EmailStr
from models import Base

class Base(BaseModel):
    pass

class MenuSchema(Base):
    id: int
    title: str | None
    description: str | None
    price: int | None
    spicy_level: int | None
    



# menu model
# category model
# cuisine model
