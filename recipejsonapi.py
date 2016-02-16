
import json, requests, pprint, urllib, urllib2, re, sys

#command line input
search = input('What are you searching for today?')

#api url for SEARCHING
urlsearch = "http://food2fork.com/api/search"
urlget = "http://food2fork.com/api/get"

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
while (count < lenresults):
    print count, (dict['recipes'][count]['title'])
    print dict['recipes'][count]['f2f_url']
    count = count + 1

#print number of results
print len(dict['recipes'])

def getingredients(selection):
    selection = selection
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
    ing = ing.replace('1/2', '')
    ing = ing.replace('1', '')
    ing = ing.replace('2', '')
    ing = ing.replace('3', '')
    ing = ing.replace('4', '')
    ing = ing.replace('5', '')
    ing = ing.replace('6', '')
    ing = ing.replace('7', '')
    ing = ing.replace('8', '')
    ing = ing.replace('small', '')
    ing = ing.replace('slices', '')
    ing = ing.replace('cp', '')
    ing = ing.replace('diced', '')
    ing = ing.replace('cups', '')
    ing = ing.replace('cup', '')
    ing = ing.replace('tablespoons', '')
    ing = ing.replace('tablespoon', '')
    ing = ing.replace('\\n', '')
    ing = ing.replace('/', '')
    ing = ing.replace('pound', '')
    ing = ing.replace('to taste', '')
    ing = ing.replace('ounces', '')
    ing = ing.replace('quart', '')
    ing = ing.replace('bag', '')
    ing = ing.replace('Halved', '')
    ing = ing.replace('Tablespoon', '')
    ing = ing.replace('Tablespoons', '')
    ing = ing.replace('  ', '')
    split = ing.split('", "')
    return split

#46980
def returnrecipeandingredients(x):
    a = getingredients(x)
    title = a[0]
    onlyingredients = removestuff(a[1])
    #strip starting and ending spaces
    ingredientlist = []
    for items in onlyingredients:
        a = items.strip()
        ingredientlist.append(a)
    return title, ingredientlist
    #create dict item for recipe and ingredients

def get(x):
    returnrecipeandingredients(x)
    recipes = {}
    recipes[title] = ingredientlist
    return recipes


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
