from app import app, db
from model import  CraftMaterial, Materials
from craft import  Craft

def clear_tables():
    print("Clearing database...")
    with app.app_context():
        db.drop_all()
        db.create_all()

def seed_crafts():
    print("Adding crafts...")

    CRAFT_DATA = [
        
        {
            'craft_id': 0,
            'title': 'title',
            'description': 'description',
            'materials': 'materials',
            'instructions': 'instructions',
            'difficulty': 0,
        },
        {
            'craft_id': 1,
            'title': 'Witch Protection Bottle',
            'description': 'Protection spells will protect you from malicious spells, hexes or negative enchantments cast deliberately against you by another.',
            'materials': 'One small jar, Broken Glass, Nails, Thorns, Steel Wool, Wormwood, Thistle, Nettles, Vinegar, Salt, One Black Candle',
            'instructions': 'Fill jar with items listed and seal tightly. On top of the lid draw a pentacle. Place the black candle on the lid and light it. '
                             'Chant the following over the candle:'
                             'Candle of the black and hexes old Release the powers that you hold '
                             'Reverse the flow of spells once cast Leave pain and sorrow in the past. '
                             'Let the candle burn out. Take the jar and bury it in the earth close to your home, '
                             'Has a shelf life of six months',
            'difficulty': 3,
        },
        {
            'craft_id': 2,
            'title': 'Happy Home Oil',
            'description': 'This happy home oil is a fantastic home spell to use between new moon cleanses! Keep your home running smoothly harmoniously and peacefully.',
            'materials': 'Gardenia, Myrrh, Coconut Oil, Pinch Of Salt, Five Finger Grass',
            'instructions': 'Add all materials together and place droplets around the house or dress candles with oil.',
            'difficulty': 2,
        },
        {
            'craft_id': 3,
            'title': 'Rosemary Infusion of Power',
            'description': 'Washing hands with an infusion of rosemary magickally empowers and enhances all healing. '
                            'Healing spells are not intended to be used in place of traditional or conventions methods of healing'
                            'They work best in conjunction with them as reinforcement.',
            'materials': 'Rosemary, Strainer, Small bottle or soap dispenser',
            'instructions': 'Create a infusion by pouring boiling water over rosemary. Allow it to cool then strain. This may be done prior to healing or liquid can be bottled and refrigerated for use later.',
            'difficulty': 1,
        },
        {
            'craft_id': 4,
            'title': 'Prosperity Basil Bath Spell',
            'description': 'The scent of basil on the skin attracts financial good fortune to the wearer. Take this bath before engaging in any interaction revolving around your finances.',
            'materials': 'Roughly chopped basil, Pot of Boiling water, One small bag',
            'instructions': 'Roughly chop most of the basil in order to release the volatile oils. You must leave some of the leaves whole. Then pour boiling water over the basil and let it steep.,'
                             'When it\'s cooled add this to your bath. Float the whole leaves in the water and visualize yourself swimming in cash.,'
                             'Let the water drain and allow yourself to air dry.'
                             'Do not dispose the used basil leaves but either leave them in the tub until your transactions are complete or remove them place in bag and '
                             'reserve until an opportune moment for disposal arises.',
            'difficulty': 5,
        },
        {
            'craft_id': 5,
            'title': 'Hydrangea Hex Reversal',
            'description': 'Hexes happen! This easy hex remover is very handy to have on hand.',
            'materials': 'Dried Hydrangeas',
            'instructions': 'Burn died Hydrangea to reverse spells and remove hexes. Blend the ashes with more dried ground hydrangea and scatter around the home.',
            'difficulty': 5,
        },
        {
            'craft_id': 6,
            'title': 'Begone Banish Powder',
            'description': 'Banishing spells remove something or someone from your presence often permanently. '
                            'This powder can also be used as an accompaniment for spells particularly around or over candles',
            'materials': 'Black peppers, Cayenne Pepper, Cinnamon, Sea Salt, Sulfur',
            'instructions': 'Sprinkle the banishing powder on clothes, especially belonging to anyone you would like to see gone(without wishing harm to them).',
            'difficulty': 3,
        },
        {
            'craft_id': 7,
            'title': 'Low Energy Spell',
            'description': 'Drained? Just want to get back into bed? Try this spell to get that pep back in your step.',
            'materials': 'One sliced lemon, Sprinkle of salt, Sprig of rosemary',
            'instructions': 'Take sliced lemon sprinkle salt over slice then pair rosemary sprig. Place under bed. Shelf life of one night to one week.',
            'difficulty': 1,
        },
        {
            'craft_id': 8,
            'title': 'Freeze Spell',
            'description': 'Do you need space? A moment or day without the presence of a certain someone or something? This spell is to create space and \'freeze them\'',
            'materials': 'One bay leaf, One cup of water',
            'instructions': 'Boil water. Write the name of the something/someone on leaf. Imagine them at peace and not thinking of you. '
                            'Dip leaf in water. Take leaf out of water and dump water out back door. Place leaf in freezer. '
                            'Practice a self-care routine or mediate on what feelings are rising. '
                            'Take leaf out when finished and dispose.',
            'difficulty': 2,
        },
        {
            'craft_id': 9,
            'title': 'Tarot Deck Cleanse',
            'description': 'It is important to cleanse your deck when you receive your deck or between reading.',
            'materials': 'Tarot Deck',
            'instructions': 'Blow air around entire edges of deck. Set your intention with this deck. tap bottom of deck 3 times on wrist. Sleep with deck under pillow for one night.',
            'difficulty': 1,
        },
        {
            'craft_id': 10,
            'title': 'New Moon Door Wash',
            'description': 'This cleanse is important to do on the day of a new moon. Do not forget to not only wash the door but also sweep the entry of dust, leaves cobwebs.',
            'materials': 'Peppermint, Alfalfa, Comfrey Leaf, Ground or whole cinnamon sticks',
            'instructions': 'Steep all together for 5 minutes. Strain and cool. Wipe down door and door frame with cooled mixture.'
                            'Blow cinnamon inside and say "When I blow this cinnamon endless health, wealth and abundance will continue to enter this home."'
                            'Witch tip! If you have familiars or pets in the home. Do not blow cinnamon inside. Cinnamon can be toxic. Best alternative is to hang cinnamon sticks over door.',
            'difficulty': 3,
        },
    ]

    for craft_info in CRAFT_DATA:
        craft = CraftMaterial(
            craft_id=craft_info['craft_id'],
            name=craft_info['title'],
            description=craft_info['description'],
            materials=craft_info['materials'],
            instructions=craft_info['instructions'],
            difficulty=craft_info['difficulty'],
        )
        db.session.add(craft) 

    db.session.commit()  

if __name__ == "__main__":
    with app.app_context():
        clear_tables()
        seed_crafts()
        print("As you wish!")
    
    
