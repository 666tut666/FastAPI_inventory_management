from fastapi import APIRouter


router = APIRouter()


@router.get(
    '/items',
    tags=["products"]
)
def get_product():
    return {"message": "products"}
