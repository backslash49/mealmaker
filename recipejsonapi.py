import json, requests, pprint, urllib, urllib2, re, sys
import saverecipe
import saveremovelist
import pickle

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

#curently taking remove list from command line.
#removelist = ['teaspoons', 'teaspoon', '5g', '0g', '1', '0', '00', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'small', 'slices', 'cp', 'diced', 'cups', 'cup', 'tablespoons', 'tablespoon', 'Tbsps', 'Tsps', 'tbsps', 'tsp', 'tbsp', 'tsp', '0g', '00g', 'pound', 'to', 'ounces', 'can', 'melted', 'thawed', 'quart', 'bag', 'Halved', 'Tablespoon', 'Tablespoons', 'for', 'shreaded', 'sliced', 'drained', 'whole', 'thinly', 'chopped', 'blanched', 'cooked', 'tolb', 'cut', 'pinch', 'plain', 'ml', 'minced', 'plus', 'package', 'each', 'cut', 'large', 'about', 'stick', 'divided', 'whole', 'at', 'grams', 'diced', 'skinless', 'room', 'packed']
def removestuff(removelist, ings):
    ingredients = json.dumps(ings)
    ingredientlist = []
    remove = '|'.join(removelist)
    regex = re.compile(r'\b('+remove+r')\b', flags=re.IGNORECASE)
    out = []
    for items in ings:
        out.append(str(regex.sub('', items)))
    stripped = []
    for items in out:
        stripped.append(items.strip())
    return stripped

def get_title_strip_ingredients(x):
    a = getingredients(x) #get raw ingredients
    title = a[0]  #save title
    removelist = saveremovelist.open_remove_list_memory()
    onlyingredients = removestuff(removelist, a[1]) #remove crap from ingredients
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


def diff(edited, original):
    d = []
    c = re.findall('(.*)' + edited + '(.*)', original)
    for items in c[0]:
        if items != '':
            a = items.strip()
            d.append(a)
    return d

def correct(x, file):
    if x == 'Delete':
        proceed = 'yes'
        while proceed == 'yes':
            count = 1
            deletingitem = input('Which Item do you want to Delete? ')
            deletingitem = deletingitem - 1
            print 'Ok, deleting the following item: '
            print file[deletingitem]
            checkb4delete = input('Are you sure you want to delete that? ')
            if checkb4delete == 'yes':
                file.pop(deletingitem)
                for items in file:
                    print count, items
                    count = count + 1
                proceed = input('Want to delete more items? ')
        #correctingitem = input('Which Ingredient? ')
        count = 1
        for items in file:
            print count, items
            count = count + 1
    if x == 'Edit':
        proceed = 'yes'
        removelist = saveremovelist.open_remove_list_memory()
        addtoremovelist = []
        count = 1
        for items in file:
            print count, items
            count = count + 1
        while proceed == 'yes':
            editingitem = input('Which Item do you want to Edit? ')
            editingitem = editingitem - 1
            print 'Ok, editing the following item: '
            print file[editingitem]
            editeditem = input('What are you changing the item to? ')
            print 'Ok, editing from "', file[editingitem], '" to "', editeditem, '"'
            checkifaddtomemory = input('Do you want to add this edit to your removelist? :')
            if checkifaddtomemory == 'yes':
                payload = diff(editeditem, file[editingitem])
                addtoremovelist.append(payload)
                for items in addtoremovelist:
                    if items not in removelist:
                        saveremovelist.add_to_remove_list_memory(items)
                        addtoremovelist = []
            checkb4edit = input('Are you sure you want to change this? ')
            if checkb4edit == 'yes':
                file[editingitem] = editeditem
            count = 1
            for items in file:
                print count, items
                count = count + 1
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
    yesorno1 = input('Want to make any corrections? [1] YES  [2] NO ')
    if yesorno1 == 1:
        editordelete = input('[1] EDIT  [2] DELETE?  [3] BOTH ')
        if editordelete == 1:
            correct('Edit', newrecipe[newrecipe.keys()[0]])
        if editordelete == 2:
            correct('Delete', newrecipe[newrecipe.keys()[0]])
        if editordelete == 3:
            correct('Edit', newrecipe[newrecipe.keys()[0]])
            correct('Delete', newrecipe[newrecipe.keys()[0]])
    yesorno2 = input('Want to add this to your recipe book? [1] YES  [2] NO ')
    if yesorno2 == 1:
        saverecipe.memory(newrecipe.keys()[0], newrecipe[newrecipe.keys()[0]])
    if yesorno2 == 2:
        print 'Ok, exiting now.'




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
