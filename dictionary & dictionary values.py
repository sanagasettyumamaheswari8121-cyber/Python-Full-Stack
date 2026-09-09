Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict
a={"name":"pooja","city":"vij"}
print(a)
{'name': 'pooja', 'city': 'vij'}
type(a)
<class 'dict'>
b={"name","pooja"}
type(b)
<class 'set'>

#methods
#keys
a={"year":2026,"month":"sep","date":9}
a.keys()
dict_keys(['year', 'month', 'date'])

#values
a.values()
dict_values([2026, 'sep', 9])

#items
a.items()
dict_items([('year', 2026), ('month', 'sep'), ('date', 9)])
a["year"]
2026
a[2026]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a[2026]
KeyError: 2026
a.get("year")
2026

#update
a={"name":"Uma","city":"vij"}
a.update({"mailid":"uma@gamil.com})
          
SyntaxError: unterminated string literal (detected at line 1)
a.update({"mailid":uma@gamil.com})
          
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.update({"mailid":uma@gamil.com})
NameError: name 'uma' is not defined
a.update({"mailid":uma@gmail.com})
          
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.update({"mailid":uma@gmail.com})
NameError: name 'uma' is not defined
a={"name":"uma","city":"vij"}
          
a.update({"mailid":"uma@gmail.com"})
          
a
          
{'name': 'uma', 'city': 'vij', 'mailid': 'uma@gmail.com'}
a.update({"year":2026},{"time":3})
          
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.update({"year":2026},{"time":3})
TypeError: update expected at most 1 argument, got 2
a.update({"year":2026,"time":3})
          
a
          
{'name': 'uma', 'city': 'vij', 'mailid': 'uma@gmail.com', 'year': 2026, 'time': 3}

#set default
          
a={"hour":3,"min":10}
          
a.setdefault("sec",4)
          
4
a
          
{'hour': 3, 'min': 10, 'sec': 4}

#pop
          
a={"week":"wed","date":9}
          
a.pop()
          
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("week")
          
'wed'
a
          
{'date': 9}

#pop item
          
a={"country":"india","state":"ap"}
          
a.popitem()
          
('state', 'ap')
a
          
{'country': 'india'}
a.popitem()
          
('country', 'india')
a
          
{}

#copy
          
a={"name":"uma","course":"python","duration":100}
          
a.copy()
          
{'name': 'uma', 'course': 'python', 'duration': 100}

#len
          
a.len()
          
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.len()
AttributeError: 'dict' object has no attribute 'len'
len(a)
          
3

#count
          
a.count("name")
          
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'

#index
          
a.index("course")
          
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.index("course")
AttributeError: 'dict' object has no attribute 'index'

a.clear()
          
a
          
{}

a#duplicate values
...           
{}
>>> a={"name":"uma","year":2026,"name":"uma"}
...           
>>> print(a)
...           
{'name': 'uma', 'year': 2026}
>>> 
>>> a={"name":"uma","year":2026,"name":"priya"}
...           
>>> a
...           
{'name': 'priya', 'year': 2026}
>>> 
>>> a={"name":"uma","year":2026,"name1":"uma"}
...           
>>> a
...           
{'name': 'uma', 'year': 2026, 'name1': 'uma'}
>>> 
>>> #1 key no of values
...           
>>> a={"idnos":[10,20,30],"names":["uma","ammu","pandu"],"places":["vij","hyd","ban"]}
...           
>>> a
...           
{'idnos': [10, 20, 30], 'names': ['uma', 'ammu', 'pandu'], 'places': ['vij', 'hyd', 'ban']}
>>> type(a)
...           
<class 'dict'>
>>> a.keys()
...           
dict_keys(['idnos', 'names', 'places'])
>>> a.values()
...           
dict_values([[10, 20, 30], ['uma', 'ammu', 'pandu'], ['vij', 'hyd', 'ban']])
>>> a.items()
...           
dict_items([('idnos', [10, 20, 30]), ('names', ['uma', 'ammu', 'pandu']), ('places', ['vij', 'hyd', 'ban'])])
