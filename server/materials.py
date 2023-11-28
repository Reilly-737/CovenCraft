from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db
  
class Materials(db.Model, SerializerMixin):
    __tablename__ = "materials"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now()) 

    craft_materials = db.relationship("CraftMaterials",
        back_populates="material", cascade="all, delete-orphan"
    )
    crafts = association_proxy("craft_materials", "craft")

    serialize_rules = ("-craft_materials", "-crafts", "-created_at", "-updated_at")
