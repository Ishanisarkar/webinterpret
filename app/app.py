from app.middleware import RequireJSON, JSONTranslator
from app import views
from database.init import create_all
import falcon
import json


class IndexResource(object):
  def on_get(self, req, res):
    res.status = falcon.HTTP_200
    res.body = json.dumps({"success": "My first falcon app"})
    
    
app = falcon.API(middleware=[
	JSONTranslator(),
  RequireJSON()
		])
app.add_route('/', IndexResource())
app.add_route('/seller/', views.SellerResource())
app.add_route('/products/', views.Productresource())
app.add_route('/transactions/', views.TransactionsResource())
app.add_route('/transactions/{product_id}', views.TransationsGetProduct())
app.add_route('/products/{seller_id}', views.ProductResourceSeller())



create_all()
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)