#!/usr/bin/env python3

def showInstructions():
    #print a main menu and the commands
    print('''
    RPG Game
    =========
    Commands:
    go [direction]
    get [item]
    ''')

def showStatus():
    #print the player's current status
    print('--------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("-------------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other room
rooms = {
            'Hall' : {
                    'south' : 'Kitchen',
                    'east' : 'Dining Room', 
                    'item' : 'key'
                }, 
            'Kitchen' : {
                    'north' : 'Hall',
                    'item' : 'monster', 
                }, 
            'Dining Room' : {
                    'west' : 'Hall',
                    'south' : 'Garden',
                    'north' : 'Bedroom',
                    'item' : 'potion'
                }, 
            'Garden' : {
                    'north' : 'Dining Room'
                }, 
            'Bedroom' : {
                    'south': 'Dining Room', 
                    'west' : 'Hidden Room',
                    'item' : 'mirror'
                }, 
            'Hidden Room' : {
                    'west' : 'Hall', 
                    'item' : 'treasure'
                }
        }
#start the player in the Hall
currentRoom = 'Hall'
showInstructions()
#loop forever
while True:
    showStatus()
    #get the player's next move
    #.split() breaks it up into a list array
    #eg typing go east would give the list:
    #['go','east']
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go 
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get':
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room 
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get 
        else:
            #tell them they can't get it 
            print('Can\'t get ' + move[1] + '!')

    #if you have the mirror when you face the monster 
    if 'mirror' in inventory and 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('The monster is a Gorgon so you use the mirror to turn it into stone!')
        inventory.remove('mirror')
        del rooms[currentRoom]['item']

    ##If a player enters a room with a monster 
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you.... Game Over!')
        break

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory and 'treasure' in inventory:
        print("You escaped the house with the key, potion, and the monster's treasure!")
        break

    ##Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion.... YOU WIN!')
        break
