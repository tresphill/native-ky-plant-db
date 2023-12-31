from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import crud
from session import SessionLocal

router = APIRouter(
    prefix="/native-ky-plants"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all", response_model=List[schemas.NativePlantSchema])
def get_items(db: Session = Depends(get_db)):
    items = crud.get_plant_db_items(db)
    return items