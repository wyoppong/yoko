from typing import Optional

from pydantic import BaseModel


class UserOutput(BaseModel):
    id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str] = None
    is_superuser: bool = False