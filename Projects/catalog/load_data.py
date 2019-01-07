#!/usr/bin/env python3
from db import DB_CONNECT
from db.model import Base
from db.model.category import Category
from db.model.category_item import CategoryItem
from db.model.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(DB_CONNECT)
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User = User(name="First User", email="fuser@udacity.com",
            picture='https://pbs.twimg.com/profile_images/\
             2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User)
session.commit()

# category for Clothing
category1 = Category(user_id=1, name="Clothing")

session.add(category1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,
                             title="BALENCIAGA",
                             description="The Spanish fashion house of\
                             Balenciaga offers cutting-edge styles that\
                             balance clean, modern silhouettes with strong\
                             shapes and innovation with refinement. This\
                             navy blue cotton shirt features a relaxed fit,\
                             short sleeves, an all over logo print and a\
                             padded interior.",
                             category_id=category1.id)

session.add(categoryItem1)
session.commit()

# category for Shoes
category2 = Category(user_id=1, name="Shoes")

session.add(category2)
session.commit()

categoryItem2 = CategoryItem(user_id=1,
                             title="GUCCI",
                             description="Pre-Fall 2018 brings the outerwear\
                             theme to the forefront while staying true to the\
                             House roots. Inspired by the hiking world, these\
                             boots are presented in a dynamic mix of\
                             materials-rubber, suede, and the Original GG\
                             monogram canvas from the 1970s. A recurring\
                             detail of the latest collections, the Gucci\
                             logo is displayed in the graphic font of\
                             SEGA—a fixture in the colorful arcades and\
                             coin-op game rooms of the eighties. Grey\
                             leather, grey suede and grey technical canvas.\
                             Men's. Rubber Gucci patch in SEGA font, used\
                             with permission of Sega Holdings Co., Ltd.\
                             Perforated padded ankle detail. Rubber lug\
                             sole. 10mm height. 16cm shaft height. Made\
                             in Italy.",
                             category_id=category2.id)

session.add(categoryItem2)
session.commit()

# category for Bags
category3 = Category(user_id=1, name="Bags")

session.add(category3)
session.commit()

categoryItem3 = CategoryItem(user_id=1,
                             title="GIVENCHY",
                             description="Softly structured, Givenchy’s red\
                             and royal blue logo stripe backpack perfectly\
                             encapsulates the Givenchy men's aesthetic;\
                             strong, urban and virile. Detailed with a logo\
                             to the front, this sleek backpack features a\
                             round top handle, adjustable shoulder straps,\
                             logo patch to the rear, an all-around zip\
                             fastening, a main internal compartment, an\
                             internal zipped pocket and a front zip\
                             pocket.",
                             category_id=category3.id)

session.add(categoryItem3)
session.commit()

print("added category items!")
