import pymongo as mongo

connect = mongo.MongoClient("mongodb+srv://antoniobendanae:antoniobendanae@project.lcdadjk.mongodb.net/test")
main = connect["Main"]
prizesdb = main["Prizes"]

year = prizesdb.find_one()
print(year)

# Powerpoint - Antonio
# Main REPL Loop - Antonio

# Queries: 
# Select all caterogies for awards - Danae 
# Select the names of all lauterates given a certain year and category - Antonio
# Give (a certain number) of queries involving a certain keyword - Danae
# See if anbody won a prize multiple data - Antonio
# Add new prizes for new year - Ben

#git push 
#git add .
#git commit -m "message here"
#git push