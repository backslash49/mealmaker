import json, requests, pprint, urllib, urllib2, re, sys
import save

def searchrecipes():
    search = input('What are you searching for today?')
    #api url for SEARCHING
    urlsearch = "http://food2fork.com/api/search"
    #create payload of parammaters for API get request
    params = {'key': '635133a811791ce4b3b05c7d0a6121a8', 'q': search}
    #call API
    data = requests.get(url=urlsearch, params=params)
    #create dictionary of results in JSON format
    dict = json.loads(data.content)
    #create variable for length of results
    lenresults = len(dict['recipes'])
    #create count variable
    count = 1
    #run while loop on results to return titles
    search_results = {}
    while (count < lenresults):
        title = json.dumps(dict['recipes'][count]['title'])
        title = title.replace('"', '')
        website = json.dumps(dict['recipes'][count]['f2f_url'])
        webID = re.findall('view/([^"]*)', website)
        search_results[title] = (webID)
        count = count + 1
    return search_results

def getingredients(selection):
    urlget = "http://food2fork.com/api/get"
    paramsget = {'key': '635133a811791ce4b3b05c7d0a6121a8', 'rId': selection}
    datarecipe = requests.get(url=urlget, params=paramsget)
    dictrecipe = json.loads(datarecipe.content)
    ingredients = dictrecipe['recipe']['ingredients']
    title = json.dumps(dictrecipe['recipe']['title'])
    title = title.replace('"', '')
    return title, ingredients

def removestuff(ingredients):
    ing = json.dumps(ingredients)
    ing = ing.replace('teaspoons', '')
    ing = ing.replace('teaspoon', '')
    ing = ing.replace('5g', '')
    ing = ing.replace('0g', '')
    ing = ing.replace('1/2', '')
    ing = ing.replace('0', '')
    ing = ing.replace('00', '')
    ing = ing.replace('1', '')
    ing = ing.replace('2', '')
    ing = ing.replace('3', '')
    ing = ing.replace('4', '')
    ing = ing.replace('5', '')
    ing = ing.replace('6', '')
    ing = ing.replace('7', '')
    ing = ing.replace('8', '')
    ing = ing.replace('9', '')
    ing = ing.replace('small', '')
    ing = ing.replace('slices', '')
    ing = ing.replace('cp', '')
    ing = ing.replace('diced', '')
    ing = ing.replace('cups', '')
    ing = ing.replace('cup', '')
    ing = ing.replace('tablespoons', '')
    ing = ing.replace('tablespoon', '')
    ing = ing.replace('Tbsps', '')
    ing = ing.replace('Tsps', '')
    ing = ing.replace('tbsps', '')
    ing = ing.replace('tsp', '')
    ing = ing.replace('tbsp', '')
    ing = ing.replace('tsp', '')
    ing = ing.replace('0g', '')
    ing = ing.replace('00g', '')
    ing = ing.replace('&nbsp', '')
    ing = ing.replace('\\n', '')
    ing = ing.replace('/', '')
    ing = ing.replace('pound', '')
    ing = ing.replace('to taste', '')
    ing = ing.replace('ounces', '')
    ing = ing.replace(' ounce', '')
    ing = ing.replace(' oz', '')
    ing = ing.replace(' ml', '')
    ing = ing.replace('can', '')
    ing = ing.replace('melted', '')
    ing = ing.replace('thawed', '')
    ing = ing.replace('quart', '')
    ing = ing.replace('bag', '')
    ing = ing.replace('Halved', '')
    ing = ing.replace('Tablespoon', '')
    ing = ing.replace('Tablespoons', '')
    ing = ing.replace('for garnish (optional)', '')
    ing = ing.replace('[', '')
    ing = ing.replace(']', '')
    ing = ing.replace('"', '')
    ing = ing.replace(', softened', '')
    ing = ing.replace('shreaded', '')
    ing = ing.replace('sliced', '')
    ing = ing.replace('drained', '')
    ing = ing.replace('whole wheat', '')
    ing = ing.replace('thinly', '')
    ing = ing.replace('chopped', '')
    ing = ing.replace('blanched', '')
    ing = ing.replace('cooked', '')
    ing = ing.replace('tolb', '')
    ing = ing.replace('cut into thin strips', '')
    ing = ing.replace('&amp', '')
    ing = ing.replace('pinch', '')
    ing = ing.replace('plain', '')
    ing = ing.replace('ml', '')
    ing = ing.replace('-', '')
    ing = ing.replace('minced', '')
    ing = ing.replace('plus extra for frying', '')
    ing = ing.replace('package', '')
    ing = ing.replace('each', '')
    ing = ing.replace('cut into', '')
    ing = ing.replace('large', '')
    ing = ing.replace('about', '')
    ing = ing.replace('stick', '')
    ing = ing.replace('divided', '')
    ing = ing.replace('whole', '')
    ing = ing.replace('at room temperature', '')
    ing = ing.replace('grams', '')
    ing = ing.replace('diced', '')
    ing = ing.replace('skinless', '')
    ing = ing.replace('  ', '')
    ing = ing.replace('()', '')
    ing = ing.replace('room temperature', '')
    ing = ing.replace('packed', '')
    split = ing.split('", "')
    return split


def get_title_strip_ingredients(x):
    a = getingredients(x) #get raw ingredients
    title = a[0]  #save title
    onlyingredients = removestuff(a[1]) #remove crap from ingredients
    string = str(onlyingredients)
    string = string.replace(']', '')
    string = string.replace('[', '')
    string = string.replace("'", '')
    string = string.split(',')
    ingredientlist = []  #create blank list to add ingredients after cleaning
    for items in string: #run for loop to...
        if items != ' ':
            if items != '':
                a = items.strip()      #strip starting and ending spaces
                ingredientlist.append(a)  #append cleaned items to ingriedentlist
    lowercaseingredients = []
    for items in ingredientlist:
        lowercaseingredients.append(items.lower())
    titleandingredients = {}    #creates blank dict for title and ing.
    titleandingredients[title] = lowercaseingredients #adds title and ingred. to dict
    return titleandingredients      #returns title and list of ingredients


def correct(x, file):
    if x == 'Delete':
        proceed = 'yes'
        while proceed == 'yes':
            deletingitem = input('Which Item do you want to Delete? ')
            deletingitem = deletingitem - 1
            print 'Ok, deleting the following item: '
            print file[deletingitem]
            checkb4delete = input('Are you sure you want to delete that? ')
            if checkb4delete == 'yes':
                file.pop(deletingitem)
                proceed = input('Want to delete more items? ')
        #correctingitem = input('Which Ingredient? ')
        count = 1
        for items in file:
            print count, items
            count = count + 1
    if x == 'Edit':
        proceed = 'yes'
        while proceed == 'yes':
            editingitem = input('Which Item do you want to Edit? ')
            editingitem = editingitem - 1
            print 'Ok, editing the following item: '
            print file[editingitem]
            editeditem = input('What are you changing the item to? ')
            print 'Ok, editing from "', file[editingitem], '" to "', editeditem, '"'
            checkb4edit = input('Are you sure you want to change this? ')
            if checkb4edit == 'yes':
                file[editingitem] = editeditem
            proceed = input('Do you want to edit more items? ')
            #correctingitem = input('Which Ingredient? ')
        count = 1
        for items in file:
            print count, items
            count = count + 1


def main():
    listofrecipes = searchrecipes()
    returnedlist = {}
    count = 1
    for items in listofrecipes.keys():
        print count, items
        returnedlist[count] = (items, listofrecipes[items])
        count = count+1
    choice = input('Which Recipe')
    selection = returnedlist[choice][1]
    newrecipe = get_title_strip_ingredients(selection)
    print 'Title:  ', newrecipe.keys()[0]
    print 'Ingredients:  ',
    count = 1
    for items in newrecipe[newrecipe.keys()[0]]:
        print count, items
        count = count + 1
    yesorno1 = input('Want to make any corrections? [1] YES [2] NO ')
    if yesorno1 == 1:
        editordelete = input('[1] EDIT [2] DELETE? [3] BOTH ')
        if editordelete == 1:
            correct('Edit', newrecipe[newrecipe.keys()[0]])
        if editordelete == 2:
            correct('Delete', newrecipe[newrecipe.keys()[0]])
        if editordelete == 3:
            correct('Edit', newrecipe[newrecipe.keys()[0]])
            correct('Delete', newrecipe[newrecipe.keys()[0]])
    yesorno2 = input('Want to add this to your recipe book?')
    if yesorno2 == 'yes':
        save.memory(newrecipe.keys()[0], newrecipe[newrecipe.keys()[0]])





        ##


    #asktosave = input('Save to Memory? )
    #if asktosave == 'yes'
    #    save.memory()


#a = re.findall('http[^\']*', address)
#requests.get(a)

#pprint.pprint(a)

#pprint.pprint(dict['result']['results'][1]['resources'][2])

#pprint.pprint(dict['result']['results'][sel]['notes'])


#for items in dict['result']:
#    pprint.pprint(items)


#print dict

# print dict.keys()

#print dict['help']

#for items in dict['help']:
#    print items

#print data.help

#binary = data.content
#output = json.loads(binary)

# test to see if the request was valid
#print output['status']

# output all of the results
#pprint.pprint(output)
