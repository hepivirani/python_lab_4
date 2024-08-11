dict = {'id' : 1 , 'Name': 'abc', 'designation': 'manager', 'salary': 50000}

print(dict)

dict["name"] = 'xyz'
print("updated dictionary:",dict)

del dict['designation']
print("after deletion:",dict)
