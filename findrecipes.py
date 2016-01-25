import re
import sys

f = open('/users/lauren/downloads/Kids.mmf')

#recipes = re.findall(r'Title:\s*(.*)\r', f.read())

things = '\d*\s*(.*)\r'

#ingredients = re.findall(r'MOLASSES'+'\r\n \r\n', f.read())

ingredients = re.findall('Servings:\s*\d*\r\n\s\r\n\s*'+'\s'+'[^\r\n\r\n]*', f.read())


#ingredients = re.findall('Servings:\s*'+ things, f.read())

#ingredients = re.findall(r'\s*\d*\s*(.*)\r\d*\s*(.*)\r', f.read())


#for titles in recipes:
    #print titles
#
for items in ingredients:
    print items
