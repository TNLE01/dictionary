#Project 2
#Dictionaries in Action
import random

username = input('What is your username? ')

gun = {
    'speed': 60,
    'power': 90,
    }
kinfe = {
    'speed': 90,
    'power': 70,
    }
ninja_stars = {
    'speed': 80
    'power': 50,
    }
print(gun, knife, ninja_stars)
weapon = input('What is your choice of weapon? ')

game_stats = {
    'user': username,
    'health': 100,
    'xp': 0,
    'money': 0,
    'weapons': weapon,
    }
