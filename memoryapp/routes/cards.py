from flask import jsonify, request

from memoryapp import app
from memoryapp.repository import get_cards, create_card


@app.route('/categories/<int:category_id>/cards', methods=['GET'])
def cards(category_id):
    return jsonify(get_cards(category_id))


@app.route('/categories/<int:category_id>/cards', methods=['POST'])
def add_card(category_id):
    r = request.json

    word = r['word']
    definition = r['definition']

    return jsonify(create_card(category_id, word, definition)), 201
