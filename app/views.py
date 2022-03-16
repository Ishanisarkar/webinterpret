from asyncio.log import logger
import json
import falcon
from database.init import db_session
from models.models import Products, Seller, Transaction
from app.schemas import TransactionPostSchema
import ujson


try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict

class BaseResource(object):
    def success(self, resp, data=None):
        resp.status = falcon.HTTP_200
        obj = OrderedDict()
        obj['status'] = 200
        obj['data'] = data
        obj['message'] = 'OK'
        resp.body = json.dumps(obj)


class TransactionsResource(BaseResource):
  serializers = {
        'post': TransactionPostSchema,
    }
    
    
  def on_get(self, req, resp):
    # ses = db_session()
    # transactions = ses.query(Transaction).all()
    # obj = [transaction.to_dict() for transaction in transactions]
    # self.success(resp, obj)
    
    try:
      logger.info("Performing get all transactions...")
      ses = db_session()
      transactions = ses.query(Transaction).all()
      obj3 = {"id":[],"product_id":[],"price":[],"quantity":[],"status":[]}
      for transaction in transactions:
        obj3["id"].append(transaction.id)
        obj3["product_id"].append(transaction.product_id)
        obj3["price"].append(transaction.price)
        obj3["quantity"].append(transaction.quantity)
        obj3["status"].append(transaction.status)
      self.success(resp, obj3)
    except Exception as e:
      logger.error(e, exc_info=True)
      resp.body = ujson.dumps({"error": e})
      resp.status = falcon.HTTP_502


  def on_post(self, req, resp):
    ses = db_session()
    task_details = req.context['doc']
    task = Transaction(
      product_id=task_details['product_id'], 
      price=task_details['price'],
      quantity=task_details['quantity'],
      status=task_details['status']
      )
    ses.add(task)
    ses.commit()
    self.success(resp, "Transaction created successfullly")
    
class TransationsGetProduct(BaseResource):
  def on_get(self, req, resp, product_id):
    ses = db_session()
    transactions = ses.query(Transaction).filter(Transaction.product_id == product_id).all()
    # obj = [transaction.to_dict() for transaction in transactions]
    # self.success(resp, obj)
    obj2 = {"id":[],"product_id":[],"price":[],"quantity":[],"status":[]}
    try:
      for transaction in transactions:
        obj2["id"].append(transaction.id)
        obj2["product_id"].append(transaction.product_id)
        obj2["price"].append(transaction.price)
        obj2["quantity"].append(transaction.quantity)
        obj2["status"].append(transaction.status)
      self.success(resp, obj2)
    except Exception as e:
      logger.error(e, exc_info=True)
      resp.body = ujson.dumps({"error": e})
      resp.status = falcon.HTTP_502
    
      
    
class SellerResource(BaseResource):
  def on_get(self, req, resp):
    obj = {"id":[],"country_code":[],"name":[]};
    ses = db_session()
    sellers = ses.query(Seller).all()
    print(sellers)
    try:
      for seller in sellers:
        obj["id"].append(seller.id)
        obj["country_code"].append(seller.country_code)
        obj["name"].append(seller.name)
      self.success(resp, obj)
    except Exception as e:
      logger.error(e, exc_info=True)
      resp.body = ujson.dumps({"error": e})
      resp.status = falcon.HTTP_502
    
  def on_post(self, req, resp):
    ses = db_session()
    task_details = req.context['doc']
    task = Seller(
      country_code=task_details['country_code'], 
      name=task_details['name'],
      )
    ses.add(task)
    ses.commit()
    self.success(resp, "Seller created successfullly")
    
class Productresource(BaseResource):
  def on_get(self, req, resp):
    ses = db_session()
    products = ses.query(Products).all()
    obj1 = {"id":[],"name":[],"seller_id":[]};
    try:
      for product in products:
        obj1['id'].append(product.id)
        obj1['name'].append(product.name)
        obj1['seller_id'].append(product.seller_id)
      self.success(resp,obj1)
    except Exception as e:
      logger.error(e, exc_info=True)
      resp.body = ujson.dumps({"error": e})
      resp.status = falcon.HTTP_502
      
    
  def on_post(self, req, resp):
    ses = db_session()
    task_details = req.context['doc']
    task = Products(
      name=task_details['name'],
      seller_id=task_details['seller_id']
      )
    ses.add(task)
    ses.commit()
    self.success(resp, "Seller created successfullly")
    
class ProductResourceSeller(BaseResource):
  def on_get(self, req, resp, seller_id):
    ses = db_session()
    products = ses.query(Products).filter(Products.seller_id == seller_id).all()
    obj4 = {"id":[],"name":[],"seller_id":[]};
    try:
      for product in products:
        obj4['id'].append(product.id)
        obj4['name'].append(product.name)
        obj4['seller_id'].append(product.seller_id)
      self.success(resp,obj4)
    except Exception as e:
      logger.error(e, exc_info=True)
      resp.body = ujson.dumps({"error": e})
      resp.status = falcon.HTTP_502
  


