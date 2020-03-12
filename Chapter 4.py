# Class

class Dog:
    kind = 'caine'
    def __init__(self, name):
        self.name = name
        self.kind = 5

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(Dog.kind)
print(e.kind)
print(Dog.kind)
print(d.name)
print(e.name)


# Class Melodii

class Melodii(object):
    def __init__(self, nume_melodii):
        self.nume_melodii = nume_melodii

    def amesteca(self):
        import random
        random.shuffle(self.nume_melodii)
        return self.nume_melodii
d = Melodii(['melodie1', 'melodie2', 'melodie3', 'melodie4'])
print(d.amesteca())

# Argv

# import sys
#
# print("Argv params:\n ",sys.argv)
#
# if not sys.stdin.isatty():
#     print("Command Line args: \n", sys.stdin.readlines())

# Time

import time

print('Timpul curent este: ' + str(time.time()))
print('Timpul curent este: ' + str(time.ctime()))
later = time.time() + 30
print('Timpul curent plus 30 de secunde: ' + str(time.ctime(later)))

# Pickle

try:
   import cPickle as pickle
except:
   import pickle

import pprint

data1 = [{'a':1.2, 'b':2.3, 'c':3.7}]
print('Inainte de serializare: ')
pprint.pprint(data1)

data1_string = pickle.dumps(data1)
print('\n')
print('\n')
print('Cum arata stringul dupa serializare')
pprint.pprint(data1_string)
print('\n')
print('\n')
data2 = pickle.loads(data1_string)
print('Cum arata dupa incarcam iar serializarea in ce era inainte folosint load: ')
pprint.pprint(data2)
print('Sunt obiectele identice?:', (data1 is data2))
print('Sunt obiectele egale?:', (data1 == data2))

#Unpickle

# try:
#    import cPickle as pickle
# except:
#    import pickle
#
# import pprint
# import sys
# from obiect_pickle import BaseClass
#
# try:
#    filename = sys.argv[1]
# except:
#    raise RuntimeError('Scriptul trebuie sa fie lansat cu un argument %s' % sys.arv[0])
#
# in_string = open(filename, 'rb')
# try:
#    while True:
#        try:
#            o = pickle.load(in_string)
#        except EOFError:
#            break
#        else:
#            print("CITESTE %s (%s)" % (o.name, o.name_reverse))
# finally:
#    in_string.close()


#Find IP adress

# import re
# ipPattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
# findIP = re.findall(ipPattern,s)
#
# Class CautaIP:
#     def __init__ (self,text):
#         self.text = text
#     def findip (self, ipPattern):
#         return re.findall( ipPattern, self.text)
#
# ipPattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
#
# Obj1=CautaIP('Adresa 192.168.0.1 ; Adresa 192.165.21.3 ; Adresa 123.25.12.12')
# print(Obj1.findip(ipPattern))

#  Jjson

import requests
import json

r = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.content)
print(r.json())
payload = {'title':'foo', 'body':'bar', 'userId':'1'}
headers = {'content-type': 'application/json'}
r = requests.post('http://jsonplaceholder.typicode.com/posts', data=json.dumps(payload), headers=headers)
print(r.status_code)
print(r.text)


