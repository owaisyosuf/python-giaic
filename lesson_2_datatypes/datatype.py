#data types

#01 Numeric Type
#A-int
num:int=10
print(num)
print(type(num))

#B-float
num:float=10.5
print(num)  
print(type(num))

#complex
num:complex=10+5j
print(type(num))

#2 boolean
true:bool=True
false:bool=False
print(true)
print(false)  
print(type(true))
print(type(false))

#3 sequence type
#A-String
msg:str= "pakistan zindabad we love our country" #string with double quotes
msg1:str='pakistan zindabad we love our country' #string with single quotes
msg2:str='''pakistan zindabad 
            we love our country''' #multiline string with triple quotes
msg3:str="""pakistan zindabad 
            we love our country""" #multiline string with triple quotes
name:str="owais yousuf "

print(f"my name in {name}")#this is f string
print("this is from msg : " +msg)
print(type(msg))

#B-List
list1:list=[1,2,3,4,5,6,7,8,9,10]
print(list1)
print(type(list1))
list2:list=["owais",1,true,10.5]
print(list2)  
print(type(list2))

#c-Tuple
tuple1:tuple=(1,2,3,4,5,6,7,8,9,10)
print(tuple1) 
print(type(tuple1))
tuple2:tuple=("owais",1,true,10.5)
print(tuple2)
print(type(tuple2))

#d-range
range1:range=range(0,10,2)
print(range1)
print(type(range1))

#E-Set
set1:set={1,2,3,4,5,6,7,8,9,10}
print(set1)  
print(type(set1))


#4-id
name:str="owais yousuf"
num:int=10
num1:int=10
print(id(name))
print(id(num))
print(id(num1))

num2:int=100000
num3:int=100000
print(id(num2))
print(id(num3))

name1:str="owais yousuf"
name2:str="owais yousuf"
print(id(name1))
print(id(name2))

name3:str="abc"
name4:str="abc"
print(id(name1))
print(id(name2))

#5-Dictionary
dic1:dict={"name":"owais","age":25} 
print(dic1)
print(type(dic1))
dic2:dict={"name":["owais","ali","umer"],"age":[25,30,35]}
print(dic2)
print(type(dic2))

#6-None
none1=None  
print(none1)
print(type(none1))

#7-type casting
num:int=10
print(num)
print(type(num))
num:float=float(num)
print(num)    
print(type(num))
num:str=str(num)
print(num)    
print(type(num))