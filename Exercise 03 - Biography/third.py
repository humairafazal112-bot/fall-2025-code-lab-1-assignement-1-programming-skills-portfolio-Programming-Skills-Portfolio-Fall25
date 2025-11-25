# Exercise 3: Biography - 25 Marks

#Ask the usserr for their info
name=input("Enter your name: ")
hometown=input(":Enter your hometown: ")
age=int(input("Enter your age: "))#use of int so it can be save as number

#store the details in a dictionary
bio = {"name": name,
"hometown": hometown,
"age" : age 
}

#print them
print("Name:", bio["name"])
print("Hometown: ", bio["hometown"])
print("age:" ,bio["age"])


print("Name:", bio["name"], "\nHometown:", bio["hometown"], "\nAge:", bio["age"])

