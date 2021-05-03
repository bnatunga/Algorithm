#finds an element in a list
def find_ele(list_, ele):
    for i in list_:
        if i == ele:
            return True
        return False

lst = [3, 15, 23, 37]
print(find_ele(lst, 2))

#using random module to generate a list of random numbers in range
import random
def random_list(N, sort=False):
    list_ = [random.randint(0, 10*N) for _ in range(N)]
    return sorted(list_) if sort else list_

print(random_list(5))

#finds an element in a sorted list
def find_ele_sorted(list_, ele):
    for i in list_:
        if i == ele:
            return True
        if i > ele:
            return False
        return False

#binary search(a recursive algorithm that allows the list to be divided roughly in half on each recursive step)
def find_ele_binary(l_, ele):
    if len(l_) < 1:
        return False
    mid_point = len(l_)//2
    if l_[mid_point] == ele:
        return True
    elif l_[mid_point] > ele:
        return find_ele_binary(l_[:mid_point], ele)
    else:
        return find_ele_binary(l_[mid_point+1:], ele)