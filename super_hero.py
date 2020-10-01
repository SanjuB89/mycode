# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 07:39:11 2020

@author: sanju
"""
#!/usr/bin/env python3
import argparse
from datetime import datetime

dict =  {
    "flash":{
        "speed": "fastest", 
        "intelligence": "lowest",
        "strength": "lowest"
        }, 
    "batman":{
        "speed": "slowest", 
        "intelligence": "highest", 
        "strength": "money"
        }, 
    "superman":{
        "speed": "fast", 
        "intelligence": "average", 
        "strength": "strongest"
        }
    }
def hero(name):
    char_name = name

def stats():
    
if __name__ == '__main__':
    choices = {'hero': hero, 'stats': stats}
    parser = argparse.ArgumentParser(description='Favorite her stats')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='HERO', type=str, default='superman',
                        help='Super hero (default superman)')
args = parser.parse_args()
function = choices[args.role]
print(function(args.p))
char_name = ""
char_stat = ""
while char_name == "" or char_name not in dict:
    char_name = input('Which character do you want to know about? (Flash, Batman, Superman): ')
    char_name = char_name.lower()
while char_stat == "" or char_stat not in dict[char_name]:
    char_stat =  input('What statistic do you want to know about? (strength, speed, or intelligence: ' )
    char_stat = char_name.lower()
print(f'{char_name.capitalize()}\'s {char_stat} is {dict[char_name][char_stat]}')