from fastapi import APIRouter, Depends, Path

from app.schemas import user
from app.enums import Tags

router = APIRouter(prefix="/users", tags=[Tags.users])

USERS =[{
    "id": 1,
    "first_name": "wisdom",
    "last_name": "oppong yeboah",
    "email": "wyoppong@gmail.com"
}]

@router.get("/", status_code=200, response_model=user.UserOutput, response_description="All users of the system")
def index() -> dict:
    """
    Get All Users
    """
    return {"results": USERS} 