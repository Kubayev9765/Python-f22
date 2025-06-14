1.
 must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
2.
n = int(input())

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

3.
a = 3
b = 15
a)
def even_numbers_if_else(a, b):
    if a <= b:
        start = a if a % 2 == 0 else a + 1
        return list(range(start, b + 1, 2))
    else:
        start = a if a % 2 == 0 else a - 1
        return list(range(start, b - 1, -2))    
b)
even_numbers = list(filter(lambda x: x % 2 == 0, range(a, b + 1))) if a <= b else list(filter(lambda x: x % 2 == 0, range(b, a + 1)))
print(even_numbers)
c)
even_numbers = list(filter(lambda x: x % 2 == 0, range(min(a, b), max(a, b) + 1)))

print(even_numbers)
