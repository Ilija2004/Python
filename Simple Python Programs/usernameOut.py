Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ("It's Friday")
It's Friday
>>> 
======================== RESTART: H:/coding/username.py ========================
Please enter your Name : ilija
Please enter your Age : 17
Traceback (most recent call last):
  File "H:/coding/username.py", line 3, in <module>
    print(userName+",You were born in ",2021-UserAge+".")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
======================== RESTART: H:/coding/username.py ========================
Please enter your Name : ilija
Please enter your Age : 17
ilija,You were born in  2004
>>> 
======================== RESTART: H:/coding/username.py ========================
Please enter your Name : ilija
Please enter your Age : 17
ilija,You were born in  2004 .
>>> 
======================== RESTART: H:/coding/username.py ========================
Please enter your Name : ilija
Please enter your Age : 7
Traceback (most recent call last):
  File "H:/coding/username.py", line 3, in <module>
    print(userName+" ,you were born in ",2021-UserAge+".")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
======================== RESTART: H:/coding/username.py ========================
Please enter your Name : ilija
Please enter your Age : 19
Traceback (most recent call last):
  File "H:/coding/username.py", line 3, in <module>
    print(userName+" ,you were born in ",2021-UserAge+chr(46))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
======================== RESTART: H:/coding/username.py ========================
Please enter your Name : ilija
Please enter your Age : 17
ilija ,you were born in  2004.
>>> 
======================== RESTART: H:/coding/username.py ========================
Please enter your Name : ilija
Please enter your Age : 17
ilija ,you were born in 2004.
>>> 
======================== RESTART: H:/coding/username.py ========================
Please enter your Name : ilija
Please enter your Age : 17
ilija, you were born in 2004.
>>> 
======================== RESTART: H:/coding/username.py ========================
Please enter your Name : Ilija
Please enter your Age : 17
Ilija, you were born in 2004.
>>> 
======================== RESTART: H:/coding/username.py ========================
Please enter your Name : ilija
Please enter your Age : 17
ilija, you were born in 2004.
>>> 