# different operations perform on a data type

#integer
x=10
print("integer:",x,type(x))

#float
y=3.14
print("float:",y,type(y))

# strings
name="john"
print("string:",name,type(name))

#boolean
is_admin=True
print("boolean:",is_admin,type(is_admin))

#list
numbers=[1,2,3,4,5]
print("list:",numbers,type(numbers)) 

#tuple 
colors = ("red","green","blue")
print("tuple:",colors,type(colors))

# dictionary
person={"name":"john","age":30}
print("dictionary:",person,type(person))

# loop 
for i in range(7):
    print("shikha soni")

# program to print a number from 5 to 15 using while loop
i = 5
while i<=15:
    print(i)
    i+=1    

# a list containing strings and number
student=['jack',32,'computer science']
print(student)

#empty list
empty_list=[]
print(empty_list)

# creating an dictionary
country_capitals={"germany":"berlin","canada":"ottwa","england":"london"}
print(country_capitals)

# functions to calculate the area using simple multiplication
def area_simple_multiplication(length,width):
    return length*width
length=5
width=8
result=area_simple_multiplication(length,width)
print("the area of a rectangle is:",result)