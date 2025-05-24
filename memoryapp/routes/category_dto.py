from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class CategoryDto:
    category_id: int
    category_name: str
    cards_count: int
