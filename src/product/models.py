from sqlalchemy import (
    Column, 
    DateTime, 
    ForeignKey,
    Integer, 
    String, 
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.database import Base


class Product(Base):

    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")