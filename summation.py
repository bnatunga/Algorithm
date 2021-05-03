#sums all the numbers between 1 and N (inclusive).
def sum_num(N):
    sum_ = 0
    for n in range(N + 1):
        sum_ += n
    return sum_

print(sum_num(15))

#Gauss summation rule
def sum_gauss(N):
    return N*(N+1)//2

print(sum_gauss(15))