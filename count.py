import random


def countWords():

    file = input('Enter File Name: ')
    var = 0
    openFile=open(file,'r')

    for line in openFile:

        words=line.split()
        var=var + len(words)

    print('Number of words')        
    print(var)

countWords()
