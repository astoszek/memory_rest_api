from memoryapp import db
from memoryapp.entities import Category, Card


def get_categories() -> list[Category]:
    return Category.query.all()


def create_category(category_name: str) -> Category:
    category = Category(category_name=category_name)

    db.session.add(category)
    db.session.commit()

    return category


def delete_category(category_id: int):
    category = Category.query.get(category_id)

    if category:
        db.session.delete(category)
        db.session.commit()

def get_cards(category_id: int):
    db.get_or_404(Category, category_id)
    return Card.query.filter_by(category_id=category_id).all()