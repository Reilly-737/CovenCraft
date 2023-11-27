from app import app, db
from materials import Materials
from craft import Craft

def clear_tables():
    print("Clearing database...")
    with app.app_context():
        db.drop_all()
        db.create_all()

def seed_crafts():
    print("Adding crafts...")

    CRAFT_DATA = [
        {
            'image': 'https://images.unsplash.com/photo-1698484628006-233d945b1e9b?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'title': 'Witch Protection Bottle',
            'description': 'Protection spells will protect you from malicious spells, hexes or negative enchantments cast deliberately against you by another.',
            'materials': ['small jar', 'broken glass', 'nails', 'thorns', 'steel wool', 'wormwood', 'thistle', 'nettles', 'vinegar', 'salt', 'black candle'],
            'instructions': 'Fill jar with items listed and seal tightly. On top of the lid draw a pentacle. Place the black candle on the lid and light it. '
                'Chant the following over the candle:'
                'Candle of the black and hexes old Release the powers that you hold '
                'Reverse the flow of spells once cast Leave pain and sorrow in the past. '
                'Let the candle burn out. Take the jar and bury it in the earth close to your home, '
                'Has a shelf life of six months',
            'difficulty': 'advanced',
        },
        {
            'image': 'https://images.unsplash.com/photo-1492552181161-62217fc3076d?q=80&w=1797&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'title': 'Happy Home Oil',
            'description': 'This happy home oil is a fantastic home spell to use between new moon cleanses! Keep your home running smoothly harmoniously and peacefully.',
            'materials': ['gardenia', 'myrrh', 'coconut oil', 'salt', 'five finger grass'],
            'instructions': 'Add all materials together and place droplets around the house or dress candles with oil.',
            'difficulty': 'beginner',
        },
        {
            'image': 'https://images.unsplash.com/photo-1531168557378-436035c2a05c?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'title': 'Rosemary Infusion of Power',
            'description': 'Washing hands with an infusion of rosemary magickally empowers and enhances all healing. '
                'Healing spells are not intended to be used in place of traditional or conventions methods of healing'
                'They work best in conjunction with them as reinforcement.',
            'materials': ['rosemary', 'strainer', 'small bottle'],
            'instructions': 'Create a infusion by pouring boiling water over rosemary. Allow it to cool then strain. This may be done prior to healing or liquid can be bottled and refrigerated for use later.',
            'difficulty': 'beginner',
        },
        {
            'image': 'https://images.unsplash.com/photo-1560517069-1b9574e2aea5?q=80&w=2073&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'title': 'Prosperity Basil Bath Spell',
            'description': 'The scent of basil on the skin attracts financial good fortune to the wearer. Take this bath before engaging in any interaction revolving around your finances.',
            'materials': ['basil', 'boiling water', 'small bag'],
            'instructions': 'Roughly chop most of the basil in order to release the volatile oils. You must leave some of the leaves whole. Then pour boiling water over the basil and let it steep.,'
                'When it\'s cooled add this to your bath. Float the whole leaves in the water and visualize yourself swimming in cash.,'
                'Let the water drain and allow yourself to air dry.'
                'Do not dispose the used basil leaves but either leave them in the tub until your transactions are complete or remove them place in bag and '
                'reserve until an opportune moment for disposal arises.',
            'difficulty': 'beginner',
        },
        {
            'image': 'https://images.unsplash.com/photo-1447875569765-2b3db822bec9?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'title': 'Hydrangea Hex Reversal',
            'description': 'Hexes happen! This easy hex remover is very handy to have on hand.',
            'materials': ['dried hydrangeas', 'fire-safe cauldron'],
            'instructions': 'Burn died Hydrangea to reverse spells and remove hexes. Blend the ashes with more dried ground hydrangea and scatter around the home.',
            'difficulty': 'intermediate',
        },
        {
            'image': 'https://images.unsplash.com/photo-1620376646319-3090858a3c1b?q=80&w=2017&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'title': 'Begone Banish Powder',
            'description': 'Banishing spells remove something or someone from your presence often permanently. '
                'This powder can also be used as an accompaniment for spells particularly around or over candles',
            'materials': ['black pepper', 'cayenne pepper', 'cinnamon', 'salt', 'sulfur'],
            'instructions': 'Sprinkle the banishing powder on clothes, especially belonging to anyone you would like to see gone(without wishing harm to them).',
            'difficulty': 'intermediate',
        },
        {
            'image': 'https://images.unsplash.com/photo-1625649947410-eef42418fc58?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'title': 'Low Energy Spell',
            'description': 'Drained? Just want to get back into bed? Try this spell to get that pep back in your step.',
            'materials': ['sliced lemon', 'salt', 'rosemary'],
            'instructions': 'Take sliced lemon sprinkle salt over slice then pair rosemary sprig. Place under bed. Shelf life of one night to one week.',
            'difficulty': 'beginner',
        },
        {
            'image': 'https://images.unsplash.com/photo-1612549224874-24dec5ba09f4?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'title': 'Freeze Spell',
            'description': 'Do you need space? A moment or day without the presence of a certain someone or something? This spell is to create space and \'freeze them\'',
            'materials': ['bay leaf', 'cup of water'],
            'instructions': 'Boil water. Write the name of the something/someone on leaf. Imagine them at peace and not thinking of you. '
                'Dip leaf in water. Take leaf out of water and dump water out back door. Place leaf in freezer. '
                'Practice a self-care routine or mediate on what feelings are rising. '
                'Take leaf out when finished and dispose.',
            'difficulty': 'advanced',
        },
        {
            'image': 'https://images.unsplash.com/photo-1689634565113-f0833a2b073b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'title': 'Tarot Deck Cleanse',
            'description': 'It is important to cleanse your deck when you receive your deck or between reading.',
            'materials': ['tarot deck'],
            'instructions': 'Blow air around entire edges of deck. Set your intention with this deck. tap bottom of deck 3 times on wrist. Sleep with deck under pillow for one night.',
            'difficulty': 'beginner',
        },
        {
            'image': 'https://images.unsplash.com/photo-1607851555973-39e3fb1293ad?q=80&w=2065&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'title': 'New Moon Door Wash',
            'description': 'This cleanse is important to do on the day of a new moon. Do not forget to not only wash the door but also sweep the entry of dust, leaves cobwebs.',
            'materials': ['peppermint', 'alfalfa', 'comfrey', 'cinnamon'],
            'instructions': 'Steep all together for 5 minutes. Strain and cool. Wipe down door and door frame with cooled mixture.'
                'Blow cinnamon inside and say "When I blow this cinnamon endless health, wealth and abundance will continue to enter this home."'
                'Witch tip! If you have familiars or pets in the home. Do not blow cinnamon inside. Cinnamon can be toxic. Best alternative is to hang cinnamon sticks over door.',
            'difficulty': 'advanced',
        },
    ]

    for craft_info in CRAFT_DATA:
        new_craft = Craft(**craft_info)
        db.session.add(new_craft) 

    db.session.commit()

    for material_name in craft_info['materials']:
        material_instance = db.session.query(Materials).filter_by(name=material_name).first()
        if not material_instance:
            material_instance = Materials(name=material_name, quantity=10)
            db.session.add(material_instance)
        
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        clear_tables()
        seed_crafts()
        print("As you wish!")
    
    
