from sqlalchemy import text
from memoryapp import db
from memoryapp.entities import Category, Card
from memoryapp.routes.category_dto import CategoryDto


def get_categories() -> list[CategoryDto]:
    sql = text("""
            SELECT c.category_id, c.category_name, COUNT(cd.card_id) AS card_count
            FROM categories c
                LEFT JOIN cards cd ON c.category_id = cd.category_id
            GROUP BY c.category_id, c.category_name
    """)

    result = db.session.execute(sql).all()

    categories_with_count = []
    for row in result:
        category = CategoryDto(category_id=row.category_id, category_name=row.category_name, cards_count=row.card_count)
        categories_with_count.append(category)

    return categories_with_count


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


def create_card(category_id: int, word: str, definition: str) -> Card:
    db.get_or_404(Category, category_id)

    card = Card(category_id=category_id, word=word, definition=definition)
    db.session.add(card)
    db.session.commit()

    return card


def remove_card(category_id: int, card_id: int):
    card = Card.query.filter_by(category_id=category_id, card_id=card_id).first()

    if card:
        db.session.delete(card)
        db.session.commit()
