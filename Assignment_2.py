# ---------------------------- Operations on Array --------------------------- #

#Creating an Array
companies = ["Nothing", "DBrand", "Nvidia", "Apple", "Samsung"]

print(companies)

#Length of an Array
print("Length of list: ", companies.__len__()) #using "__len__()" method
print("Length of list: ", len(companies)) #using "len()" function

#Append operation
companies.append("OnePlus")
print('Appended "OnePlus" at the end :',companies)

#Insertion of an element at a specified index
companies.insert(2, "Intel")
print('Inserted "Intel" :',companies)

#Deletion of the last element using "pop()" function
companies.pop()
print('Removed "OnePlus" from the end :',companies)

#Deletion of a specified element using "remove()" function
companies.remove("Intel")
print('Removed "Intel" :',companies)

#Sorting the list Alphabetically using "sort()" function
companies.sort()
print('Sorted Alphabetically :',companies)

#Finding the index of an element
indexOfNvidia = companies.index("Nvidia")
print('Index of "Nvidia" :',indexOfNvidia)

#Iritating through an array using "for-in" loop
print(" ")
print('Iritating through the list using "for-in" loop: ')
for company in companies:
    print(company)