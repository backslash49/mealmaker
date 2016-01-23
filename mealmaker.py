import re
import sys


recipes = {}

recipes['soup'] = ('salt', 'water', 'stock')

print recipes
print type(recipes)

pantry = ('salt', 'beer', 'bread', 'water', 'stock', 'pepper')

print pantry
print type(pantry)

count = 0
for ingredients in recipes['soup']:
    a = ingredients in pantry
    print a
    if ingredients in pantry:
        count = count+1
print count
recipelen = len(recipes['soup'])
if count == recipelen:
    print 'You have what you need for soup'
