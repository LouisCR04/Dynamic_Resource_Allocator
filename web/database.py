"""
Database Engine
"""

from mongoengine import Document, StringField, DictField, ReferenceField
from datetime import datetime

class Post(Document):
    author = ReferenceField(User, required=True, unique-True)
    title = StringField(required=True, max_length=100)
    content = StringField(required=True)
    date_posted = DateTimeField(required=True, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class User(Document):
    username = StringField(required=True, max_length=20, unique=True)
    email = StringField(required=True, max_length=120, unique=True)
    image_file = StringField(required=True, max_length=120, default='default.jpg')
    password = StringField(required=True, max_length=60)

    def get_posts(self):
        returnPost.objects(author=self)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', self.image_file)"
