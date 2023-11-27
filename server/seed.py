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
            
            'title': 'title',
            'description': 'description',
            'materials': 'materials',
            'instructions': 'instructions',
            'difficulty': 0,
        },
        {
            
            'title': 'Witch Protection Bottle',
            'description': 'Protection spells will protect you from malicious spells, hexes or negative enchantments cast deliberately against you by another.',
            'materials': ['One small jar, Broken Glass, Nails, Thorns, Steel Wool, Wormwood, Thistle, Nettles, Vinegar, Salt, One Black Candle'],
            'instructions': 'Fill jar with items listed and seal tightly. On top of the lid draw a pentacle. Place the black candle on the lid and light it. '
                             'Chant the following over the candle:'
                             'Candle of the black and hexes old Release the powers that you hold '
                             'Reverse the flow of spells once cast Leave pain and sorrow in the past. '
                             'Let the candle burn out. Take the jar and bury it in the earth close to your home, '
                             'Has a shelf life of six months',
            'difficulty': 'advanced',
        },
        {
            
            'title': 'Happy Home Oil',
            'description': 'This happy home oil is a fantastic home spell to use between new moon cleanses! Keep your home running smoothly harmoniously and peacefully.',
            'materials': ['Gardenia, Myrrh, Coconut Oil, Pinch Of Salt, Five Finger Grass'],
            'instructions': 'Add all materials together and place droplets around the house or dress candles with oil.',
            'difficulty': 'beginner',
        },
        {
            
            'title': 'Rosemary Infusion of Power',
            'description': 'Washing hands with an infusion of rosemary magickally empowers and enhances all healing. '
                            'Healing spells are not intended to be used in place of traditional or conventions methods of healing'
                            'They work best in conjunction with them as reinforcement.',
            'materials': ['Rosemary, Strainer, Small bottle or soap dispenser'],
            'instructions': 'Create a infusion by pouring boiling water over rosemary. Allow it to cool then strain. This may be done prior to healing or liquid can be bottled and refrigerated for use later.',
            'difficulty': 'advanced',
        },
        {
            
            'title': 'Prosperity Basil Bath Spell',
            'description': 'The scent of basil on the skin attracts financial good fortune to the wearer. Take this bath before engaging in any interaction revolving around your finances.',
            'materials': ['Roughly chopped basil, Pot of Boiling water, One small bag'],
            'instructions': 'Roughly chop most of the basil in order to release the volatile oils. You must leave some of the leaves whole. Then pour boiling water over the basil and let it steep.,'
                             'When it\'s cooled add this to your bath. Float the whole leaves in the water and visualize yourself swimming in cash.,'
                             'Let the water drain and allow yourself to air dry.'
                             'Do not dispose the used basil leaves but either leave them in the tub until your transactions are complete or remove them place in bag and '
                             'reserve until an opportune moment for disposal arises.',
            'difficulty': 'beginner',
        },
        {
          
            'title': 'Hydrangea Hex Reversal',
            'description': 'Hexes happen! This easy hex remover is very handy to have on hand.',
            'materials': ['Dried Hydrangeas'],
            'instructions': 'Burn died Hydrangea to reverse spells and remove hexes. Blend the ashes with more dried ground hydrangea and scatter around the home.',
            'difficulty': 'advanced',
        },
        {
            
            'title': 'Begone Banish Powder',
            'description': 'Banishing spells remove something or someone from your presence often permanently. '
                            'This powder can also be used as an accompaniment for spells particularly around or over candles',
            'materials': ['Black peppers, Cayenne Pepper, Cinnamon, Sea Salt, Sulfur'],
            'instructions': 'Sprinkle the banishing powder on clothes, especially belonging to anyone you would like to see gone(without wishing harm to them).',
            'difficulty': 'beginner',
        },
        {
           
            'title': 'Low Energy Spell',
            'description': 'Drained? Just want to get back into bed? Try this spell to get that pep back in your step.',
            'materials': ['One sliced lemon, Sprinkle of salt, Sprig of rosemary'],
            'instructions': 'Take sliced lemon sprinkle salt over slice then pair rosemary sprig. Place under bed. Shelf life of one night to one week.',
            'difficulty': 'beginner',
        },
        {
            
            'title': 'Freeze Spell',
            'description': 'Do you need space? A moment or day without the presence of a certain someone or something? This spell is to create space and \'freeze them\'',
            'materials': ['Bay leaves, One cup of water'],
            'instructions': 'Boil water. Write the name of the something/someone on leaf. Imagine them at peace and not thinking of you. '
                            'Dip leaf in water. Take leaf out of water and dump water out back door. Place leaf in freezer. '
                            'Practice a self-care routine or mediate on what feelings are rising. '
                            'Take leaf out when finished and dispose.',
            'difficulty': 'beginner',
        },
        {
          
            'title': 'Tarot Deck Cleanse',
            'description': 'It is important to cleanse your deck when you receive your deck or between reading.',
            'materials': ['Tarot Deck'],
            'instructions': 'Blow air around entire edges of deck. Set your intention with this deck. tap bottom of deck 3 times on wrist. Sleep with deck under pillow for one night.',
            'difficulty': 'beginner',
        },
        {
           
            'title': 'New Moon Door Wash',
            'description': 'This cleanse is important to do on the day of a new moon. Do not forget to not only wash the door but also sweep the entry of dust, leaves cobwebs.',
            'materials': ['Peppermint, Alfalfa, Comfrey Leaf, Ground or whole cinnamon sticks'],
            'instructions': 'Steep all together for 5 minutes. Strain and cool. Wipe down door and door frame with cooled mixture.'
                            'Blow cinnamon inside and say "When I blow this cinnamon endless health, wealth and abundance will continue to enter this home."'
                            'Witch tip! If you have familiars or pets in the home. Do not blow cinnamon inside. Cinnamon can be toxic. Best alternative is to hang cinnamon sticks over door.',
            'difficulty': 'advanced',
        },
           {
            
            'title': 'Dream Enhancing Tea',
            'description': 'Need to make a difficult decision? Curious about the other side? Drink and feel deeply with this tea.',
            'materials': ['Mugwort, Chamomile, Peppermint'],
            'instructions': 'Brew a tea using equal parts of mugwort, chamomile and peppermint. Drink it before betime to enhance dreams and intuition.',
            'difficulty': 'beginner',
        },
        {
            
            'title': 'Healing Herbal Sachet',
            'description': 'For Witches and friends of that need an extra boost.',
            'materials': ['Lavender, Rosemary, Chamomile, Cotton bag'],
            'instructions': 'Combine equal parts in a small cotton bag. Carry it with you or place it under your pillow for healing energy.',
            'difficulty': 'advanced',
        },
        {
            
            'title': 'Prosperity Spell Jar',
            'description': 'Create and attract prosperity with this jar!',
            'materials': ['Green Candle, Bay leaves, Cinnamon Sticks, Citrine Crystal, Small Jar'],
            'instructions': 'Place bay leaves cinnamon stick, and citrine crystal in a jar. Light a green candle and focus on attracting prosperity. Seal the jar and keep in your home.',
            'difficulty': 'advanced',
        },
        {
            
            'title': 'Cleansing Bath Salt',
            'description': 'Best done on Full Moon. Cleanse body, mind and soul with this bath.',
            'materials': ['Epsom Salt, Sea Salt, Lavender Essential Oil'],
            'instructions': 'Mix Epsom salt and sea salt with a few drops of lavender essential oil. Add the mixture to your bath for a cleansing and purifying experience',
            'difficulty': 'advanced',
        },
        {
            
            'title': 'Divination Oil',
            'description': 'A beginners divination oil! Easy and perfect for baby witches.',
            'materials': ['Frankincense, Myrrh, Jojoba Oil'],
            'instructions': 'Create oil by mixing frankincense and myrrh with jojoba oil. Use it to anoint divination tools or your forehead before practicing divination.',
            'difficulty': 'beginner',
        },
        {
           
            'title': 'Grounding Incense Blend',
            'description': 'This is a wonderful craft to add to your own practice. ',
            'materials': ['Sandalwood, Patchouli, Myrrh'],
            'instructions': 'Blend sandalwood, patchouli and myrrh to create an incense. Burn it during meditation or rituals to promote grounding and centering.',
            'difficulty': 'advanced',
        },
        {
            
            'title': 'Steel Wool Talisman',
            'description': 'An alternative to the evil eye. Has a shelf life of about 6 months. This talisman will keep your energy safe. ',
            'materials': ['Steel Wool, Small cotton bag'],
            'instructions': 'Place a piece of steel wool in a small cotton bag. Carry it with you to absorb and neutralize negative energies around you.',
            'difficulty': 'beginner',
        },
        {
            
            'title': 'Thistle and Nettles Tea',
            'description': 'Drink this tea for vitality, strength and a boost in your immune system.',
            'materials': ['Thistle, Nettles'],
            'instructions': 'Brew equal amounts into tea. Let steep for 5 minutes before drinking. Stir tea counter clockwise with your health intention.',
            'difficulty': 'advanced',
        },
        {
            
            'title': 'Hydrangea Hex-Breaking Spell',
            'description': 'Remove hexes with this spell. Not for beginners.',
            'materials': ['Dried Hydrangeas, Thorns, Steel Wool'],
            'instructions': 'Burn all listed materials in small bowl to break hexes and remove negative energy. Scatter the ashes around your home.',
            'difficulty': 'advanced',
        },
        {
            
            'title': 'Coconut Oil Spell Candle',
            'description': 'This candle is a perfect swiss-army knife of spells. Can be used for love, protection, prosperity etc.',
            'materials': ['Coconut Oil, Small Candle'],
            'instructions': 'Dress a small candle with coconut oil. Light the candle, focusing on your intentions.',
            'difficulty': 'beginner',
        },
          {
            
            'title': 'Five Finger Grass Talisman',
            'description': 'A little talisman to carry for good luck and positive energy',
            'materials': ['Five Finger Grass, Small Cloth'],
            'instructions': 'Place fiver finger grass in a small cloth and tie it with a string. Carry it with you for good luck and positive energy.',
            'difficulty': 'advanced',
        },  
        {
            
            'title': 'Protection Sachet',
            'description': 'A small sachet to protect you from negativity ',
            'materials': ['Hydrangea Petals, thorns, Small pouch'],
            'instructions': 'Combine hydrangea petals and thorns in a small pouch. Carry it with you or place it in your home for protection against negativity.',
            'difficulty': 'beginner',
        },
        {
            
            'title': 'Familiar Protection Jar',
            'description': 'Protect your familiar with this jar.',
            'materials': ['Basil, Five Finger Grass, Thistle, Coconut Oil, Small Jar, Hair from familiar'],
            'instructions': 'Place all materials in jar. Hold in hands tightly and focus on intention. Seal jar. Holds for 3 months.',
            'difficulty': 'advanced',
        },

        {
        
        'title': 'Moonwater Spell',
        'description': 'Using in so many spells. Moonwater is an essential.',
        'materials': ['Small jar, One cup of water'],
        'instructions': 'Place a glass of water under the full moon overnight, visualizing its energy infusing the water. In the morning, collect the charged Moonwater for use in magical workings.',
        'difficulty': 'beginner',
     },
     {
        
        'title': 'Fullmoon Blessing Oil Spell',
        'description': 'Another witch essential to have on hand!',
        'materials': ['Jasmine, Yiang-Yiang, Sandalwood, Clear Quartz Crystal, Sweet Almond Oil, Small jar'],
        'instructions': 'On the night of the full moon, add moon-associated essential oils to a carrier oil, placing the mixture under moonlight overnight. Strain (if needed) and use the Full Moon Blessing Oil to anoint and bless, infusing it with positive energies.',
        'difficulty': 'beginner',
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
    
    
