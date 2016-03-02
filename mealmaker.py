import re
import sys
import openascsv
import saverecipe
import saveremovelist
import recipejsonapi
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#open recipes from memory as python DICT and save DICT to new variable recipes
recipes = saverecipe.openrecipefile()

# display recipes from memory, printing only the title of recipe
print 'Recipes Loaded into System'
meals = recipes.keys()
for i in meals:
    print '  ' + i

#import ingredients from memory csv file, and add each ingredient to
#new list variable named pantry
pantry = []
for items in openascsv.opencsv('/users/lauren/downloads/google-python-exercises/mealmaker/ingredients.csv'):
    pantry.extend([items])

# display ingredients from memory
print 'Ingredients Loaded into System'
for i in pantry:
    print '  ' + i

haveall = []        #create blank list to be populated by title of recipes w/ all ingredients in pantrh
havemost = []       #create blank list to be populted by title of recipes w/ most ingredients in pantry
for keys in meals:  #run for loop on the title of recipes
    count = 0       #create zero count, which will increase by 1 for each matched ingredient
    matches = []    #create blank list to be populated by each ingredient that matches in pantry
    for items in recipes[keys]:     #run forloop on items in each recipe
        for ings in pantry:         #run for loop on items in pantry
            a = fuzz.ratio(items, ings) #assign match ratio for each itemsinpantry-each item in recipe
            if a > 85:      #create threshold for match rate and only proceed w/ below if > that threshold
                count = count+1     #add one to count if ingredient matches in pantry
                matches.append(items)   #append matching item to match list for later exclusion
    if count >= len(recipes[keys]):
        haveall.append(keys)
        #print 'You have what you need to make ', keys
        #print 'Ingredients are', recipes[keys]
        #print 'Matched ingredients are ', matches
    if count >= .75*len(recipes[keys]):
        if keys not in haveall:
            havemost.append(keys)
            #print 'You have most of what you need to make ', keys
            #print 'Ingredients are', recipes[keys]
            #print 'Matched ingredients are ', matches
print 'You have what you need for'
for items in haveall:
    print '  ', items
print 'You have most of what you need for'
for items in havemost:
    print '  ', items

yesorno = input("Do you want to search for new recipes? [1] YES  [2] NO")
if yesorno == 1:
    recipejsonapi.main()
if yesorno == 2:
    print 'Ok, exiting now.'
