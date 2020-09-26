# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:48:10 2020

@author: sanju
"""

#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    #print a main menu and the commands
    print('''
Intelligence Report says that this house is being used by Terrorist as their hide out spot. Currently they have hostages of high 
========
Commands:
  go [direction]
  get [item]
''')

def showStatus(number_of_moves, currentRoom, inventory):
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print('Move count: ' + str(number_of_moves))
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        uSee(currentRoom)
        if "mystery box" in rooms[currentRoom]:
            print('You see ' + str(rooms[currentRoom]['item']['mystery box']))
    print("---------------------------")
                
            
def uSee(currentRoom):
    print('You see ' + str(list(rooms[currentRoom]['item'])))
    


#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : {'key':'', 'comb':'','mystery box': {'1':'knife', '2':'m4', '3':'hand grenade','opened': False}},
                  #sanju added list
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : {'frankenstien'},
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item'  : {'torch':'', 'comb':'','mystery box': {'1':'m16', '2':'flash bang', '3':'smoke', 'opened': False}},
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'weapon': ['tank', 'M24'],
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : {'cookie dough', 'raw noodles', 'expired chips'},
            }
         }


#open objects and prints the content
def openIt(currentRoom,elem):
    items = rooms[currentRoom]['item']
    if elem in items and elem == 'mystery box':
        print("---------------------------")
        visibleItems = list(rooms[currentRoom]['item']['mystery box'].values())[0:3]
        rooms[currentRoom]['item']['mystery box']['opened'] = True 
        print("You found " + str(visibleItems))
    else:
        print("seriously? Go get a job")
              
def go(currentRoom, elem):
     #check that they are allowed wherever they want to go
     if elem in rooms[currentRoom]:
         #set the current room to the new room
         return rooms[currentRoom][elem]       
         #there is no door (link) to the new room
     else:
            print('You can\'t go that way!')

def main():
    #start the player in the Hall
    currentRoom = 'Hall'
    #visibleItems = rooms[currentRoom]['item']

    showInstructions()
    
    #an inventory, which is initially empty
    inventory = []

    number_of_moves = 0       
    #loop forever
    while True:
        showStatus(number_of_moves, currentRoom, inventory)
        number_of_moves +=1
        #get the player's next 'move'
        #.split() breaks it up into an list array
        #eg typing 'go east' would give the list:
        #['go','east']
        move = ''
        while move == '':
            move = input('Make the Next Move >> ')
    
        # split allows an items to have a space on them
        # get golden key is returned ["get", "golden key"]          
        move = move.lower().split(" ", 1)
        
        #if they type 'open' first
        if move[0] == 'open':
            openIt(currentRoom, move[1])
            
            #print(rooms[currentRoom]['item']['mystery box'])    
        #if they type 'go' first
        if move[0] == 'go':
            currentRoom = go(currentRoom, move[1])
    
        #if they type 'get' first
        if move[0] == 'get' :
            #if the room contains an item, and the item is the one they want to get
            if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                #print("its inside weapon")
                #add the item to their inventory
                inventory += [move[1]]
                #display a helpful message
                print(move[1] + ' got!')
                #delete the item from the room
                itempointer = rooms[currentRoom]['item']
                del itempointer[itempointer.index(move[1])]
                #del rooms[currentRoom]['item'][move[1]]
                #otherwise, if the item isn't there to get
          
            elif "weapon" in rooms[currentRoom] and move[1] in rooms[currentRoom]['weapon']:
                #print('its inside weapon')
                #add the item to their inventory
                inventory += [move[1]]
                #display a helpful message
                print(move[1] + ' got!')
                #delete the item from the room
                itempointer = rooms[currentRoom]['weapon']
                del itempointer[itempointer.index(move[1])]
            else:
                #tell them they can't get it
                print('Can\'t get ' + move[1] + '!')
    
        ## Define how a player can win
        if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
            print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
            break
    
        ## If a player enters a room with a monster BUT HAS A COOKIE
        if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'cookie' in inventory:
            print('The monster takes your cookie and runs away! Whew!')
            del rooms[currentRoom]['item']
            inventory.remove('cookie')
    
        ## If a player enters a room with a monster
        elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
            print('A monster has got you... GAME OVER!')
            break

if __name__ == '__main__': 
    main() 
