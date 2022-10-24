# zad1
# 1a

def func1a (a):
    dict = {}
    for x in a:
        if x not in dict.keys():
            dict.update({x:1})
        else:
            dict[x] += 1
    return dict

# 1b

def func1b (a):
    dict = {}
    for x in a:
        if x.isalpha():
            if x not in dict.keys():
                dict.update({x:1})
            else:
                dict[x] += 1
    return dict

# 1c

def func1c (a):
    dict = {}
    a = a.lower()
    for x in a:
        if x.isalpha():
            if x not in dict.keys():
                dict.update({x:1})
            else:
                dict[x] += 1
    return dict

# 1d

def func1d(a):
    a = a.lower()
    dict = {}
    i = 0
    for x in a:
        if x.isalpha():
            if x not in dict.keys():
                dict.update({x: 1})
            else:
                dict[x] += 1
        else:
            i += 1
    if len(a) == i:
        return "Brak liter"
    return max(dict, key=dict.get)

# czytanie ze standardowego wejścia

a = input("Podaj łańcuch znaków: ")
print(func1a(a))
print(func1b(a))
print(func1c(a))
print(func1d(a))

# czytanie z pliku

f = open("tekst.txt")
c = f.read()
print(func1a(c))
print(func1b(c))
print(func1c(c))
print(func1d(c))
f.close()

# zad 2
dict = {}

while True:
    a = input("Podaj liczbę: ")
    if not a:
        break
    else:
        if a not in dict.keys():
            dict.update({a:1})
        else:
            dict[a] += 1

print(dict)
# zad3
dict = {}

a = open("tekst.txt")
b = a.read()
b = b.lower()

for x in b:
    if x.isalpha():
        if x not in dict:
            dict.update({x:1})
        else:
            dict[x] += 1

print(dict)
a.close()

# zad 4

f = open("tekst.txt")
b = f.readlines()
dict = {}

for l in b:
    a = l.split()
    for x in a:
        if x.isnumeric():
            if x not in dict:
                dict.update({x: 1})
            else:
                dict[x] += 1
print(dict)

f.close()