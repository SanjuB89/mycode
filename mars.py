# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 07:41:52 2020

@author: sanju
"""

#!/usr/bin/python3

import requests


def main():
    apodresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY").json()
    
    #actions = ['1: all link', '2: all link with Rover', '3: link by cam']
    #userInputer('CHoose 1, 2 or 3: ')
    #for i in range(len(actions)):
        #print 
        
    #printLinksRover(apodresp)
    userInputCams(apodresp)
    #printLinks(apodresp)
    #print(apodresp)

def printLinks(apodresp):
    for i in apodresp['photos']:
        print(i['img_src'])

def printLinksRover(apodresp):
    for i in apodresp['photos']:
        print(i['rover']['name'])
        print(i['earth_date'])
        print(i['img_src'])
        print("")
        
def userInputCams(apodresp):
    all_cams= ["FHAZ","RHAZ","MAST","CHEMCAM","NAVCAM"]
    userInput = input("Enter cam: ")
    
    if userInput.upper() in all_cams:
        for i in apodresp['photos']:
            if i['camera']['name'] == userInput.upper():
                print(i['rover']['name'])
                print(i['earth_date'])
                print(i['img_src'])
                print("")
    else:
        print("No cams available in that name")
    
if __name__ == "__main__":
    main()