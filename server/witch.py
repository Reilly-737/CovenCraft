
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

class Witch(db.Model, SerializerMixin):
    __tablename__ = 'witches'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    hash = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, on_update=db.func.now())

    witch_crafts = db.relationship(
        "WitchCrafts", back_populates="witch", cascade="all, delete-orphan"
    )
    crafts = association_proxy("witch_crafts", "witch")

    serialize_rules = ("-witch_crafts")

    def __repr__(self):
        return f"<Witch {self.id}: {self.username}>"
    
    @validates("username")
    def validate_username(self, _, username):
        if not isinstance(username, str):
            raise TypeError("Username must be a string")
        elif len(username) < 1:
            raise ValueError("Username must be at least 1 characters")
        return username
    
 