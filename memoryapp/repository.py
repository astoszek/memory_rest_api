from memoryapp import db
from memoryapp.entities import Category


def get_categories() -> list[Category]:
    return Category.query.all()

def create_category(category_name: str) -> Category:
    category = Category(category_name=category_name)

    db.session.add(category)
    db.session.commit()

    return category