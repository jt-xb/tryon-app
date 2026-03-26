from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

from .cloth import ClothResponse


class OutfitItemBase(BaseModel):
    cloth_id: int
    order: int = 0


class OutfitItemCreate(OutfitItemBase):
    pass


class OutfitItemResponse(OutfitItemBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class OutfitBase(BaseModel):
    name: str = Field(..., max_length=255)
    description: Optional[str] = None
    occasion: Optional[str] = Field(None, max_length=128)
    season: Optional[str] = Field(None, max_length=64)


class OutfitCreate(OutfitBase):
    items: List[OutfitItemCreate] = []


class OutfitUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    occasion: Optional[str] = Field(None, max_length=128)
    season: Optional[str] = Field(None, max_length=64)
    items: Optional[List[OutfitItemCreate]] = None


class OutfitItemDetailResponse(OutfitItemResponse):
    cloth: Optional[ClothResponse] = None


class OutfitResponse(OutfitBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class OutfitDetailResponse(OutfitResponse):
    items: List[OutfitItemDetailResponse] = []
