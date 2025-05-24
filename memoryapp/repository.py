from memoryapp.entities import Category


def get_categories() -> list[Category]:
    return Category.query.all()


