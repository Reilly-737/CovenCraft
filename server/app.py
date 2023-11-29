#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session
from flask_restful import Resource
from werkzeug.exceptions import NotFound

# Local imports
from config import app, db, api
# Add your model imports
from craft import Craft
from materials import Materials
from craft_materials import CraftMaterials
from witch import Witch
from witchcraft import WitchCraft

# Views go here!

@app.errorhandler(NotFound)
def handle_404(error):
    response = {"message": error.description}
    return response, error.code

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class Crafts(Resource):
    def get(self):
        try:
            crafts = [craft.to_dict() for craft in Craft.query]
            return crafts, 200
        except Exception as e:
            return {'error': str(e)}, 400

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
            new_witch = Witch(
                username = data.get('username'),
                email = data.get('email'),
                bio = data.get('bio')
            )
            new_witch.password_hash = data.get('password')
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
            return witch.to_dict(rules=("crafts",)), 200
        
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

class WitchCraftsById(Resource):
    def delete(self, id):
        old_wc = db.session.get(WitchCraft, id)

        try:
            db.session.delete(old_wc)
            db.session.commit()
            return {}, 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400

api.add_resource(WitchCraftsById, "/witch_crafts/<int:id>")

class CheckSession(Resource): 
    def get(self):  
        if "user_id" not in session:
            return {"message": "Not Authorized"}, 403
        if user := db.session.get(Witch, session["user_id"]):
            return user.to_dict(rules=("-email", "-bio")), 200
        return {"message": "Not Authorized"}, 403

api.add_resource(CheckSession, '/check_session') 

class Login(Resource): 
    def post(self): 
        try:
            data = request.get_json()
            print("Received data:", data)

            user_by_username = Witch.query.filter_by(username = data.get('username')).first()
            user_by_email = Witch.query.filter_by(email = data.get('username')).first()

            if (user_by_username or user_by_email):
                user = user_by_username or user_by_email
                if user.authenticate(data.get('password')):
                    session['user_id'] = user.id
                    return user.to_dict(), 200
            return {'message': 'Invalid Credentials'}, 403
        except Exception as e:
            print("Exception:", e)
            return {'message': 'Invalid Credentials'}, 403
    
api.add_resource(Login, "/login")

class Logout(Resource): 
    def delete(self):  
        session['user_id'] = None 
        return {'message': '204: No Content'}, 204 

api.add_resource(Logout, '/logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)