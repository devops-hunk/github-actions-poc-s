l = [10, 20, 30, 15, 20, 25, 26]

dict = {}

for i in l:
    if i in dict:
        print("Duplicate found: {}".format(i))
    else:
        dict[i] = 1
