from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from config import db

class WitchCraft(db.Model, SerializerMixin):
    __tablename__ = 'witch_crafts'

    id = db.Column(db.Integer, primary_key=True)
    witch_id = db.Column(db.Integer, db.ForeignKey("witches.id"), nullable=False)
    craft_id = db.Column(db.Integer, db.ForeignKey("crafts.id"), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # relationships

    witch = db.relationship("Witch", back_populates="witch_crafts")
    craft = db.relationship("Craft", back_populates="witch_crafts")

    # serialization

    serialize_rules = ("-witch", "-craft", "-created_at", "-updated_at")

    def __repr__(self):
        return f'<WitchCraft {self.id}>'