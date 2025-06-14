1.
my_dict = {
    'apple': 10,
    'banana': 5,
    'cherry': 7,
    'date': 3
}

for value in my_dict.values():
    print(value)

2.
my_dic={0: 10, 1: 20}
my_dic[2]=30
print(my_dic)

3.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

my_dict=dict()
my_dict.update(dic1)
my_dict.update(dic2)
my_dict.update(dic3)
print(my_dict)

4.
n=int(input("Biror sonni kiriting: "))

my_dic={i:i*i for i in range(1, n+1)}
my_dic
my_dic_2={}
for i in range(1, n+1):
    my_dic_2[i]= i*i
print(my_dic_2)

5.
my_dict={i: i**2 for i in range(1, 16)}
my_dict

my_dict_2={}
for i in range(1, 16):
    my_dict_2[i]=i * i
print(my_dict_2)

1.
my_set={320,32,23,24,1,3,5,100}
print(my_set)

2.
my_set={320,32,23,24,1,3,5,100}
for n in my_set:
    print(n)

3.
my_set={320,32,23,24,1,3,5,100}
my_set.update([8,7,6])
print(my_set)

4.
my_set={320,32,23,24,1,3,5,100}
my_set.update([8,7,6])
print(my_set)
my_set.remove(100)
my_set.remove(320)
print(my_set)

5.
my_set={320,32,23,24,1,3,5,100}
my_set.update([8,7,6])
my_set.discard(100)
my_set.discard(320)
my_set.discard(500)
print(my_set)






