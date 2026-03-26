from fastapi import FastAPI

from app.api import clothes, outfits

app = FastAPI(title="TryOn App API", version="0.1.0")

app.include_router(clothes.router)
app.include_router(outfits.router)


@app.get("/")
def root():
    return {"message": "TryOn App API"}


@app.get("/health")
def health():
    return {"status": "ok"}
