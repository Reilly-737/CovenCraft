#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session
from flask_restful import Resource
from sqlalchemy.orm import joinedload

# Local imports
from config import app, db, api
# Add your model imports
from craft import Craft
from materials import Materials
from craft_materials import CraftMaterials
from witch import Witch
from witchcraft import WitchCraft

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class Crafts(Resource):
    def get(self):
        crafts = [craft.to_dict() for craft in Craft.query]
        return crafts, 200

api.add_resource(Crafts, "/crafts")

class CraftsById(Resource):
    def get(self, id):
        if craft := Craft.query.get_or_404(id, 
            description=f"Craft {id} not found"):
            return craft.to_dict(only=(
                "id", "title", "description", "instructions", "image", "difficulty", 
                "materials.name", "witches.username"
            )), 200
        
api.add_resource(CraftsById, "/crafts/<int:id>")

class Witches(Resource):
    def get(self):
        witches = [witch.to_dict() for witch in Witch.query]
        return witches, 200
    
    def post(self):
        try:
            data = request.get_json()
            new_witch = Witch(**data)
            db.session.add(new_witch)
            db.session.commit()
            return new_witch.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400
    
api.add_resource(Witches, "/witches")

class WitchesById(Resource):
    def get(self, id):
        if witch := Witch.query.get_or_404(id, 
            description=f"Witch {id} not found"):
            return witch.to_dict(), 200
        
    def patch(self, id):
        witch = Witch.query.get_or_404(id, 
            description=f"Witch {id} not found")
        try:
            data = request.get_json()
            for k, v in data.items():
                setattr(witch, k, v)
            db.session.commit()
            return witch.to_dict(), 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400
        
    def delete(self, id):
        witch = Witch.query.get_or_404(id, 
            description=f"Witch {id} not found")
        try:
            db.session.delete(witch)
            db.session.commit()
            return {}, 204
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400
        
api.add_resource(WitchesById, "/witches/<int:id>")

class WitchCrafts(Resource):
    def post(self):
        if 'user_id' not in session:
            return {'error': 'User not logged in'}, 401

        user_id = session['user_id']
        craft_id = request.json.get('craft_id')

        try:
            new_wc = WitchCraft(user_id=user_id, craft_id=craft_id)
            db.session.save(new_wc)
            db.session.commit()
            return new_wc.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400

api.add_resource(WitchCrafts, "/witch_crafts")

class Login(Resource): 
    def post(self): 
        user = Witch.query.filter( 
            Witch.username == request.get_json()['username'] 
        ).first() 

        session['user_id'] = user.id 
        return user.to_dict()
    
api.add_resource(Login, "/login")



if __name__ == '__main__':
    app.run(port=5555, debug=True)