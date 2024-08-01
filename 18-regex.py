# replace, find, validation => regex

import re

text = """

reza 
ali

ismryazdan@gmail.co.co.coc.ci

ismryazdan@gmail.com.

reza-reza-rez983492334.s.dadas.a

sdasd@mailna.co.com

ismry45.64az.dan@gmail.com.

9012313213213123@mailna.co.

rezayazdab@reza

12312312dsfsf@sdfs

12313@dfsdfds.cs

{reza@gmail.com
"""

email_phone_value = "ismryazdan@gmail.com"

# pattern = re.compile(r'\b([\w.-]+)@([\w.-]+\.\w{2,4})\b')
pattern = re.compile(r'\b(?P<before>[\w.-]+)@(?P<after>[\w.-]+\.\w{2,4})\b', flags=re.MULTILINE | re.IGNORECASE)

# for index, email in enumerate(pattern.findall(text)):
# for index, email in enumerate(re.findall(pattern, text)):
# for index, email in enumerate(re.findall(r'\b[\w.-]+@[\w.-]+\.\w{2,4}\b', text)):
#     print(index+1, email)

# if match_object := re.search(pattern, text):
#     print(match_object)
#     print(match_object.span())
#     print(match_object.group())
#     print(match_object.group(1))
#     print(match_object.group('before'))
#     print(match_object.group(2))
#     print(match_object.group('after'))
#     print(match_object.groups())
#     print(match_object.end())
#     print(match_object.start())

# replacement :
# text = re.sub(pattern, " 😎 ", text)

# print(text)

print(re.split(pattern, text))
