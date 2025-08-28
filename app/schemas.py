from pydantic import BaseModel, HttpUrl

class URLCreate(BaseModel):
    long_url: HttpUrl

class URLInfo(BaseModel):
    shortcode: str
    long_url: HttpUrl

    class Config:
        orm_mode = True
