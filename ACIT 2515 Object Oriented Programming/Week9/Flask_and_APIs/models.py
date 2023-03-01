from database import db


class Product(db.Model):
    name = db.Column(db.String, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=True)
    
    def to_dict(self):
        return {'name': self.name, 'price': self.price, 'quantity': self.quantity}
    
    def remove(self):
        db.delete(self.name)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    completed = db.Column(db.Boolean)
    products = db.relationship('ProductsOrder', back_populates='order')
    def to_dict(self):
        return {'name': self.name, 'address': self.address, 'completed': self.completed, 'products': self.products}
    
class ProductsOrder(db.Model):
    # Product foreign key is name
    product_name = db.Column(db.ForeignKey("product.name"), primary_key=True)
    # Order foreign key is ID
    order_id = db.Column(db.ForeignKey("order.id"), primary_key=True)
    # This is how many items we want
    quantity = db.Column(db.Integer, nullable=False)
    # Relationships and backreferences for SQL Alchemy
    product = db.relationship('Product')
    order = db.relationship('Order', back_populates='products')
