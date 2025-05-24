from flask import jsonify

from memoryapp import app
from memoryapp.repository import get_categories


@app.route('/categories', methods=['GET'])
def categories():
    return jsonify(get_categories())

