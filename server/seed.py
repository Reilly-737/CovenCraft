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
            'title': 'Happy Home Oil',
            'description': 'This happy home oil is a fantastic home spell to use between new moon cleanses! Keep your home running smoothly harmoniously and peacefully.',
            'materials': ['gardenia', 'myrrh', 'coconut oil', 'salt', 'five finger grass'],
            'instructions': 'Add all materials together and place droplets around the house or dress candles with oil.',
            'difficulty': 'beginner',
        },
        {
            'title': 'Rosemary Infusion of Power',
            'description': 'Washing hands with an infusion of rosemary magickally empowers and enhances all healing. '
                'Healing spells are not intended to be used in place of traditional or conventions methods of healing'
                'They work best in conjunction with them as reinforcement.',
            'materials': ['rosemary', 'strainer', 'small bottle'],
            'instructions': 'Create a infusion by pouring boiling water over rosemary. Allow it to cool then strain. This may be done prior to healing or liquid can be bottled and refrigerated for use later.',
            'difficulty': 'beginner',
        },
        {
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
            'title': 'Hydrangea Hex Reversal',
            'description': 'Hexes happen! This easy hex remover is very handy to have on hand.',
            'materials': ['dried hydrangeas', 'fire-safe cauldron'],
            'instructions': 'Burn died Hydrangea to reverse spells and remove hexes. Blend the ashes with more dried ground hydrangea and scatter around the home.',
            'difficulty': 'intermediate',
        },
        {
            'title': 'Begone Banish Powder',
            'description': 'Banishing spells remove something or someone from your presence often permanently. '
                'This powder can also be used as an accompaniment for spells particularly around or over candles',
            'materials': ['black pepper', 'cayenne pepper', 'cinnamon', 'salt', 'sulfur'],
            'instructions': 'Sprinkle the banishing powder on clothes, especially belonging to anyone you would like to see gone(without wishing harm to them).',
            'difficulty': 'intermediate',
        },
        {
            'title': 'Low Energy Spell',
            'description': 'Drained? Just want to get back into bed? Try this spell to get that pep back in your step.',
            'materials': ['sliced lemon', 'salt', 'rosemary'],
            'instructions': 'Take sliced lemon sprinkle salt over slice then pair rosemary sprig. Place under bed. Shelf life of one night to one week.',
            'difficulty': 'beginner',
        },
        {
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
            'title': 'Tarot Deck Cleanse',
            'description': 'It is important to cleanse your deck when you receive your deck or between reading.',
            'materials': ['tarot deck'],
            'instructions': 'Blow air around entire edges of deck. Set your intention with this deck. tap bottom of deck 3 times on wrist. Sleep with deck under pillow for one night.',
            'difficulty': 'beginner',
        },
        {
            'title': 'New Moon Door Wash',
            'description': 'This cleanse is important to do on the day of a new moon. Do not forget to not only wash the door but also sweep the entry of dust, leaves cobwebs.',
            'materials': ['peppermint', 'alfalfa', 'comfrey', 'cinnamon'],
            'instructions': 'Steep all together for 5 minutes. Strain and cool. Wipe down door and door frame with cooled mixture.'
                'Blow cinnamon inside and say "When I blow this cinnamon endless health, wealth and abundance will continue to enter this home."'
                'Witch tip! If you have familiars or pets in the home. Do not blow cinnamon inside. Cinnamon can be toxic. Best alternative is to hang cinnamon sticks over door.',
            'difficulty': 'advanced',
        },
           {
            'craft_id': 11,
            'title': 'Dream Enhancing Tea',
            'description': 'Need to make a difficult decision? Curious about the other side? Drink and feel deeply with this tea.',
            'materials': 'Mugwort, Chamomile, Peppermint',
            'instructions': 'Brew a tea using equal parts of mugwort, chamomile and peppermint. Drink it before betime to enhance dreams and intuition.',
            'difficulty': 2,
        },
        {
            'craft_id': 12,
            'title': 'Healing Herbal Sachet',
            'description': 'For Witches and friends of that need an extra boost.',
            'materials': 'Lavender, Rosemary, Chamomile, Cotton bag',
            'instructions': 'Combine equal parts in a small cotton bag. Carry it with you or place it under your pillow for healing energy.',
            'difficulty': 3,
        },
        {
            'craft_id': 13,
            'title': 'Prosperity Spell Jar',
            'description': 'Create and attract prosperity with this jar!',
            'materials': 'Green Candle, Bay leaves, Cinnamon Sticks, Citrine Crystal, Small Jar',
            'instructions': 'Place bay leaves cinnamon stick, and citrine crystal in a jar. Light a green candle and focus on attracting prosperity. Seal the jar and keep in your home.',
            'difficulty': 4,
        },
        {
            'craft_id': 14,
            'title': 'Cleansing Bath Salt',
            'description': 'Best done on Full Moon. Cleanse body, mind and soul with this bath.',
            'materials': 'epsom Salt, Sea Salt, Lavender Essential Oil',
            'instructions': 'Mix Epsom salt and sea salt with a few drops of lavender essential oil. Add the mixture to your bath for a cleansing and purifying experience',
            'difficulty': 2,
        },
        {
            'craft_id': 15,
            'title': 'Divination Oil',
            'description': 'A beginners divination oil! Easy and perfect for baby witches.',
            'materials': 'Frankincense, Myrrh, Jojoba Oil',
            'instructions': 'Create oil by mixing frankincense and myrrh with jojoba oil. Use it to anoint divination tools or your forehead before practicing divination.',
            'difficulty': 1,
        },
        {
            'craft_id': 16,
            'title': 'Grounding Incense Blend',
            'description': 'This is a wonderful craft to add to your own practice. ',
            'materials': 'Sandalwood, Patchouli, Myrrh',
            'instructions': 'Blend sandalwood, patchouli and myrrh to create an incense. Burn it during meditation or rituals to promote grounding and centering.',
            'difficulty': 2,
        },
        {
            'craft_id': 17,
            'title': 'Steel Wool Talisman',
            'description': 'An alternative to the evil eye. Has a shelf life of about 6 months. This talisman will keep your energy safe. ',
            'materials': 'Steel Wool, Small cotton bag',
            'instructions': 'Place a piece of steel wool in a small cotton bag. Carry it with you to absorb and neutralize negative energies around you.',
            'difficulty': 5,
        },
        {
            'craft_id': 18,
            'title': 'Thistle and Nettles Tea',
            'description': 'Drink this tea for vitality, strength and a boost in your immune system.',
            'materials': 'Thistle, Nettles',
            'instructions': 'Brew equal amounts into tea. Let steep for 5 minutes before drinking. Stir tea counter clockwise with your health intention.',
            'difficulty': 1,
        },
        {
            'craft_id': 19,
            'title': 'Hydrangea Hex-Breaking Spell',
            'description': 'Remove hexes with this spell. Not for beginners.',
            'materials': 'Dried Hydrangeas, Thorns, Steel Wool',
            'instructions': 'Burn all listed materials in small bowl to break hexes and remove negative energy. Scatter the ashes around your home.',
            'difficulty': 5,
        },
        {
            'craft_id': 20,
            'title': 'Coconut Oil Spell Candle',
            'description': 'This candle is a perfect swiss-army knife of spells. Can be used for love, protection, prosperity etc.',
            'materials': 'Coconut Oil, Small Candle',
            'instructions': 'Dress a small candle with coconut oil. Light the candle, focusing on your intentions.',
            'difficulty': 1,
        },
          {
            'craft_id': 21,
            'title': 'Five Finger Grass Talisman',
            'description': 'A little talisman to carry for good luck and positive energy',
            'materials': 'Five Finger Grass, Small Cloth',
            'instructions': 'Place fiver finger grass in a small cloth and tie it with a string. Carry it with you for good luck and positive energy.',
            'difficulty': 1,
        },  
        {
            'craft_id': 22,
            'title': 'Protection Sachet',
            'description': 'A small sachet to protect you from negativity ',
            'materials': 'Hydrangea Petals, thorns, Small pouch',
            'instructions': 'Combine hydrangea petals and thorns in a small pouch. Carry it with you or place it in your home for protection against negativity.',
            'difficulty': 1,
        },
        {
            'craft_id': 23,
            'title': 'Familiar Protection Jar',
            'description': 'Protect your familiar with this jar.',
            'materials': 'Basil, Five Finger Grass, Thistle, Coconut Oil, Small Jar, Hair from familiar',
            'instructions': 'Place all materials in jar. Hold in hands tightly and focus on intention. Seal jar. Holds for 3 months.',
            'difficulty': 3,
        },
          {
        'craft_id': 24,
        'title': 'Unity Energy Crystal Grid',
        'description': 'A crystal grid designed to harness and amplify the collective energy of the coven, promoting unity, protection, and manifestation.',
        'materials': 'Clear Quartz Points, Amethyst, Rose Quartz, Citrine, Selenite, Black Tourmaline, Small cloth bags(one for each witch), One small personal item for each witch',
        'instructions': '''Begin by placing all the crystals in the center of your sacred space. Each witch can bring a personal item or symbol to infuse their energy into the grid.
As a group, set a collective intention for the crystal grid. This could be unity, protection, manifestation of shared goals, or any other positive intention.
Assign different crystals to each witch or let them choose based on their intuition. Place the crystals in a geometric pattern that resonates with the group's energy. You can use a predefined pattern or create your own.
Each witch takes a turn placing their personal item or symbol in the center of the crystal grid, infusing it with their energy and intention.
Once all items are placed, join hands and visualize a bright, unified energy flowing through the crystals and connecting everyone in the circle. Speak words of power, chant, or perform a brief ritual to activate the grid.
Conclude the ritual by acknowledging the shared energy and sealing the intention. Each witch takes their small cloth bag and places the crystals and their personal item inside. This bag becomes a personal talisman connected to the group's energy.
Sit in meditation together, focusing on the energy of the crystal grid and the collective intention. Feel the unity and connection within the group.
Thank the spirits, elements, or deities you work with, and close the circle. Each witch takes their personal bag home, carrying the unified energy with them.''',
        'difficulty': 3,
    },
    {
        'craft_id': 25,
        'title': 'Coven Manifestation Candle',
        'description': ' A collaborative spell candle designed to manifest shared goals and desires.',
        'materials': 'One Large Pillar Candle, Carving tools, Corresponding Herbs for Group Intention, Anointing Oil, Small Cloth for each witch',
        'instructions': '''Gather the coven and discuss the shared goals and desires you want to manifest. Agree on a specific intention for the candle spell.
Pass the large candle around, and each witch carves symbols, words, or intentions into the wax. Encourage creativity and intuition.
As a group, rub the candle with anointing oil and then roll it in a mixture of the selected herbs. This infuses the candle with the energies corresponding to your intention.
Each witch ties a small cloth square or ribbon around the candle, adding their personal energy and intention. They can also attach symbols representing their wishes.
Place the candle in the center of your sacred space. Form a circle around it and hold hands. Visualize the shared goal coming to fruition. Chant, sing, or speak words of power to charge the candle.
Light the candle together, focusing on the flame and the collective energy imbued in the wax.
Thank the energies and entities involved, and formally close the ritual. Encourage witches to keep the remnants of the candle, such as the wax pool or the cloth, as a reminder of the shared manifestation.''',
        'difficulty': 2,
    },
    {
        'craft_id': 26,
        'title': 'Full Moon Broom Crafting Initiation',
        'description': 'A ritual where new coven members craft their own besom (witch\'s broom) under the light of the full moon, symbolizing initiation, unity, and the sweeping away of old energies.',
        'materials': 'Broom Handles or branches, Twine, Purification Herbs, Colored Ribbons or Cloth Strips, Charms, Full Moon Blessing oil, Moonwater, Decorative elements important to witch',
        'instructions': '''Schedule the ritual to begin at moonrise. Members gather in a sacred space outdoors where the full moon is visible.
The coven leader or High Priestess opens the sacred circle, invoking the energies of the full moon and the elements. Members stand in a circle, holding hands.
If there's a new member, welcome them to the coven and explain the significance of crafting their own besom as a symbol of initiation.
Pass around the broom handles or branches. Each member, including the new initiate, holds their broom handle while the group collectively blesses them with moonwater, stating intentions for unity, protection, and magical prowess.
In a communal act, the coven purifies the broom handles with smoke from burning herbs (sage, rosemary, lavender). This symbolizes the removal of negative energies and the preparation for new beginnings.
Members decorate their broom handles with colored ribbons, charms, and other personal items. Each element added represents an aspect of the witch's magical identity.
The besom handles are anointed with Full Moon Blessing Oil. Each member, including the new initiate, receives a few drops on their broom, symbolizing the blessing of the full moon.
Members bind their broom handles with twine or rope, further sealing the intentions and magic within. The coven chants or recites a blessing during this process.
Members place their besoms in an arrangement under the full moon. The coven stands in a circle around the besoms, channeling energy and intentions into the newly crafted tools.
As a celebration of unity and initiation, the coven may choose to engage in a dance or movement under the moonlight, raising energy and joy.
The coven leader or High Priestess closes the circle, thanking the moon and the elements. Each member, now with their personalized besom, is officially initiated into the coven.
Conclude the ceremony with a shared feast or refreshments, fostering a sense of community and bonding among coven members.''',
        'difficulty': 1,
    },
    {
        'craft_id': 27,
        'title': 'Moonwater Spell',
        'description': 'Using in so many spells. Moonwater is an essential.',
        'materials': 'Small jar, One cup of water',
        'instructions': 'Place a glass of water under the full moon overnight, visualizing its energy infusing the water. In the morning, collect the charged Moonwater for use in magical workings.',
        'difficulty': 1,
    },
     {
        'craft_id': 28,
        'title': 'Fullmoon Blessing Oil Spell',
        'description': 'Another witch essential to have on hand!',
        'materials': 'Jasmine, Yiang-Yiang, Sandalwood, Clear Quartz Crystal, Sweet Almond Oil, Small jar',
        'instructions': 'On the night of the full moon, add moon-associated essential oils to a carrier oil, placing the mixture under moonlight overnight. Strain (if needed) and use the Full Moon Blessing Oil to anoint and bless, infusing it with positive energies.',
        'difficulty': 2,
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
    
    
