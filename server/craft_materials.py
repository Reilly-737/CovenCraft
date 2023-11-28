from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

from config import db

class CraftMaterials(db.Model, SerializerMixin):
    __tablename__ = "craft_materials"

    id = db.Column(db.Integer, primary_key=True)
    craft_id = db.Column(db.Integer, db.ForeignKey('crafts.id'))
    material_id = db.Column(db.Integer, db.ForeignKey('materials.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    craft = db.relationship('Craft', back_populates='craft_materials') 
    material = db.relationship('Materials', back_populates='craft_materials') 

    serialize_rules = ("-craft.craft_materials", "-material.craft_materials", "-created_at", "-updated_at")