haveall = []
havemost = []
for keys in meals:
    count = 0
    matches = []
    for items in recipes[keys]:
        for ings in pantry:
            a = fuzz.ratio(items, ings)
            if a > 85:
                count = count+1
                matches.append(items)
    #print count, 'of ', len(recipes[keys]), 'ingredients for ', keys
    #print 'ingredients', recipes[keys]
    if count >= len(recipes[keys]):
        haveall.append(keys)
        #print 'You have what you need to make ', keys
        #print 'Ingredients are', recipes[keys]
        #print 'Matched ingredients are ', matches
    if count >= .75*len(recipes[keys]):
        if keys in haveall:
            do = 'nothing'
        else:
            havemost.append(keys)
            #print 'You have most of what you need to make ', keys
            #print 'Ingredients are', recipes[keys]
            #print 'Matched ingredients are ', matches
print haveall
print havemost
