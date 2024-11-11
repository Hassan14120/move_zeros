def move_zeros(list):
    for i in list:
        if i == 0:
            list.remove(i)
            list.append(0)
    return list

list = [1,2,3,0,4,0,5,6]
print(move_zeros(list))