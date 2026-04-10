Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> bucketlist=["learn french" , "python" , "drink water" , "eat food" , "skydive"]
>>> type(bucketlist)
<class 'list'>
>>> bucketlist[4]
'skydive'
>>> L1=(12 ,34 ,56 ,67 ,89 , 90)
>>> len(L1)
6
>>> max(L1)
90
>>> min(L1)
12
>>> L1=('g' , 34 , 'gf' , 67 , 'gfh' , 7 , 5)
>>> len(l1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    len(l1)
NameError: name 'l1' is not defined
>>> len(L1)
7
>>> max(L1)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    max(L1)
TypeError: '>' not supported between instances of 'int' and 'str'
>>> #NOT SUPPORTED BW STRINGS
>>> t1=["one" , 2 , "three" , 4 , "five" , 6 ]
>>> len(t1)
6
>>> max(t1()
max(t1)
    
SyntaxError: invalid syntax
>>> min(t1)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    min(t1)
TypeError: '<' not supported between instances of 'int' and 'str'
>>> #NOT SUPPORTED
>>> #FORMATTING LISTS
>>> L1=["butter" , "chicken" , "shawarma" , "eggroll" , "tikka" ]
>>> list(L1)
['butter', 'chicken', 'shawarma', 'eggroll', 'tikka']
\
>>> tuple[L1]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    tuple[L1]
TypeError: 'type' object is not subscriptable
>>> tuple(L1)
('butter', 'chicken', 'shawarma', 'eggroll', 'tikka')
>>> L1=["butter" , "chicken" , "shawarma" , "eggroll" , "tikka" ]
>>> L1.append('soya bean')
>>> 
>>> L1.append('soya bean')
>>> 
>>> L1.insert('soya chaap')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    L1.insert('soya chaap')
TypeError: insert() takes exactly 2 arguments (1 given)
>>> L2=['Tailor Swift', 'Ed Sheeran', 'Imagine Dragons', 'Pink', 'Maroon 5']
>>> L2.append('eminem')
>>> 
>>> [1,2]+[4]
[1, 2, 4]
>>> [1,2]*[4]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    [1,2]*[4]
TypeError: can't multiply sequence by non-int of type 'list'
>>> max('ten' , 'twenty' , 'thirty' )
'twenty'
>>> pages=[11 , 13 , 15 , ( 37 , 21 ,43 , ), 17 , 19 , 21]
>>> tuple'1,2')
SyntaxError: invalid syntax
>>> L1=['python' , 'java' , 'css']
>>> L1.insert(len(L1), 'sql')
>>> L1.insert(len(L1), 'sql')
>>> 
>>> 
>>> 
>>> 
