from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship


class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)
        #id should be primary key
    email = Column(String, unique=True, nullable=False, index=True)
        #unique as p_k is already assigned
            #2 ppl can`t have same email
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    items = relationship('Items', back_populates='owner')


class Items(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True)
    quantity = Column(Integer, nullable=False)
    category = Column(String)
    type = Column(String)
    date_posted= Column(Date)
    owner_id= Column(Integer, ForeignKey('admin.id'))

    owner = relationship('Admin', back_populates='items')
