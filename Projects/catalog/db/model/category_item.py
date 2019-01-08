#!/usr/bin/env python3
from datetime import datetime
from db.model import Base
from db.model.category import Category
from db.model.user import User
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship


class CategoryItem(Base):
    """ The class CategoryItem is responsible for manage category items """

    __tablename__ = 'category_item'

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    description = Column(Text(), nullable=False)

    # Fields for audit
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime)

    # Relationship
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'title': self.title,
            'description': self.description,
            'id': self.id
        }
