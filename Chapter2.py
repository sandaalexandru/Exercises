# Empty list

a = [1, 2, 2, 3, 5]
a.append(3)
print(a)
del a[3]
print(a)
a.remove(a[2])
print(a)
a.pop(2)
print(a)
a = []
print(a)

# Intersect, difference, union

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {5, 6, 7, 8}
print(b.intersection(c))
print(c.intersection(b))
print(a.union(b))
print(b.union(a))
print(a.difference(b))
print(b.difference(a))

# Key value

t = {'IBM':194, 'AAPL':416, 'GOOG':895}
for a, b in t.items():
    print("{key} => {value}".format(key=a,value=b))
keyss = list(t.keys())
valuess = list(t.values())
print(valuess[keyss.index('AAPL')])

# Kwags

def tag(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result
print(tag('img',src="monet.jpg",alt="Sunrise by Claude Monet",border=1))

# Min_list, max_list, sum

def min_lista(t):
    a = t[0]
    for i in t[1:]:
        if i < a: a = i
    return a

def max_lista(t):
    a = t[0]
    for i in t[1:]:
        if i > a: a = i
    return a

print(min_lista([1, 3, 0, 5, 7]))
print(min([1, 3, 0, 5, 7]))

print(max_lista([1, 3, 0, 5, 7]))
print(max([1, 3, 0, 5, 7]))

def sum_list(t):
    a = t[0]
    for i in t[1:]:
        a = a + i
    return a
print(sum_list([1, 3, 0, 5, 7]))
print(sum([1, 3, 0, 5, 7]))

def sort_lista_asc(t):
    a = []
    while t:
        minim = min_lista(t)
        t.remove(minim)
        a.append(minim)
    return a
print(sort_lista_asc([1, 3, 0, 5, 7]))
d = [1, 3, 0, 5, 7]
d.sort()
print(d)