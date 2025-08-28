import random, string
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import URL

def generate_shortcode(length: int = 6) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

async def create_url(db: AsyncSession, long_url: str) -> URL:
    shortcode = generate_shortcode()
    # Make sure column name matches your model
    url = URL(long_url=str(long_url), shortcode=shortcode)
    db.add(url)
    await db.commit()
    await db.refresh(url)
    return url

async def get_url_by_shortcode(db: AsyncSession, shortcode: str):
    result = await db.execute(select(URL).where(URL.shortcode == shortcode))
    return result.scalars().first()