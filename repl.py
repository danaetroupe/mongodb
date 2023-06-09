import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://antoniobendanae:antoniobendanae@project.lcdadjk.mongodb.net/test")
db = cluster["Main"]
prizes_collection = db["Prizes"]

def REPL():
    print('\nWelcome to the MongoDB Python interaction!')

    while True:
        print('''\n1. Find all award categories in a given year
2. Find all prize winners in a certain year for a certain prize
3. Find all winners of a certain prize
4. Insert new prize data for a new year\n''')

        choice = int(input('Enter the number of the action to perform: '))
        if choice == 1:
            year = input('Enter a year: ')
            select_categories(year)
        if choice == 2:
            year = input('\nEnter a year: ')
            category = input('Enter a prize: ')
            year_prize_winners(year, category)
        if choice == 3:
            category = input('\nEnter a prize: ')
            prize_winners(category)
        if choice == 4:
            New_Year = input("Enter the New Year: ")
            Category = input("Enter the Category: ")
            First_Name = input("Enter the Surname: ")
            Surname = input("Enter the Motivation: ")
            Motivation = input("Enter the Motivation: ")
            Share = input("Enter the Share: ")
            insert(New_Year , Category , First_Name , Surname , Motivation , Share)

def year_prize_winners(year, category):
    prizes = prizes_collection.find_one()
    prize_array = prizes['prizes']
    for prize in prize_array:
        if prize['year'] == year and prize['category'] == category:
            print(f'\nThe winners of {category} in {year} are:\n')
            for laureat in prize['laureates']:
                print(laureat['firstname'], laureat['surname'])

def prize_winners(category):
    prizes = prizes_collection.find_one()
    prize_array = prizes['prizes']
    laureats = []
    for prize in prize_array:
        if prize['category'] == category:
            try:
                for laureat in prize['laureates']:
                    laureats.append([laureat['firstname'], laureat['surname']])
            except:
                pass
    if laureats:
        print(f'\nThe winners of {category} are:\n')
        for laureat in laureats:
            print(laureat[0], laureat[1])

def select_categories(year):
    collect = prizes_collection.find_one()
    prizes = collect['prizes']
    for prize in prizes:
        if prize['year'] == str(year):
            print(prize['category'])

def insert(year, category, first_name, surname, motivation, share): 
    ## retrieves the Prize Collection to insert information into specific categories ## 
    prizes = prizes_collection.find_one()
    array = prizes["prizes"]

    ## New Entry for a Possible New Year to be Added ## 
    document = {"year": year, "category": category, "laureates": [{"firstname":first_name , "surname":surname , "motivation":motivation , "share":share}]}
    prizes_collection.insert_one(document)
    
if __name__ == '__main__':
    REPL()
    
    
"C:/danae/Desktop/Programming/prizes.json"