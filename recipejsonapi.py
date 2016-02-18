import json, requests, pprint, urllib, urllib2, re, sys
import save

#command line input

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
        search_results[count] = (title, webID)
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
    ing = ing.replace('Tbsp', '')
    ing = ing.replace('Tsp', '')
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

    ing = ing.replace('quart', '')
    ing = ing.replace('bag', '')
    ing = ing.replace('Halved', '')
    ing = ing.replace('Tablespoon', '')
    ing = ing.replace('Tablespoons', '')
    ing = ing.replace('[', '')
    ing = ing.replace(']', '')
    ing = ing.replace('"', '')
    ing = ing.replace(', softened', '')
    ing = ing.replace('  ', '')
    ing = ing.replace('()', '')

    split = ing.split('", "')

    return split

#46980
def get_title_strip_ingredients(x):
    a = getingredients(x) #get raw ingredients
    title = a[0]  #save title
    onlyingredients = removestuff(a[1]) #remove crap from ingredients
    string = str(onlyingredients)
    string = string.split(',')
    ingredientlist = []  #create blank list to add ingredients after cleaning
    for items in string: #run for loop to...
        a = items.strip()      #strip starting and ending spaces
        ingredientlist.append(a)  #append cleaned items to ingriedentlist
    titleandingredients = {}
    titleandingredients[title] = ingredientlist
    return titleandingredients
    #create dict item for recipe and ingredients

def main():
    listofrecipes = searchrecipes()
    pprint.pprint(listofrecipes)
    choice = input('Which Recipe')
    selection = listofrecipes[choice][1]
    a = get_title_strip_ingredients(selection)
    return a
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
