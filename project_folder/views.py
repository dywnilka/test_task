from project_folder import app, db
from models import Order
from datetime import date
from flask import jsonify, request


@app.route('/orders', methods=['GET'])
def get_all_orders():
    orders = Order.query.all()
    output = []
    for order in orders:
        order_data = {
            'order_id': order.order_id,
            'customer_id': order.customer_id,
            'product_name': order.product_name,
            'quantity': order.quantity,
            'price_per_unit': order.price_per_unit,
            'order_date': order.order_date.strftime("%Y-%m-%d"),
        }
        output.append(order_data)
    return jsonify({'orders': output})


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'})
    order_data = {
        'order_id': order.order_id,
        'customer_id': order.customer_id,
        'product_name': order.product_name,
        'quantity': order.quantity,
        'price_per_unit': order.price_per_unit,
        'order_date': order.order_date.strftime("%Y-%m-%d"),
    }
    return jsonify({'order': order_data})


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'})
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted'})


@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(
        order_id=data['order']['order_id'],
        customer_id=data['order']['customer_id'],
        product_name=data['order']['product_name'],
        quantity=data['order']['quantity'],
        price_per_unit=data['order']['price_per_unit'],
        order_date=date.fromisoformat(data['order']['order_date']),
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'New order created'})


@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'})
    data = request.get_json()
    order.customer_id = data['order']['customer_id']
    order.product_name = data['order']['product_name']
    order.quantity = data['order']['quantity']
    order.price_per_unit = data['order']['price_per_unit']
    order.order_date = date.fromisoformat(data['order']['order_date'])
    db.session.commit()
    return jsonify({'message': 'Order updated'})
