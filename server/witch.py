from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from config import bcrypt

from config import db

class Witch(db.Model, SerializerMixin):
    __tablename__ = 'witches'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)
    bio = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # relationships
    witch_crafts = db.relationship(
        "WitchCraft", back_populates="witch", cascade="all, delete-orphan"
    )
    crafts = association_proxy("witch_crafts", "witch")

    # serialization
    serialize_rules = ("-witch_crafts", "-created_at", "-updated_at")

    def __repr__(self):
        return f"<Witch {self.id}: {self.username}>"
    
     # validation
    @validates("username")
    def validate_username(self, _, username):
        if not isinstance(username, str):
            raise TypeError("Username must be a string")
        elif len(username) < 1:
            raise ValueError("Username must be at least 1 characters")
        return username
    
    @validates("bio")
    def validate_desc(self, _, desc):
        if not isinstance(desc, str):
            raise TypeError("Witches bio must be a string")
        elif len(desc) < 50 or len(desc) > 5000:
            raise ValueError("Witches bio must be between 50-5000 characters")
        return desc
        
    @hybrid_property
    def password_hash(self):
        # return self._password_hash
        raise AttributeError("Password hashes are super secret!")

    @password_hash.setter
    def password_hash(self, new_password):
        hashed_password = bcrypt.generate_password_hash(new_password).decode("utf-8")
        self._password_hash = hashed_password

    def authenticate(self, password_to_check):
        return bcrypt.check_password_hash(self._password_hash, password_to_check)
 
