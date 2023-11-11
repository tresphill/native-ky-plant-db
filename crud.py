from sqlalchemy.orm import Session, aliased, joinedload
from models import *
from schemas import *
from sqlalchemy import and_, or_

# read
def get_plant_db_items(db: Session):
    plant_db_query = (
        db.query(PlantDb).all()
    )
    return plant_db_query