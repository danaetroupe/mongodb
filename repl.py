import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://antoniobendanae:antoniobendanae@project.lcdadjk.mongodb.net/test")
db = cluster["Main"]
prizes_collection = db["Prizes"]

def REPL():
    print('\nWelcome to the MongoDB Python interaction!')

    while True:
        print('''\n1. Find all award categories
2. Find all prize winners in a certain year for a certain prize
3. Find all winners of a certain prize
4. Find prize data based on a certain keyword
5. Insert new prize data for a new year\n''')

        choice = int(input('Enter the number of the action to perform: '))
        if choice == 1:
            pass
        if choice == 2:
            year = input('\nEnter a year: ')
            category = input('Enter a prize: ')
            second_option(year, category)
        if choice == 3:
            category = input('\nEnter a prize: ')
            third_option(category)
        if choice == 4:
            pass
        if choice == 5:
            pass

def second_option(year, category):
    prizes = prizes_collection.find_one()
    prize_array = prizes['prizes']
    for prize in prize_array:
        if prize['year'] == year and prize['category'] == category:
            print(f'\nThe winners of {category} in {year} are:\n')
            for laureat in prize['laureates']:
                print(laureat['firstname'], laureat['surname'])

def third_option(category):
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
    

if __name__ == '__main__':
    REPL()