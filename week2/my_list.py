my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)
print (my_list)
my_list.extend([50, 60, 70])
print (my_list)

my_list.remove(my_list[-1])
print (my_list)

my_list.sort()
indexOf30 = my_list.index(30)
print(indexOf30)


