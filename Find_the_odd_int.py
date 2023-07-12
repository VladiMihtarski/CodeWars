# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
def find_it(seq):
    element_count = {}
    
    # Преброяване на срещанията на всеки елемент в масива
    for element in seq:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    # Намиране на елемента с нечетен брой срещания
    for element, count in element_count.items():
        if count % 2 != 0:
            return element
    
    return None

seq = [1, 2, 3, 2, 1, 3, 1]
result = find_it(seq)
print(result)  # Извежда: 2
