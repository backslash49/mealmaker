import pickle
import os
import pprint

def memory(newtitle, newrecipe):
    output=open('recipelist.txt', 'rb')
    obj_dict = pickle.load(output)
    print "Recipes Currently Loaded"
    pprint.pprint(obj_dict)
    output.close()
    os.remove('recipelist.txt')
    addtitle = newtitle
    addings = newrecipe
    obj_dict[addtitle] = addings
    print 'New Recipe Being Added'
    pprint.pprint(obj_dict)
    #save and close
    output = open('recipelist.txt', 'ab+')
    pickle.dump(obj_dict, output)
    output.close()

def openrecipefile():
    output=open('recipelist.txt', 'rb')
    obj_dict = pickle.load(output)
    print "Recipes Currently Loaded"
    pprint.pprint(obj_dict)
    output.close()
