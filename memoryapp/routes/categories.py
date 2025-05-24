from flask import jsonify

from memoryapp import app

categories_list = [
    {'category_id': 1, 'category_name': 'Sport'},
    {'category_id': 2, 'category_name': 'Kuchnia'}
]

@app.route('/categories', methods=['GET'])
def categories():
    return jsonify(categories_list)

