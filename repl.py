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
4. Find prize motivation based on a certain keyword
5. Insert new prize data for a new year\n''')

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
            word = input('Enter a keyword: ')
            find_keyword(word)
        if choice == 5:
            print(prizes_collection.find_one())

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
    

def find_keyword(word):
    for result in prizes_collection.aggregate([{"$project":{"prizes":{"laureates":{"$filter":{"input":"laureates", "cond": {"$regex": word}}}}}}]):
        print(result)

def insert(New_Year , Category , First_Name , Surname , Motivation , Share): 
    ## retrieves the Prize Collection to insert information into specific categories ## 
    prizes = prizes_collection.find_one()
    Prize_Array = prizes["prizes"]

    ## New Entry for a Possible New Year to be Added ## 
    New_Entry = {"year":"0" , "category":"0" , "laureates":[{"id":"0" , "firstname":"0" , "surname":"0" , "motivation":"0" , "share":"0"}]} 
    Old_Entry_Addition = {} 

    ## creates a loop that will go through and find the most recent year ##
    for Prize in Prize_Array: 
        if Prize["year"] == New_Year and Prize["category"] == Category:        ## if the Year and Category correspond with the given information than add it to the Older Entry ##                                                                                 
            ## update the New Year ##                                          ## goes through the Laureates to update the proper information and add a completely new entry ##
            for Year in New_Entry["year"]:
                Year["year"] == New_Year
            ## update the New Category ## 
            for Category in New_Entry["category"]:
                Category["category"] == Category
            for New_Laureates in New_Entry["laureates"]:                              
                ## updates the First Name ## 
                if New_Entry["firstname"]: 
                    New_Entry["firstname"] = First_Name
                ## updates the SurName ## 
                elif New_Entry["surname"]:
                    New_Entry["surname"] = Surname
                ## updates the Motivation ## 
                elif New_Entry["motivation"]:
                    New_Entry["motivation"] = Motivation
                ## updates the Share ## 
                elif New_Entry["share"]:
                    New_Entry["share"] = Share
        elif New_Year not in Prize:                                            ## if the new proposed year is not in the dictionary than add items to the New_Entry ## 
            ## update the New Year ## 
            for Year in New_Entry["year"]:
                Year["year"] == New_Year
            ## update the New Category ## 
            for Category in New_Entry["category"]:
                Category["category"] == Category
            for New_Laureates in New_Entry["laureates"]:                              
                ## updates the First Name ## 
                if New_Entry["firstname"]: 
                    New_Entry["firstname"] = First_Name
                ## updates the SurName ## 
                elif New_Entry["surname"]:
                    New_Entry["surname"] = Surname
                ## updates the Motivation ## 
                elif New_Entry["motivation"]:
                    New_Entry["motivation"] = Motivation
                ## updates the Share ## 
                elif New_Entry["share"]:
                    New_Entry["share"] = Share
        prizes_collection.insert_one(New_Entry)


if __name__ == '__main__':
    REPL()