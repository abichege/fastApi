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

class SaleRequest(BaseModel):
    product_id : int
    created_at : datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class SaleResponse(BaseModel):
    id : int
    product_id : int
    created_at : datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class PaymentRequest(BaseModel):
    sale_id : int
    mrid : str
    crid : str
    trans_code : str
    trans_amount : float
    phone_paid : str
    status : str
    created_at : datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class PaymentResponse(BaseModel):
    id : int
    sale_id : int
    mrid : str
    crid : str
    trans_code : str
    trans_amount : float
    phone_paid : str
    status : str
    created_at : datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class StockRequest(BaseModel):
    product_id : int
    quantity : int
    updated_at : datetime = Field(default_factory=lambda: datetime.now(timezone.utc))   

class StockResponse(BaseModel):
    id : int
    product_id : int
    quantity : int
    updated_at : datetime = Field(default_factory=lambda: datetime.now(timezone.utc))