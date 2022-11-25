from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import StaffCreate, ShowStaff
from database import get_db
from hashing import Hasher
from models import Staff

router=APIRouter()


@router.post(
    "/staff",
    tags=['staff'],
    response_model=ShowStaff
)
def create_staff(
        staff: StaffCreate,
        db: Session = Depends(get_db)
):
    staff = Staff(
        email=staff.email,
        password=Hasher.get_hash_password(staff.password)
    )
    db.add(staff)
    db.commit()
    db.refresh(staff)
    return staff
