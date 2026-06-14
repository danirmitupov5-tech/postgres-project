from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)  # ✅ обязательное поле
    price = Column(Float, nullable=True)       # ✅ обязательное поле

    books = relationship("Book", back_populates="category")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)  # ✅ обязательное поле
    price = Column(Float, nullable=False)      # ✅ обязательное поле
    url = Column(String, nullable=True)        # ✅ обязательное поле
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="books")