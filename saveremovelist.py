import pickle
import os
import pprint

def add_to_remove_list_memory(newphrase):
    output=open('removelistmemory.txt', 'rb')
    removelist = pickle.load(output)
    print "Words/Phrases Currently Loaded into Removelist: "
    pprint.pprint(removelist)
    output.close()
    os.remove('removelistmemory.txt')
    print 'New Word/Phrases Being Added'
    pprint.pprint(newphrase)
    addornot = input('Are you sure you want to add this? ')
    if addornot == 'yes':
        removelist.extend(newphrase)
    #save and close
    output = open('removelistmemory.txt', 'ab+')
    pickle.dump(removelist, output)
    output.close()

def open_remove_list_memory():
    output=open('removelistmemory.txt', 'rb')
    obj_dict = pickle.load(output)
    return obj_dict
    output.close()
