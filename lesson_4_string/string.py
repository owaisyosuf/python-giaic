msg:str = "pakistan zindabad we love our country" #single line string with double quote
print (msg)

msg1:str = 'pakistan zindabad we love our country' #single line string with single quote
print (msg1)

msg2:str = """pakistan zindabad
we love our country""" #multi line string with triple double quote
print (msg2)

msg3:str = '''pakistan zindabad 
we love our country''' #multi line string with triple single quote
print (msg3)

name:str = "owais"
print("my name is",name)
print(f"my name is {name}")

#Concatenation
first_name:str = "owais"
last_name:str = "yousuf"
full_name:str = first_name + " " + last_name
print(full_name)

#INDEXING
name:str = "owais"
print(name[0]) #o 
print(name[1]) #w

#SLICING
name:str = "owais"
print(name[0:3]) #owa
print(name[0:4]) #owai

#LENGTH
name:str = "owais"
print(len(name))

#STRIP
name:str = "    owais    "
print(name.strip()) #owais

#LOWER
name:str = "OWAIS"
print(name.lower()) #owais

#UPPER
name:str = "owais"
print(name.upper()) #OWAIS

#SPLIT
name:str = "owais yousuf"
print(name.split()) #['owais', 'yousuf']
print(name.split("a")) #['ow', 'is yo', 'suf']
