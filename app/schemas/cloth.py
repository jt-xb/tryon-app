from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class ClothCategory(str, Enum):
    TOP = "top"
    BOTTOM = "bottom"
    DRESS = "dress"
    OUTERWEAR = "outerwear"
    SHOES = "shoes"
    ACCESSORY = "accessory"


class ClothBase(BaseModel):
    name: str = Field(..., max_length=255)
    category: ClothCategory
    image_url: Optional[str] = None
    description: Optional[str] = None


class ClothCreate(ClothBase):
    pass


class ClothUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    category: Optional[ClothCategory] = None
    image_url: Optional[str] = None
    description: Optional[str] = None


class ClothResponse(ClothBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
