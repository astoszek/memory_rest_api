from flask import jsonify

from memoryapp import app
from memoryapp.repository import get_cards


@app.route('/categories/<int:category_id>/cards', methods=['GET'])
def cards(category_id):
    return jsonify(get_cards(category_id))

