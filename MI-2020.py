# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:48:10 2020

@author: sanju
"""

#!/usr/bin/python3

import time
import datetime
import threading
import requests
import random
#import sys
import winsound
#from playsound import playsound
#import keyboard

def openWormHole(number_of_lives, number_of_moves):
    
    ## Define NEOW URL 
    NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"
    with open('C:/Users/sanju/Documents/TLG_python/mycode/nasa-creds.txt') as mycreds:
        nasacreds = mycreds.read()
        nasacreds = "api_key="+nasacreds.strip("\n")
        
        #randomly generate date
        date = generate_date()
        startdate = f"start_date={date}"
        neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds).json()
        #print(neowrequest)
        
    message ='''
Oh no!! You opened a wormhole . . . . 
You are as of now sitting back and relaxing . . . .
In front of you, you see a big ball . . . .
It is planet earth . . . .
You are on Mars . . . .
'''
    instruction =f'''
Today's date: {date} . . . .
Looks like you have travelled back in time . . . .
Some asteroids are headed towards Feeser Residence . . . .
Only way to travel back in future is to destroy all the asteroids . . . .
Choose and shoot wisely . . . .
        '''
    commands = '''
                        You will be using these commands 
                            to destroy the asteroids
                       ================================
                               load [asteroid]
                        shoot [v-150 Planet Defender]

                               
                                Goodluck !!
        '''
    winsound.PlaySound('typewriter.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
    typewriter(message, 0.02)
    winsound.PlaySound(None, winsound.SND_ASYNC)
    time.sleep(3)
    winsound.PlaySound('typewriter.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
    typewriter(instruction, 0.02)
    winsound.PlaySound(None, winsound.SND_ASYNC)
    time.sleep(3)
    winsound.PlaySound('typewriter.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
    typewriter(commands, 0.02)
    winsound.PlaySound(None, winsound.SND_ASYNC)
    time.sleep(2)
    
    wins = 0
    loss = 0
    while wins <= loss:
        list_of_asteroids = []
        list_of_velocity = []
        for i in range(len(neowrequest['near_earth_objects'][date])):
            list_of_asteroids.append(neowrequest['near_earth_objects'][date][i]['name'])
            list_of_velocity.append(neowrequest['near_earth_objects'][date][i]['close_approach_data'][0]['relative_velocity']['miles_per_hour'])
            
        # player getting ammo
        middle_of_asteroid_list = int(len(list_of_asteroids)/2)
        ai_list_of_asteroids = list_of_asteroids[:middle_of_asteroid_list]
        players_list_of_asteroids = list_of_asteroids[middle_of_asteroid_list:]
        
        #AI getting ammo
        middle_of_velocity_list = int(len(list_of_velocity)/2)
        ai_list_of_velocity = list_of_velocity[:middle_of_velocity_list]
        players_list_of_velocity = list_of_velocity[middle_of_velocity_list:]
        
        input("\nPress enter to continue ...\n")
        chamber=[]
        while True:
            number_of_moves +=1
            if number_of_moves/10 == number_of_lives:
                print("Terrorists have discovered your movements. Hostages are killed and you are fired..!! ")
                break
            print(f'Asteroid Ammo list: {players_list_of_asteroids}')
            print(f'Chamber : {chamber}')
            print(f'Total domination : {wins}')
            move = input("Make the next move >>")
            move = move.lower().split(" ", 1)
            print(move[1])
            if move[0] == 'load':
                if len(chamber) != 0:
                    print('Only one asteroid can be loaded at a time...')
                else:
                    if move[1].upper() in players_list_of_asteroids:
                        chamber.append(move[1].upper())
                        print('Asteroid loaded')
            elif move[0] == 'shoot':
                if len(chamber) == 0:
                    print('Asteroids not loaded yet...')
                elif move[1].upper() in chamber:
                    v1 = players_list_of_velocity[players_list_of_asteroids.index(move[1].upper())]
                    v2 = ai_list_of_velocity[0]
                    print('Shot fired !!')
                    winsound.PlaySound('Asteroid_Launch.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
                    time.sleep(2)
                    winsound.PlaySound(None, winsound.SND_ASYNC)
                    print(f'Your asteroid {move[1]}, travelled {v1} miles per hour')
                    print(f'{ai_list_of_asteroids[0]}, travelled {v2} miles per hour')
                    
                    if(float(v1) > float(v2)):
                        winsound.PlaySound('Explosion.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
                        time.sleep(2)
                        winsound.PlaySound(None, winsound.SND_ASYNC)
                        wins +=1
                        print("You smashed the asteroid in space. Great work")
                    elif(float(v1) < float(v2)):
                        loss +=1
                        print("Asteroid reached Feeser Residence on earth")
                    else:
                        print("Asses reached the earth's atmosphere")
                        
                    #remove from chamber
                    chamber.pop(0)
                    #remove from velocity list
                    players_list_of_velocity.pop(players_list_of_asteroids.index(move[1].upper()))
                    #remove from asteriod list
                    players_list_of_asteroids.remove(move[1].upper())
                    ai_list_of_velocity.pop(0)
                    ai_list_of_asteroids.pop(0)
                    if len(ai_list_of_asteroids) == 0:
                        break
            else:
                print('Doesn\'t seem to work !!')           
        
def generate_date():
     year =  str(random.randint(1900,2021))
     #year_twodigit = year[2:-1]
     month = str(random.randint(1,12)).zfill(2)
     day = str(random.randint(1,31)).zfill(2)
     try:
         datetime.datetime(int(year), int(month), int(day))
         return f'{year}-{month}-{day}'
         #print(f'{year}-{month}-{day} is valid')
     except ValueError:
         generate_date()
         #print(f'{year}-{month}-{day} is invalid')

# Replace RPG starter project with this code when new instructions are live
def typewriter(message,delay=0.01):
    for character in message:
        print(character,end="")
        time.sleep(delay)
    print("")
  
def showInstructions():
    #print a main menu and the commands
    header_message = ('''
                                 =============
                                 |  MI-2020  |
                                 =============
        ''')
    objective_message = ('''
Intelligence Report says that Feeser Residence is being used by Terrorist
as their hide out spot. President is held hostage somewhere in the house.
Your mission is to command your one man team to extract the hostage of high 
priority, and destroy the hide out. 
=============================================================================
''')
    command_message = (''' 
                       You will be using these commands 
                               to lead your team:
                       ================================
                               go [direction]
                               get [item]
                               open [item]
                               shoot [item]
''')
    winsound.PlaySound('typewriter.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
    typewriter(header_message, 0.02)
    time.sleep(1)
    winsound.PlaySound('typewriter.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
    typewriter(objective_message, 0.02)
    winsound.PlaySound(None, winsound.SND_ASYNC)
    time.sleep(2)
    winsound.PlaySound('typewriter.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
    typewriter(command_message, 0.02)
    time.sleep(2)
    winsound.PlaySound(None, winsound.SND_ASYNC)
    print('''                               
                                Goodluck !!''')
    time.sleep(1)
    print('')
    #winsound.PlaySound('mi-beat', winsound.SND_ASYNC | winsound.SND_LOOP)
    
def showStatus(number_of_lives, number_of_moves, currentRoom, inventory):
    #print the player's current status
    print('------------------------------------------')
    print('You are in the ' + currentRoom)
    print('Remaining lives: ' + str(number_of_lives))
    print('Move count: ' + str(number_of_moves))
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        uSee(currentRoom)
        if "mystery box" in rooms[currentRoom]:
            print('You see ' + str(rooms[currentRoom]['item']['mystery box']))
    print("-----------------------------------------")
                
            
def uSee(currentRoom):
    print('You see ' + str(list(rooms[currentRoom]['item'])))
    
#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : {
                      'master key':{
                          'grabbable': True,
                          'grabbed': False
                          }, 
                      'door':{
                          'east door': {
                              'content': 'a dinosaur, and you got eaten',
                              'impact' : '3',
                              'opened': False,
                              'grabbable': False,
                              'dependency': 'master key',
                              'hostile' : 'n/a'
                              },
                          'west door': {
                              'content':'passcode',
                              'impact':'0',
                              'opened': False,
                              'grabbable': False,
                              'dependency': 'master key',
                              'hostile': False
                              },
                          'south door': {
                              'content': '2 Hajis pointing m16s at you.',
                              'impact':'1',
                              'opened':False,
                              'grabbable':False,
                              'dependency': 'master key',
                              'hostile': True
                              },
                          'opened': False,
                          'impact': '0',
                          'grabbable' :'False'
                          },
                      'mystery box': {
                          'medical kit':{
                              'grabbable': True
                              }, 
                          'm4': {
                              'grabbable': True
                              }, 
                          'hand grenade':{
                              'grabbable': True
                              },
                          'opened': False,
                          'impact': '0',
                          'grabbable' : False
                          }
                      },
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : {'frankenstien'},
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item'  : {
                      'step ladder': {
                          'grabbable': True,
                          'grabbed': False
                          }, 
                      'door':{
                          'east attic door': {
                              'content': 'a Python living up there. You got bitten',
                              'impact' : '1',
                              'opened': False,
                              'grabbable': False,
                              'dependency': 'step ladder',
                              'hostile' : 'True'
                              },
                          'west attic door': {
                              'content':'explosives. Got triggered and exploded',
                              'impact':'3',
                              'opened': False,
                              'grabbable': False,
                              'dependency': 'step ladder',
                              'hostile': False
                              },
                          'book': {
                              'content': 'passcode',
                              'impact':'0',
                              'opened':False,
                              'grabbable':False,
                              'dependency': 'passcode',
                              'hostile': False
                              },
                          'opened': False,
                          'impact': '0',
                          'grabbable' :'False'
                          },
                      'mystery box': {
                          'C4':{
                              'grabbable': True
                              }, 
                          'flash bang':{
                              'grabbable': True
                              }, 
                          'smoke': {
                              'grabbable': True
                              }, 
                          'opened': False,
                          'impact': '0',
                          'grabbable' : False
                          }
                      },
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'item': ['tank', 'M24'],
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'east' : 'Cliff',
                  'item' : {
                      'cookie' :{
                          'grabbable': True
                          },
                      'door':{
                          'east metal door':{
                              'content': 'a tunnel. It\'s Dark',
                              'impact':'0',
                              'opened':False,
                              'grabbable':False,
                              'dependency': 'passcode',
                              'hostile': False
                              }
                          },
                      'mystery box':{
                              'shiny rock':{
                                  'grabbable': True
                                  },
                              'opened': False,
                              'impact': '0',
                              'grabbable' : False
                              },
                      
                      },
                  
            }
         }
timer_off = False
def hostileAttack():
    print('You just got shot....Focus !!')
    global timer_off
    timer_off = True
    
timer = threading.Timer(5.0, hostileAttack) 

#open objects and prints the content
def openIt(currentRoom, elem, inventory, number_of_lives):
    items = rooms[currentRoom]['item']
    N = -3

    if elem in items and elem == 'mystery box':
        visibleItems = list(rooms[currentRoom]['item']['mystery box'].keys())[0:N]
        if items['mystery box']['opened'] == False:
            #print("---------------------------")
            items['mystery box']['opened'] = True 
            print("You found " + str(visibleItems))
            print("")
            return 0
        else:
            #print("---------------------------")
            print("It's open already. smh ")
            print("You found " + str(visibleItems))
            return 0
    elif elem in items and elem == "door":
        visibleItems = list(items['door'].keys())[0:N]
        if items['door']['opened'] == False:
            items['door']['opened'] = True
            print("You found " + str(visibleItems))
            print("One of these doors have passcode to get out of this room")
            print("There might be some surprises too. Be very careful..")
            
            return 0
        else:
            print("Choose east door, west door or south door..")
            return 0
    elif items['door']['opened'] == True and elem in items['door'].keys():
        visibleItems = list(items['door'].keys())[0:N]
        
        if items['door'][elem]['opened'] == False:
            if items['door'][elem]['dependency'] in inventory:
                items['door'][elem]['opened'] = True
                print("You found " + str(items['door'][elem]['content']))
                if items['door'][elem]['content'] == 'passcode':
                    inventory += [items['door'][elem]['content']]
                    return 0
                if elem == 'east door':
                    winsound.PlaySound('T-Rex.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
                    time.sleep(2)
                    winsound.PlaySound('PsychoScream.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
                    time.sleep(5)
                    winsound.PlaySound(None, winsound.SND_ASYNC)
                if items['door'][elem]['hostile'] == True:
                    print('shoot, shoot !!')
                    timer.start()
                    action = input("Type shoot to shoot >> ")
                    if timer_off == True:
                        return items['door'][elem]['impact']
                    elif action == 'shoot' and timer_off==False:
                        if 'm4' in inventory:
                            timer.cancel()
                            print('Threats elimininated.. Great Work')
                            return 0
                        else:
                            return items['door'][elem]['impact']
                    else:
                        print("Unlucky day")
                        return items['door'][elem]['impact']
                else:
                    return items['door'][elem]['impact']
            else:
                print('Personal inventory missing tool')
                return items['door']['impact']
        else:
            print("It has been opened already.. !!")
            return items['door']['impact']
    else:
        print("doesn't seem to work !!")
        return items['door']['impact']


              
def go(currentRoom, elem):
     #check that they are allowed wherever they want to go
     if elem in rooms[currentRoom]:
         #set the current room to the new room
         return rooms[currentRoom][elem]       
         #there is no door (link) to the new room
     else:
            print('You can\'t go that way!')
def get(currentRoom, elem, inventory, number_of_lives, number_of_moves):
    items = rooms[currentRoom]['item']
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom]: 
        if elem in items and items[elem]['grabbable'] == True:
            items[elem]['grabbed'] = True
            #print("its inside weapon")
            #add the item to their inventory
            inventory += [elem]
            #display a helpful message
            print(elem + ' got!')
            #delete the item from the room
            #itempointer = rooms[currentRoom]['item']
            del items[elem]
            #del rooms[currentRoom]['item'][move[1]]
            #otherwise, if the item isn't there to get
        
        elif items['mystery box']['opened'] == True:
            if elem in items['mystery box'] and items['mystery box'][elem]['grabbable'] == True:
                #print('its inside weapon')
                #add the item to their inventory
                inventory += [elem]
                #display a helpful message
                print(elem + ' got!')
                #delete the item from the room
                del items['mystery box'][elem]
                if elem =='shiny rock':
                    openWormHole(number_of_lives, number_of_moves)
                    
        else:
            print('Can\'t get ' + elem + '!')
    else:
        #tell them they can't get it
        print('Are you out of your mind?')
        

def main():
    #start the player in the Hall
    currentRoom = 'Hall'
    #visibleItems = rooms[currentRoom]['item']

    showInstructions()
    
    #an inventory, which is initially empty
    inventory = []

    number_of_moves = 0
    number_of_lives = 3  
    #loop forever
    while True:
        showStatus(number_of_lives, number_of_moves, currentRoom, inventory)
        
        #10 moves is equal to 1 life lost
        if number_of_moves/10 == number_of_lives:
            print("Terrorists have discovered your movements. Hostages are killed and you are fired..!! ")
            break
        if number_of_lives <= 0:
            winsound.PlaySound(None, winsound.SND_ASYNC)
            print("Mission failed...")
            break
        number_of_moves +=1
        #get the player's next 'move'
        #.split() breaks it up into an list array
        #eg typing 'go east' would give the list:
        #['go','east']
        move = ''
        while move == '':
            move = input('Make the Next Move >> ')
        if move == 'q':
            winsound.PlaySound(None, winsound.SND_ASYNC)
            print('You are fired.. Loser!')
            break
        print("------------------------------------------")
        # split allows an items to have a space on them
        # get golden key is returned ["get", "golden key"]          
        move = move.lower().split(" ", 1)
        
        #items = rooms[currentRoom]['item']
        
        impact = 0
        #if they type 'open' first
        if move[0] == 'open':
            impact = int(openIt(currentRoom, move[1], inventory, number_of_lives))
            number_of_lives -= impact
            #print(rooms[currentRoom]['item']['mystery box'])    
        #if they type 'go' first
        if move[0] == 'go':
            if 'passcode' in inventory:
                currentRoom = go(currentRoom, move[1])
            else:
                print("passcode needed to leave !!")
    
        #if they type 'get' first
        if move[0] == 'get' :
            get(currentRoom, move[1], inventory, number_of_lives, number_of_moves)
        
        if move[0] == 'shoot':
            #detect_hostile = dict()
            #index = 0
            #size = len(rooms[currentRoom]['item']['door'])
            if 'm4' not in inventory:
                print('No weapon available..')
            elif impact > 0:
                print(impact)
                if timer_off==False:
                    timer.cancel()
                    print("Nicely Done !!")
                else:
                    number_of_lives -=1
            else:
                print("Have you lost your mind ?!!")
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
    winsound.PlaySound(None, winsound.SND_PURGE)