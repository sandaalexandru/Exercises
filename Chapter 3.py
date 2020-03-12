# Scrierea in fisier

f = open('testwrite.txt', mode = 'wt', encoding = 'utf-8')
print(f.write("Test linia 1, "))
f.write('continuare linia 1\n')
f.write('Sfarsit de fisier care e linia 2')
f.close()

# Citirea din fisier

g = open('testwrite.txt', mode='rt', encoding='utf-8')
print(g.read(14))
print(g.read())
print(g.seek(0))
print(g.readline())
print(g.readline())
print(g.readline())
print(g.seek(0))
print(g.readline())
print(g.seek(0))
print(g.readlines())
g.close()

# Exceptions

x,y = (5, 0)
try:
    z = y/x
except:
    z = x/y
finally:
    print("Final de program")
print(z)





