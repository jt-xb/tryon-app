from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app.schemas.cloth import ClothCreate, ClothUpdate, ClothResponse

router = APIRouter(prefix="/clothes", tags=["clothes"])


def get_db():
    """Placeholder DB dependency — implement with actual session"""
    raise NotImplementedError("Database not configured")


@router.get("/", response_model=List[ClothResponse])
def list_clothes(
    user_id: int,
    category: str = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """List all clothes for a user, optionally filtered by category."""
    raise NotImplementedError("Not implemented")


@router.get("/{cloth_id}", response_model=ClothResponse)
def get_cloth(cloth_id: int, db: Session = Depends(get_db)):
    """Get a single cloth by ID."""
    raise NotImplementedError("Not implemented")


@router.post("/", response_model=ClothResponse, status_code=status.HTTP_201_CREATED)
def create_cloth(cloth: ClothCreate, user_id: int, db: Session = Depends(get_db)):
    """Create a new cloth item."""
    raise NotImplementedError("Not implemented")


@router.put("/{cloth_id}", response_model=ClothResponse)
def update_cloth(cloth_id: int, cloth: ClothUpdate, db: Session = Depends(get_db)):
    """Update an existing cloth item."""
    raise NotImplementedError("Not implemented")


@router.delete("/{cloth_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cloth(cloth_id: int, db: Session = Depends(get_db)):
    """Delete a cloth item."""
    raise NotImplementedError("Not implemented")
