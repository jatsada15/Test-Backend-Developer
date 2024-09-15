def find_max_index(number):
    if len(number) == 0:
        return "list can not be blank"
    max_index = 0
    for i in range(1, len(number)):
        if number[i] > number[max_index]:
            max_index = i
    return max_index
print(find_max_index([1,2,1,3,5,6,4]))
print(find_max_index([]))