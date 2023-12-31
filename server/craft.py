from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

class Craft(db.Model, SerializerMixin):
    __tablename__ = 'crafts'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    instructions = db.Column(db.String, nullable=False)
    difficulty = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    witch_crafts = db.relationship("WitchCraft", 
        back_populates="craft", cascade="all, delete-orphan"
    )
    witches = association_proxy("witch_crafts", "witch")

    craft_materials = db.relationship("CraftMaterials",
        back_populates="craft", cascade="all, delete-orphan"
    )
    materials = association_proxy("craft_materials", "material")

    serialize_rules = ("-witch_crafts", "-witches", "-craft_materials", "-materials", "-created_at", "-updated_at")

    def __repr__(self):
        return f"<Craft {self.id}: {self.title}>"
    
    @validates("name")
    def validate_name(self, _, name):
        if not isinstance(name, str):
            raise TypeError("Craft name must be a string")
        elif len(name) < 5:
            raise ValueError("Craft name must be at least 5 characters")
        return name
    
    @validates("decription")
    def validate_desc(self, _, desc):
        if not isinstance(desc, str):
            raise TypeError("Craft description must be a string")
        elif len(desc) < 50 or len(desc) > 250:
            raise ValueError("Craft description must be between 50-250 characters")
        return desc
    
    @validates("difficulty")
    def validate_diff(self, _, diff):
        difficulties = ["beginner", "intermediate", "advanced"]
        if diff not in difficulties:
            raise ValueError(f"Difficulty must be: {difficulties}")
        return diff
    
