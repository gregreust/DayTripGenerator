from random import choice
from xxlimited import new

#destination options
destinations = ['Austin', 'New Orleans', 'San Antonio', 'Chicago', 'Atlanta', 'Santa Fe', 'Nashville', 'Washington DC']
#transportation options
transportations = ['plane', 'train', 'rental car', 'bus', 'scooter', 'horse', 'bicycle']
#entertainment options
entertainments = ['a concert', 'an art museum', 'a bar crawl', 'a shopping spree', 'a guided tour', 'a cooking class', 'the zoo', 'a farmer\'s market']
#dining options
austin_dining = ['Odd Duck', 'Launderette', 'ATX Cocina', 'Salty Sow', 'Jeffery\'s']
new_orleans_dining = ['Cochon', 'GW Fins', 'Commander\'s Palace', 'Peche Seafood Grill', 'Brennan\'s']
san_antonio_dining = ['Southerleigh', 'Fogo de Chão', 'Bliss', 'Bohanan\'s Prime Steaks and Seafood', 'Cappy\'s']
chicago_dining = ['The Purple Pig', 'Girl & The Goat', 'Boka', 'Monteverde', 'Alinea']
atlanta_dining = ['Poor Calvin\'s', 'South City Kitchen', 'Nan Thai', 'Lazy Betty', 'Sotto Sotto']
santa_fe_dining = ['The Shed', 'Marker Steer Steakhouse', 'Radish & Rye', 'Sassella', 'La Boca']
nashville_dining = ['Butcher & Bee', 'Etch', 'The Catbird Seat', 'Adele\'s', 'Kayne Prime Steakhouse']
washington_dc_dining = ['Estadio', 'The Dabney', 'Le Diplomate', 'Fiola Mare', 'Founding Farmers']

print('Let\'s plan a fun day trip!')

#selecting destination 
user_selection = ''
while user_selection != 'y':
    destination_pick = choice(destinations)
    print(f'The destination we have selected is {destination_pick}.')
    user_selection = input('Does that sound good? Enter y or n: ')
    if user_selection == 'y':
        print(f'Great! You are going to {destination_pick}.')
    elif user_selection == 'n':
        print('Okay, lets try a different option.')
    else:
        print('Error. Please enter y or n')

#selecting dining
user_selection = ''
while user_selection != 'y':
    if destination_pick == 'Austin':      #dining lists are specific to the destination
        dining_pick = choice(austin_dining)
    elif destination_pick == 'New Orleans':
        dining_pick = choice(new_orleans_dining)
    elif destination_pick == 'San Antonio':
        dining_pick = choice(san_antonio_dining)
    elif destination_pick == 'Chicago':
        dining_pick = choice(chicago_dining)
    elif destination_pick == 'Atlanta':
        dining_pick = choice(atlanta_dining)   
    elif destination_pick == 'Santa Fe':
        dining_pick = choice(santa_fe_dining)
    elif destination_pick == 'Nashville':
        dining_pick = choice(nashville_dining)
    elif destination_pick == 'Washington DC':
        dining_pick = choice(washington_dc_dining)

    print(f'You will be dining at {dining_pick}.')
    user_selection = input('Does that sound good? Enter y or n: ')
    if user_selection == 'y':
        print(f'Great! {dining_pick} has delicious food.')
    elif user_selection == 'n':
        print('Okay, lets try a different restaurant.')
    else:
        print('Error. Please enter y or n')

#selecting transportation
user_selection = ''
while user_selection != 'y':
    transportation_pick = choice(transportations)
    print(f'You will be travelling via {transportation_pick}.')
    user_selection = input('Is that okay? Enter y or n: ')
    if user_selection == 'y':
        print(f'Great! Your {transportation_pick} will be ready shortly.')
    elif user_selection == 'n':
        print('Okay, lets try a different option.')
    else:
        print('Error. Please enter y or n')

#selecting entertainent
user_selection = ''
while user_selection != 'y':
    entertainment_pick = choice(entertainments)
    print(f'Your entertainment for the day will be {entertainment_pick}.')
    user_selection = input('Does that sound fun? Enter y or n: ')
    if user_selection == 'y':
        print(f'Great! We hope you have fun at {entertainment_pick}.')
    elif user_selection == 'n':
        print('Okay, lets try a different option.')
    else:
        print('Error. Please enter y or n')

