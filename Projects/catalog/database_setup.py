#!/usr/bin/env python3
from db import DB_CONNECT
from db.model import Base
from db.model.category import Category
from db.model.category_item import CategoryItem
from db.model.user import User
from sqlalchemy import create_engine


engine = create_engine(DB_CONNECT)
Base.metadata.create_all(engine)
