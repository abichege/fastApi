from datetime import datetime, timezone
from pydantic import BaseModel, Field

class ProductRequest(BaseModel):
    user_id : int
    name : str
    amount: float
    created_at : datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ProductResponse(BaseModel):
    id : int
    name: str
    amount: float
    created_at : datetime = Field(default_factory=lambda: datetime.now(timezone.utc))