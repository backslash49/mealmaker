import csv
import sys
import re

#simple function that opns a single row csv file and returns the contents as a list
a = []

def opencsv(filename):
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            a.extend(row)
            #print ', '.join(row)
    return a
