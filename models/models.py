
from datetime import datetime
from turtle import back
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import FLOAT, Column, String, TIMESTAMP, text, JSON
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.types import JSON, DateTime, String, Integer, Float
from sqlalchemy.orm import relationship

from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, declared_attr

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict

class BaseModel(object):
  @declared_attr
  def __tablename__(self):
        return self.__name__.lower()


  def to_dict(self):
      intersection = set(self.__table__.columns.keys()) & set(self.FIELDS)
      return dict(map(
          lambda key:
              (key,
                  (lambda value: self.FIELDS[key](value) if value else None)
                  (getattr(self, key))),
              intersection))
  FIELDS = {}
      
Base = declarative_base(cls=BaseModel)
#metadata = Base.metadata

class Seller(Base):
  __tablename__ = 'seller'
  
  id = Column(Integer, primary_key=True)
  country_code = Column(Integer)
  name = Column(String)
  created_at = Column(DateTime, default=datetime.utcnow)
  
  #product = relationship("Products", back_populates="products")
  
class Products(Base):
  __tablename__ = 'products'
  
  id = Column(Integer, primary_key=True)
  name = Column(String)
  seller_id = Column(Integer, ForeignKey('seller.id'),nullable=False)
  created_at = Column(DateTime, default=datetime.utcnow)
  
  #transaction = relationship("Transaction", back_populates="transaction")
  
  def __repr__(self):
        return (
            f'UserModel(id={self.id}, name={self.name},'
            f'price={self.seller_id})'
        )
  FIELDS = {
      'name': String,
      'seller_id': Integer,
  }
  
class Transaction(Base):
  __tablename__ = 'transactions'
  
  id = Column(Integer, primary_key=True)
  product_id = Column(Integer, ForeignKey('products.id'))
  price = Column(Float)
  quantity = Column(Integer)
  status = Column(String)
  created_at = Column(DateTime, default=datetime.utcnow)
  
  
  def __repr__(self):
        return (
            f'UserModel(id={self.id}, product_id={self.product_id},'
            f'price={self.price}, quantity={self.quantity},'
            f'status={self.status}, created={self.created_at})'
        )
        
  FIELDS = {
      'product_id': Integer,
      'price': Float,
      'status': String,
  }
  
  FIELDS.update(Base.FIELDS)
  

  

  