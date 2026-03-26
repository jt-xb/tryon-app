from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app.schemas.outfit import OutfitCreate, OutfitUpdate, OutfitResponse, OutfitDetailResponse

router = APIRouter(prefix="/outfits", tags=["outfits"])


def get_db():
    """Placeholder DB dependency — implement with actual session"""
    raise NotImplementedError("Database not configured")


@router.get("/", response_model=List[OutfitResponse])
def list_outfits(
    user_id: int,
    occasion: str = None,
    season: str = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """List all outfits for a user, optionally filtered."""
    raise NotImplementedError("Not implemented")


@router.get("/{outfit_id}", response_model=OutfitDetailResponse)
def get_outfit(outfit_id: int, db: Session = Depends(get_db)):
    """Get a single outfit with its items."""
    raise NotImplementedError("Not implemented")


@router.post("/", response_model=OutfitResponse, status_code=status.HTTP_201_CREATED)
def create_outfit(outfit: OutfitCreate, user_id: int, db: Session = Depends(get_db)):
    """Create a new outfit."""
    raise NotImplementedError("Not implemented")


@router.put("/{outfit_id}", response_model=OutfitResponse)
def update_outfit(outfit_id: int, outfit: OutfitUpdate, db: Session = Depends(get_db)):
    """Update an existing outfit."""
    raise NotImplementedError("Not implemented")


@router.delete("/{outfit_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_outfit(outfit_id: int, db: Session = Depends(get_db)):
    """Delete an outfit."""
    raise NotImplementedError("Not implemented")
