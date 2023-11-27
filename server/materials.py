from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from config import db


metadata = db.MetaData()


craft_materials = db.Table(
    'craft_materials',
    metadata, 
    db.Column('craft_id', db.Integer, db.ForeignKey('crafts.id'), primary_key=True),
    db.Column('material_id', db.Integer, db.ForeignKey('materials.id'), primary_key=True)
)
    
  
class Materials(db.Model, SerializerMixin):
    __tablename__ = "materials"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    
    crafts = db.relationship('Craft',  
        secondary=craft_materials, back_populates='materials') 

    serialize_rules = ("-crafts",)

