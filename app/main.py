from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, database, crud, schemas
import json

app = FastAPI()


@app.on_event("startup")
async def startup():
    # create tables
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.get("/")
def health():
    return ({"status": "good", "server is live":"and healthy"})

@app.post("/shorten", response_model=schemas.URLInfo)
async def shorten_url(
    url_create: schemas.URLCreate, db: AsyncSession = Depends(database.get_db)
):
    url = await crud.create_url(db, url_create.long_url)
    return url


@app.get("/{shortcode}")
async def redirect_to_url(shortcode: str, db: AsyncSession = Depends(database.get_db)):
    url = await crud.get_url_by_shortcode(db, shortcode)
    if not url:
        raise HTTPException(status_code=404, detail="Shortcode not found")
    
    # Use 302 status code for better client compatibility
    return RedirectResponse(url=url.long_url, status_code=302)
