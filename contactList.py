name=[]
phone_number=[]
num=3
for i in range(num):
    names=input("Name: ")
    phone_numbers=input("Phone number: ")

    name.append(names)
    phone_number.append(phone_numbers)
print("Name \t\t phone Number\n")
for i in range(num):
    print("{}\ t\t{}".format(name[i], phone_number[i]))

search_term=input("\n Enter serch term: ")
print("Search result: ")

if search_term in name:
    index =name.index(search_term)
    phone_numbers=phone_number[index]
    print("Name :{}, Phone Number :{}".format(search_term, phone_numbers))

else:
    ("Name Not Found")
