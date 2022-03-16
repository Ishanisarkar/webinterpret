from dataclasses import field
from email.policy import strict
from marshmallow import fields, Schema

class TransactionPostSchema(Schema):
  class Meta:
    strict=True
    product_id = fields.Integer(required=True)
    price = fields.Float(required=True)
    quantity = fields.Integer()
    status = fields.Str()
    created_at = fields.Str()
    