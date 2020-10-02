# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 07:40:54 2020

@author: sanju
"""

#https://pokeapi.co/api/v2/pokemon/

#!/usr/bin/python3
import requests
import wget

json2python = "https://pokeapi.co/api/v2/pokemon/"

def api_slice(json2python):
    
        #('Enter q to quit')
    name = input("Enter Pokemon name:>> ")
    name = name.lower()
    
    res = requests.get(json2python + name).json()
    poke_pic= res['sprites']['front_default']
    print(poke_pic)
    return poke_pic
#api_slice(json2python)

def wget_pic(pic):
    
    wget.download(pic, 'C:/Users/sanju/Documents/TLG_python/mycode/static/')
    

def main():
    #json_conv(api_pull()
    wget_pic(api_slice(json2python))

main()