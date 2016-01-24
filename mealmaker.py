import re
import sys
import openascsv



recipes = {}
recipes['soup'] = ('salt', 'water', 'stock')
recipes['grilled cheese'] = ('bread', 'butter', 'cheese')
recipes['pb&j'] = ('peanut-butter', 'jelly')

# cisplay recipes
print 'Recipes Loaded into System'
meals = recipes.keys()
for i in meals:
    print '  ' + i

# create a tupil of ingredients import from a csv file
pantry = []
for items in openascsv.opencsv('/users/lauren/downloads/ings.csv'):
    pantry.extend([items])    

# display ingredients
print 'Ingredients Loaded into System'
for i in pantry:
    print '  ' + i
    
# nexted for loop to determine which recipes the ingredients in the pantry are
# sufficient to create
for keys in meals:  # keys are the names of the meals
    count = 0                       # initiate zero count
    for ingredients in recipes[keys]:   # for loop on ingreadients in the recipes       
        if ingredients in pantry:   # check if ingreadients are in pantry
            count = count+1         # if in pantry, add one to count
    recipelen = len(recipes[keys])  # compare length of count to length of recipe 
    if count == recipelen:          # if equal, you have all the ingredients
        print 'You have what you need for ' + keys  # returns meals you have ingredients for
