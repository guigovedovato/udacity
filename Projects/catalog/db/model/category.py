#!/usr/bin/env python3
from datetime import datetime
from db.model import Base
from db.model.user import User
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Category(Base):
    """ The class Category is responsible for manage categories """

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    # Fields for audit
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime)

    # Relationship
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id
        }
