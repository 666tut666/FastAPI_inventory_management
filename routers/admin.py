from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import AdminCreate, ShowAdmin
from database import get_db
from hashing import Hasher
from models import Admin, User, AdminType

router=APIRouter()


@router.post(
    "/admin",
    tags=['admin'],
    response_model=ShowAdmin
)
def create_admin(
        admin: AdminCreate,
        db: Session = Depends(get_db)
):
    admin = Admin(
        email=admin.email,
        password=Hasher.get_hash_password(admin.password),
        #user_id=admin.user_id,
        #admin_type_id=admin.admin_type_id
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin
