from sqlalchemy import Column, String, Boolean, Integer


from src.database import Base


class Bahan(Base):

    __tablename__ = "bahan"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)