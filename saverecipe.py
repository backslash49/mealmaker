import pickle
import os
import pprint

def memory(newtitle, newrecipe):
    output=open('recipememory.txt', 'rb')
    obj_dict = pickle.load(output)
    print "Recipes Currently Loaded"
    pprint.pprint(obj_dict)
    output.close()
    os.remove('recipememory.txt')
    obj_dict[newtitle] = newrecipe
    print 'New Recipe Being Added'
    pprint.pprint(obj_dict)
    #save and close
    output = open('recipememory.txt', 'ab+')
    pickle.dump(obj_dict, output)
    output.close()

def openrecipefile():
    output=open('recipememory.txt', 'rb')
    obj_dict = pickle.load(output)
    return obj_dict
    output.close()
