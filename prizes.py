import pymongo as mongo

connect = mongo.MongoClient("mongodb+srv://antoniobendanae:antoniobendanae@project.lcdadjk.mongodb.net/test")
main = connect["Main"]
prizesdb = main["Prizes"]

year = prizesdb.find_one()
print(year)
