from sqlalchemy.orm import Session, aliased, joinedload
from models import *
from schemas import *
from sqlalchemy import and_, or_

# read
def get_menu_items(db: Session):
    menu_items_query = (
        db.query(Menu).all()
    )
    return menu_items_query