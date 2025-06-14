1.
txt = input("Matn yozing: ") # Misol uchun

result = ""
i = 0

while i < len(txt):
    result += txt[i]
    
    # Unli harflar ro'yxati
    unli = 'aeiouAEIOU'
    
    # Har uchinchi belgi va oxirgi belgi emas
    if (i + 1) % 3 == 0 and i != len(txt) - 1:
        # Agar hozirgi belgi unli bo'lsa yoki undan oldin underscore qo'yilgan bo'lsa
        if txt[i] in unli or (len(result) > 1 and result[-2] == '_'):
            if i + 1 < len(txt):
                result += txt[i + 1]
                result += "_"
                i += 1  # Keyingi belgi oldindan qo'shilgani uchun i ni oshiramiz
            # Agar oxirgi belgi bo'lsa, hech narsa qo'shmaymiz
        else:
            result += "_"
    i += 1

print(result)

2.
n = int(input())

for i in range(n):
    print(i ** 2)

# Input Format: first and only line contains the integer n
n = int(input())

# Constraints: 1 <= n <= 20
if 1 <= n <= 20:
    # Output Format: print i^2 for all 0 <= i < n, each on a new line
    for i in range(n):
        print(i ** 2)
else:
    print("n is out of allowed range (1 to 20)")

3.
#1
# # Exercise 1
i = 1
while i <= 10:
    print(i)
    i += 1

4.
#2
# Exercise 2
for row in range(1, 6):  # 1 dan 5 gacha (5 qatordan iborat)
    for num in range(1, row + 1):
        print(num, end=' ')
    print()  # har qatordan keyin yangi qatorga o'tish
5.
# Exercise 3: Calculate sum of all numbers from 1 to a given number

# Foydalanuvchidan son olish
num = int(input("Enter number: "))

# Yig‘indi hisoblash
total = 0
i = 1
while i <= num:
    total += i
    i += 1

# Natijani chiqarish
print("Sum is:", total)

6.
#4
# Foydalanuvchidan son olish
num = int(input("Enter a number: "))

# 1 dan 10 gacha bo‘lgan ko‘paytmalarni chiqarish
for i in range(1, 11):
    print(num * i)
7.
#5
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num > 70:
        print(num)


8.
#6
# Foydalanuvchidan son olish
num = int(input("Enter a number: "))

# Raqamlar sonini hisoblash
count = 0
while num != 0:
    num = num // 10  # sonni 10 ga bo'lib boramiz
    count += 1

print("Total digits:", count)

9.
#7
for i in range(5, 0, -1):           # 5 dan 1 gacha kamayadi
    for j in range(i, 0, -1):       # Har bir qator: i dan 1 gacha
        print(j, end=' ')
    print()                         # Har qatordan keyin yangi qator

10.
#8
list1 = [10, 20, 30, 40, 50]

# Ro'yxatni teskari tartibda chiqarish
for i in range(len(list1)-1, -1, -1):
    print(list1[i])
11.
#9
for num in range(-10, 0):
    print(num)

12.
#10
for i in range(5):
    print(i)
else:
    print("Done!")

13.
#11

# start = int(input("Enter start of range: "))
# end = int(input("Enter end of range: "))

# Boshlanish va tugash oralig'ini belgilash
start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1:  # Tub sonlar faqat 1 dan katta bo‘ladi
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break  # bo‘linadigan topilsa, bu tub emas
        else:
            print(num)

14.
#12
# Fibonachchi seriyasining 10 ta sonini chiqarish

n = 10  # nechta son kerak
a, b = 0, 1

print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b

15.
#13
# Faktorialni hisoblash

n = 5  # bu yerda istalgan sonni yozish mumkin
fact = 1

for i in range(1, n + 1):
    fact *= i

print(f"{n}! = {fact}")


16.
#14
from collections import Counter

list1 = [1, 1, 2]
list2 = [2, 3, 4]

# Har bir ro'yxatdagi elementlarni sanaymiz
c1 = Counter(list1)
c2 = Counter(list2)

# Umumiy elementlar (eng kam takrorlanganlar bo‘yicha)
common = c1 & c2

# Har bir ro'yxatdan umumiy elementlarni olib tashlaymiz
unique1 = list((c1 - common).elements())
unique2 = list((c2 - common).elements())

# Natijani birlashtiramiz
result = unique1 + unique2
print(result)

17.
#15
list1 = [1, 2, 3] 
list2 = [4, 5, 6]

list1.extend(list2)
new_list=list1
print(new_list)

18.
from collections import Counter

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

# Har bir ro'yxatdagi elementlarni sanaymiz
c1 = Counter(list1)
c2 = Counter(list2)

# Umumiy elementlarning minimal sonini topamiz
common = c1 & c2

# Har bir ro'yxatdan umumiy elementlarni olib tashlaymiz
unique1 = list((c1 - common).elements())
unique2 = list((c2 - common).elements())

# Natijani birlashtiramiz
result = unique1 + unique2
print(result)

19.
