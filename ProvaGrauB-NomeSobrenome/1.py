import random

def shuffle_array(array):
    n = len(array)
    for _ in range(n):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)

        array[i], array[j] = array[j], array[i]
    return array


array = ['a', 'b', 'c', 'd', 'e']
shuffle_array= shuffle_array(array)
print(shuffle_array)