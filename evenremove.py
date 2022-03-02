list_nos = [1,2,3,4,5,6,7,8,9,10]
for i in list_nos:
    if (i % 2 == 0):
        list_nos.remove(i)
print("the list after removing even number:")
print(list_nos)