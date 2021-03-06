from datetime import datetime
import uuid


class Movement:

    DIFFICULTY = ('beginner', 'intermediate', 'advanced')

    FIELDS = ('id', 'name', 'description', 'notes', 'tags',
              'weighted', 'created_at', 'difficulty')

    @classmethod
    def generate_id(cls):
        return str(uuid.uuid4())[:8]

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['name'],
            data['description'],
            data['notes'],
            data['difficulty'],
            data['weighted'],
            data['tags'],
            data['id'])

    def __init__(
            self,
            name,
            description='',
            notes='',
            difficulty=None,
            weighted=True,
            tags=[],
            id=None):
        if difficulty is not None and difficulty not in self.DIFFICULTY:
            raise ValueError("%s is not a valid difficulty." % difficulty)
        self.id = id if id else self.generate_id()
        self.name = name
        self.weighted = weighted
        self.tags = tags
        self.description = description
        self.notes = notes
        self.created_at = datetime.now()
        self.difficulty = difficulty
