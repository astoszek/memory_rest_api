from flask import jsonify, request


from memoryapp import app
from memoryapp.repository import get_categories, create_category, delete_category


@app.route('/categories', methods=['GET'])
def categories():
    return jsonify(get_categories())


@app.route('/categories', methods=['POST'])
def add_category():
    r = request.json
    category_name = r['category_name']

    return jsonify(create_category(category_name)), 201


@app.route('/categories/<int:category_id>', methods=['DELETE'])
def remove_category(category_id):
    delete_category(category_id)

    return '', 204