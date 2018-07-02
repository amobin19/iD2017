bool1 = True;
store1 = 0;
store2 = 0;
store3 = 0;
store4 = 0;
list1 = []
while(bool1 == True):
    keys = input("Directions in ^ (North) or v (South) or < (East) or > (West): ")
    if(keys == "^"):
        store1 += 1
        print("store1", store1)
        list1.append("store1")
    elif(keys == ">"):
        store2 += 1
        print("store2", store2)
        list1.append("store2")
    elif(keys == "<"):
        store3 += 1
        print("store3", store3)
        list1.append("store3")
    elif(keys == "v"):
        store4 += 1
        print("store4", store4)
        list1.append("store4")
    else:
        break;
print("These are the number of times each store has been visited: ")
print("Store 1:", store1)
print("Store 2:", store2)
print("Store 3:", store3)
print("Store 4:", store4)
print("Only", len(list1), "store have been visited.")
