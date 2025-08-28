from sqlalchemy import Column, Integer, String
from .database import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    long_url = Column(String, nullable=False)
    shortcode = Column(String, unique=True, index=True, nullable=False)
