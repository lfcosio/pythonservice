import os
from . import create_app
from app.models.models import Customer
from . import db
from flask import jsonify, request, abort

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.route("/api/customer/list", methods=["GET"])
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer.to_json() for customer in customers])


@app.route("/api/customer/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer is None:
        abort(404)
    return jsonify(customer.to_json())


@app.route("/api/customer/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer is None:
        abort(404)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'result': True})


@app.route('/customer', methods=['POST'])
def create_customer():
    if not request.json:
        abort(400)
    customer = Customer(
        first_name=request.json.get('first_name'),
        last_name=request.json.get('last_name'),
        dob=request.json.get('dob'),
        street_addr=request.json.get('street_addr'),
        country=request.json.get('country'),
        phone_number=request.json.get('phone_number'),

    )
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.to_json()), 201


@app.route('/api/customer/<int:isbn>', methods=['PUT'])
def update_customer(isbn):
    if not request.json:
        abort(400)
    customer = Customer.query.get(isbn)
    if customer is None:
        abort(404)
    customer.title = request.json.get('title', customer.title)
    customer.author = request.json.get('author', customer.author)
    customer.price = request.json.get('price', customer.price)
    db.session.commit()
    return jsonify(customer.to_json())
