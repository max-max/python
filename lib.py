#!/usr/bin/python3
'''Version 0.1'''

import sys

def record():
    bookname = input('What is your name: ')
    print('This is what you have just typed in: {0}'.format(bookname))

    f = open('text.txt', 'a')
    f.write(bookname)
    f.write('\n')

def read():
    f = open('text.txt', 'r')
    while True:
        line = f.readline()
        print(line)
        if len(line) == 0:
            break

def search():
    f = open('text.txt','r')
    needle = input('Enter the name you\'re looking for: ')
    while True:
        line = f.readline()
#        if needle in line:
        if line.find(needle) != -1:
            print('Yes it\'s here!')
            print('Here it is: {0}'.format(line))
            break
        else:
            print('Nope no can do!')
            break

def quit():
    sys.exit()

print('What would you like to do?\n')
choice = int(input('[1] Record a text\n[2] Read the file back\n[3] search\n[4] quit\n'))

if choice == 1:
    record()
elif choice == 2:
    read()
elif choice == 3:
    search()
elif choice == 4:
    quit()
