import csv
import sys
import re


a = []

def opencsv(filename):
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            a.extend(row)
            #print ', '.join(row)
    return a
