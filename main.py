from random import choice

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

def main_app():
    print('Let\'s plan a fun day trip!')

    destination_pick = user_chooses_option(destinations, 'destination')
    dining_pick = user_chooses_dining(destination_pick)
    transportation_pick = user_chooses_option(transportations, 'transportation')
    entertainment_pick = user_chooses_option(entertainments, 'entertainment')

    print(f'Here is your final itinerary: \n You are travelling to {destination_pick} via {transportation_pick}. \n You will experience {entertainment_pick} and have a nice dinner at {dining_pick}.')
    

def rand_item_from_list(string_list):
    return choice(string_list)

def user_chooses_option(string_list, type_of_choice):
    user_y_or_n = ''
    copy_of_list = string_list
    while user_y_or_n != 'y':
        user_decision = rand_item_from_list(copy_of_list)
        print(f'The {type_of_choice} we have selected is {user_decision}.')
        user_y_or_n = input('Does that sound good? Enter y or n: ')
        if user_y_or_n == 'y':
            print(f'Great! You are going to {user_decision}.')
        elif user_y_or_n == 'n':
            print('Okay, lets try a different option.')
            if len(copy_of_list) == 1:  #preventing stopping the program if no options left
                print('Make up your mind!')
                copy_of_list = string_list
            copy_of_list.remove(user_decision)  #remove the already displayed option so user doesn't get it twice
        else:
            print('Error. Please enter y or n')
    return user_decision

def user_chooses_dining(destination_string):
    if destination_string == 'Austin':
        return user_chooses_option(austin_dining, 'restaurant')
    elif destination_string == 'New Orleans':
        return user_chooses_option(new_orleans_dining, 'restaurant')
    elif destination_string == 'San Antonio':
        return user_chooses_option(san_antonio_dining, 'restaurant')
    elif destination_string == 'Chicago':
        return user_chooses_option(chicago_dining, 'restaurant')
    elif destination_string == 'Atlanta':
        return user_chooses_option(atlanta_dining, 'restaurant')
    elif destination_string == 'Santa Fe':
        return user_chooses_option(santa_fe_dining, 'restaurant')
    elif destination_string == 'Nashville':
        return user_chooses_option(nashville_dining, 'restaurant')
    elif destination_string == 'Washington DC':
        return user_chooses_option(washington_dc_dining, 'restaurant')

def confirm_itinerary():
    user_selection = ''
    while user_selection != 'y' and user_selection != 'n':     
        user_selection = input('Does everything look good? Enter y or n: ')
        if user_selection == 'y':
            print ('Awesome! Enjoy your trip.')
            return True
        elif user_selection == 'n':
            print('Sorry, let\'s try again.')
            return False
        else:
            print('Error. Please enter y or n: ')


is_user_satisfied = False
while is_user_satisfied != True:
    main_app()
    is_user_satisfied = confirm_itinerary()



