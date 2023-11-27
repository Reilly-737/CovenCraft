#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from craft import Craft
from witch import Witch

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
        if craft := Craft.get_or_404(id, 
            description=f"Craft {id} not found"):
            return craft.to_dict(), 200
        
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
        if witch := Witch.get_or_404(id, 
            description=f"Witch {id} not found"):
            return witch.to_dict(), 200
        
    def patch(self, id):
        witch = Witch.get_or_404(id, 
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
        witch = Witch.get_or_404(id, 
            description=f"Witch {id} not found")
        try:
            db.session.delete(witch)
            db.session.commit()
            return {}, 204
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400
        
api.add_resource(WitchesById, "/witches/<int:id>")

if __name__ == '__main__':
    app.run(port=5555, debug=True)