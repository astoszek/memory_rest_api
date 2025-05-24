from dataclasses import dataclass

from dataclasses_json import dataclass_json
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from memoryapp import db


@dataclass_json
@dataclass
class Category(db.Model):
    __tablename__ = 'categories'

    category_name: Mapped[str]
    category_id: Mapped[int] = mapped_column(primary_key=True)


@dataclass_json
@dataclass
class Card(db.Model):
    __tablename__ = 'cards'

    word: Mapped[str]
    definition: Mapped[str]
    card_id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey(Category.category_id, ondelete='CASCADE'), nullable=False)

