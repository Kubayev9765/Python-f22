1.
fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]
fruit=fruits[2]
print(fruit)  

2.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
new_list = list1 + list2
print(new_list)

3.
my_list=[3,5 ,9,5,21,8,12,45,65, 1]
#O'rta index ni topish
Urta_index = my_list[len(my_list) // 2]
print(Urta_index)
result = [my_list[0], my_list[Urta_index], my_list[-1]]
print(result

4.
movies = ["O'tgan kunlar", "Shaytanat", "Shum bola", "Navda", "Qashqirlar makoni"]
my_tupl=tuple(movies)
print(movies)
print(my_tupl)

5.
City=input("Shahar nomini kiriting: ")
shaharlar = ["Samarqand", "Xorazm", "Paris", "Toshkent", "Parij"]
if City in shaharlar:
    print(City, " ro'yhatda mavjud!")
else:
    print(City ," ro'yhatda mavjud emas.")

6.
my_list = [1, 66, 2, 91,  3, 77, 4, 5]
my_list_2 =my_list.copy() 
print(my_list_2)


7.
my_list = [1, 66, 2, 91,  3, 77, 4, 5]
if len(my_list)>1:
    my_list[0], my_list[-1]=my_list[-1], my_list[0]
    print(my_list)
else:
        print(my_list)

8.
my_tupl=(1, 2, 3, 4, 5, 6, 7, 8, 9, 11)
tupl=my_tupl[3:8]
print(tupl)

9.
rang=input("Yoqtirgan rangingizni kiriting: ")
ranglar=["oq", "qizil", "ko'k", "sariq", "ko'k"]
kuk_rang=ranglar.count(rang)
print(kuk_rang)

10.
animals = ("tiger", "elephant", "lion", "zebra", "giraffe","lion")
lion_index = animals.index("lion")
print(lion_index)

11.
tuple1 = (9, 22, 35)
tuple2 = (43, 55, 69)
umumiy_tuple = tuple1 + tuple2
print(umumiy_tuple)

12.
my_list = [14, 43, 2, 54, 33, 45, 52]
my_tuple = (15, 65, 27, 76, 39, 40)
list_length = len(my_list)
tuple_length = len(my_tuple)
print('my_list ni uzunligi:',list_length,' my_tuple ni uzunligi:', tuple_length)

13.
my_tuple=(45, 43, 56, 87, 93, 100, 98)
my_List=list(my_tuple)
print(my_List)

14.
my_tuple = (113, 543, 500, 220, 53, 470, 195)
#Finding the maximum and minimum values
eng_kattasi = max(my_tuple)
eng_kichigi = min(my_tuple)
# Printing the results
print("Eng katta qiymat: ", eng_kattasi)
print("Eng kichik qiymat: ", eng_kichigi)

15.
cars_tuple = ("Merccedes", "BMW", "Audi", "Porsha")
reverse_car = tuple(reversed(cars_tuple))
print(reverse_car)

cars_tuple = ("Merccedes", "BMW", "Audi", "Porsha")
# Reversing the tuple
reversed_car = tuple(reversed(cars_tuple))
# Printing the reversed tuple
print(reversed_car)
