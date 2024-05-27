from project_folder import app, db
from datetime import date


class Order(db.Model):
    __tablename__ = "Orders"
    __table_args__ = {'extend_existing': True}
    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = quantity = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price_per_unit = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.Date, nullable=False)


if __name__ == "__main__":
    app.app_context().push()
    db.create_all()

    order1 = Order(order_id=1, customer_id=101, product_name='Laptop',
                   quantity=1, price_per_unit=1200, order_date=date.fromisoformat('2024-04-01'))
    order2 = Order(order_id=2, customer_id=102, product_name='Smartphone',
                   quantity=2, price_per_unit=800, order_date=date.fromisoformat('2024-04-02'))
    order3 = Order(order_id=3, customer_id=101, product_name='Tablet',
                   quantity=1, price_per_unit=500, order_date=date.fromisoformat('2024-04-03'))
    order4 = Order(order_id=4, customer_id=103, product_name='Headphones',
                   quantity=1, price_per_unit=100, order_date=date.fromisoformat('2024-04-04'))
    order5 = Order(order_id=5, customer_id=102, product_name='Laptop',
                   quantity=1, price_per_unit=1200, order_date=date.fromisoformat('2024-04-05'))

    db.session.add(order1)
    db.session.add(order2)
    db.session.add(order3)
    db.session.add(order4)
    db.session.add(order5)
    db.session.commit()
