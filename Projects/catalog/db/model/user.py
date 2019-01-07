#!/usr/bin/env python3
from datetime import datetime
from db.model import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class User(Base):
    """ The class User is responsible for manage users """

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    # Fields for audit
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime)
