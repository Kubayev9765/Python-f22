1.
num=[1, 3, 5, 9, 6, 11, 21, 90]

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
result=list(filter(is_prime, num))
result_2=list(map(is_prime, num))
print(result)
print(result_2)

2.
son=[348, 278,561]
def digit_sum(k):
    return sum(int(r) for r in str(abs(k)))
result=list(map(digit_sum,son))
# result_2=list(filter(digit_sum,son))
# print(result_2)
print(result)

3.
def powers_of_two(n):
    k = 1
    result = []
    while (2 ** k) <= n:
        result.append(2 ** k)
        k += 1
    print(*result)

powers_of_two(10)
