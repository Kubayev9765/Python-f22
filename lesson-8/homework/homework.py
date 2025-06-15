# 1
#a)
try:
    # Foydalanuvchidan ikkita son kiritishni so'raymiz
    son1 = float(input("Birinchi sonni kiriting: "))
    son2 = float(input("Ikkinchi sonni kiriting (bo'luvchi): "))

    # Bo'lish amalini bajarish
    natija = son1 / son2
    print("Natija:", natija)

except ZeroDivisionError:
    print("Xatolik: Sonni nolga bo'lish mumkin emas.")

except ValueError:
    print("Xatolik: Iltimos, faqat son kiriting.")

except Exception as e:
    print("Boshqa xatolik yuz berdi:", e)

#b)___________________________________________________________________________

def Sum_Zero (a, b):
 
    try:
        sum=a/b
        print(f"Natija: {sum}")
    except ZeroDivisionError:
        print("0 soniga bo'lish mumkin emas")
  
a = float(input("1- sonni kiriting: "))
b = float(input("2- sonni kiriting: "))
Sum_Zero(a, b)


#2
#a)
try:
    son = int(input("Iltimos, butun son kiriting: "))
    print("Siz kiritgan son:", son)

except ValueError:
    print("Xatolik: Bu butun son emas. Iltimos, faqat butun son kiriting.")
#b)______________________________________________________________________
def Butun_son():
    Son = input("Son kiriting: ")
    if not Son.strip().lstrip('-').isdigit():
        raise ValueError("Kiritilgan son butun son emas.")
    return int(Son)

try:
    number = Butun_son()
    print(f"Butun son kiriting!: {number}")
except ValueError as e:
    print(f"Xatolik: {e}")


#3
#a)
try:
    fayl_nomi = input("Iltimos, ochiladigan fayl nomini kiriting: ")
    with open(fayl_nomi, 'r') as fayl:
        mazmuni = fayl.read()
        print("Fayl mazmuni:")
        print(mazmuni)

except FileNotFoundError:
    print("Xatolik: Bunday fayl topilmadi. Iltimos, fayl nomini tekshiring.")
#b)----------------------------------------------------------------------------
def open_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:\n", contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage
filename = input("Enter the name of the file to open: ")
open_file(filename)


#4
#a)
try:
    # Foydalanuvchidan raqamlarni kiritishni so'raymiz
    a = input("Birinchi raqamni kiriting: ")
    b = input("Ikkinchi raqamni kiriting: ")

    # Kirishlar raqam ekanligini tekshiramiz
    if not a.replace('.', '', 1).isdigit() or not b.replace('.', '', 1).isdigit():
        raise TypeError("Xatolik: Faqat raqam kiriting.")

    # Agar to'g'ri bo'lsa, float ga aylantiramiz
    a = float(a)
    b = float(b)

    # Raqamlar bilan amallar
    print("Yig'indisi:", a + b)

except TypeError as e:
    print("TypeError:", e)

#b)-----------------------------------------------------

try:
    # Foydalanuvchidan raqamlarni kiritishni so'raymiz
    a = input("Birinchi raqamni kiriting: ")
    b = input("Ikkinchi raqamni kiriting: ")

    # Kirishlar raqam ekanligini tekshiramiz
    if not a.replace('.', '', 1).isdigit() or not b.replace('.', '', 1).isdigit():
        raise TypeError("Xatolik: Faqat raqam kiriting.")

    # Agar to'g'ri bo'lsa, float ga aylantiramiz
    a = float(a)
    b = float(b)

    # Raqamlar bilan amallar
    print("Yig'indisi:", a + b)

except TypeError as e:
    print("TypeError:", e)


#5
#a)
try:
    fayl_nomi = input("Iltimos, ochiladigan fayl nomini kiriting: ")
    
    # Faylni o‘qish uchun ochamiz
    with open(fayl_nomi, 'r') as fayl:
        mazmuni = fayl.read()
        print("Fayl mazmuni:")
        print(mazmuni)

except PermissionError:
    print("Xatolik: Faylga ruxsat yo‘q. Iltimos, ruxsatlarni tekshiring.")

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi. Fayl nomini tekshiring.")

except Exception as e:
    print("Boshqa xatolik yuz berdi:", e)
#b)---------------------------------------------------------------------------------
def open_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except PermissionError:
        print(f"Permission denied: You do not have the rights to access '{filename}'.")
    except FileNotFoundError:
        print(f"File not found: '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
file_path = input("Enter the path to the file you want to open: ")
open_file(file_path)



#6
#a)
try:
    my_list = [10, 20, 30, 40, 50]
    print("List:", my_list)

    index = int(input("Enter the index of the element you want to access: "))
    
    # Try accessing the element at the specified index
    print("Element at index", index, "is:", my_list[index])

except IndexError:
    print("IndexError: The index you entered is out of range.")

except ValueError:
    print("ValueError: Please enter a valid integer index.")

except Exception as e:
    print("An unexpected error occurred:", e)
#b)-------------------------------------------------------

def access_list_element(my_list, index):
    try:
        # Try to access the element at the given index
        element = my_list[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        
        print(f"Error: Index {index} is out of range for the list.")

sample_list = [10, 20, 30, 40, 50]
access_list_element(sample_list, 2)
access_list_element(sample_list, 10)


#7
#a)

try:
    number = input("Please enter a number: ")
    number = float(number)
    print("You entered:", number)

except KeyboardInterrupt:
    print("\nKeyboardInterrupt: Input cancelled by the user.")

except ValueError:
    print("ValueError: That is not a valid number.")

except Exception as e:
    print("An unexpected error occurred:", e)

#b)----------------------------------------------------------

def main():
    try:
        number = input("Please enter a number: ")
        print(f"You entered: {number}")
    except KeyboardInterrupt:
        print("\nInput cancelled by user.")

if __name__ == "__main__":
    main()


#8
#a)

try:
    a = float(input("Enter the numerator: "))
    b = float(input("Enter the denominator: "))

    result = a / b
    print("Result of division:", result)

except ArithmeticError:
    print("ArithmeticError: An error occurred during the arithmetic operation.")

except ValueError:
    print("ValueError: Please enter valid numbers.")

except Exception as e:
    print("An unexpected error occurred:", e)

#b)-------------------------------------------------

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is: {result}")
    except ArithmeticError as e:
        print(f"An arithmetic error occurred: {e}")

num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

divide_numbers(num1, num2)

#9
#a

try:
    filename = input("Enter the file name to open: ")

    # Try to open the file assuming it's UTF-8 encoded
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("File content:")
        print(content)

except UnicodeDecodeError:
    print("UnicodeDecodeError: The file contains characters that can't be decoded using UTF-8.")

except FileNotFoundError:
    print("FileNotFoundError: The file does not exist.")

except PermissionError:
    print("PermissionError: You do not have permission to read this file.")

except Exception as e:
    print("An unexpected error occurred:", e)

#b)-------------------------------------------------------

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File content:\n", content)
    except UnicodeDecodeError:
        print("Error: Could not decode the file due to an encoding issue.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
read_file('example.txt')


#10
#a)

try:
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)

    # Let's intentionally use a nonexistent method to cause AttributeError
    my_list.sortedd()  # Typo: should be my_list.sort()

except AttributeError:
    print("AttributeError: The list object has no such attribute or method.")

except Exception as e:
    print("An unexpected error occurred:", e)

#b)-------------------------------------------------------

def perform_list_operation():
    my_list = [1, 2, 3, 4, 5]

    try:
        # Attempting to use a non-existent method 'append_all'
        my_list.append_all([6, 7, 8])
    except AttributeError as e:
        print(f"AttributeError caught: {e}")
        print("Attempting valid operation instead...")

        # Correct method to append multiple elements
        my_list.extend([6, 7, 8])

    print("Updated list:", my_list)

if __name__ == "__main__":
    perform_list_operation()

#11
#a)

# Fayl nomini belgilang
file_nomi = "matn.txt"

try:
    # Faylni ochamiz va hamma matnni o'qib chiqamiz
    with open(file_nomi, "r", encoding="utf-8") as fayl:
        matn = fayl.read()
        print("Fayl mazmuni:")
        print(matn)

except FileNotFoundError:
    print("Fayl topilmadi. Iltimos, fayl nomini tekshiring.")
except UnicodeDecodeError:
    print("Faylni o'qishda kodlash (encoding) bilan bog'liq xatolik yuz berdi.")
except Exception as e:
    print("Noma'lum xatolik:", e)

#b)------------------------------------------------------------------------------

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File Content:\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'example.txt'  # Replace this with your file path
read_file(file_path)

#12
#a)
# Fayl nomini va nechta qator o'qish kerakligini foydalanuvchidan olamiz
file_name = input("Fayl nomini kiriting: ")
n = int(input("Nechta qatordan iborat qismini o'qishni xohlaysiz? "))

try:
    # Faylni o'qish rejimida ochamiz
    with open(file_name, "r", encoding="utf-8") as file:
        for i in range(n):
            line = file.readline()
            if not line:  # Fayl tugagan bo‘lsa
                break
            print(line.strip())  # Qatorni chop etamiz, oxiridagi \n belgilarisiz

except FileNotFoundError:
    print("Fayl topilmadi.")
except UnicodeDecodeError:
    print("Kodlash bilan bog'liq xatolik yuz berdi.")
except Exception as e:
    print("Xatolik:", e)

#b)--------------------------------------------------------------------

def read_first_n_lines(file_name, n):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for i in range(n):
                line = file.readline()
                if not line:
                    break  # Stop if file has fewer than n lines
                print(line.strip())  # Remove trailing newline
    except FileNotFoundError:
        print("File not found. Please check the file name.")
    except UnicodeDecodeError:
        print("Encoding error while reading the file.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
file_name = input("Enter the file name: ")
n = int(input("Enter the number of lines to read: "))
read_first_n_lines(file_name, n)

#13
#a)

# Foydalanuvchidan fayl nomi va qo'shiladigan matnni olamiz
file_name = input("Fayl nomini kiriting: ")
text_to_append = input("Qo'shmoqchi bo'lgan matnni kiriting: ")

try:
    # Matnni faylga qo‘shamiz (append mode - "a")
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(text_to_append + "\n")  # Har bir matn yangi qatordan yoziladi

    print("\nMatn faylga muvaffaqiyatli qo‘shildi.")
    
    # Faylni o'qib, butun mazmunini ko‘rsatamiz
    print("\nFaylning yangilangan mazmuni:")
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Fayl topilmadi.")
except UnicodeDecodeError:
    print("Kodlash (encoding) bilan bog'liq xatolik yuz berdi.")
except Exception as e:
    print("Xatolik:", e)

#b)___________________________________________________________________

def append_text_to_file(filename, text_to_append):
    with open(filename, 'a') as file:
        # Append the text to the file
        file.write(text_to_append + '\n')
    
    with open(filename, 'r') as file:
        content = file.read()
        print("Current content of the file:")
        print(content)

filename = "example.txt"
text_to_append = "This is the new text that will be appended."

append_text_to_file(filename, text_to_append)


#14
#a)
file_name= input("Faul nomini kiriting: ")
n= int(input("Qatorni kiriting: "))
try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
            last_lines = lines[-n:]  # Get the last n lines
            print(f"\nLast {n} line(s) of the file:")
            for line in last_lines:
                print(line.strip())
except FileNotFoundError:
        print("File not found. Please check the file name.")
except UnicodeDecodeError:
        print("Encoding error while reading the file.")
except Exception as e:
        print("An error occurred:", e)


#b)-------------------------------------------------------------------
def read_last_n_lines(file_name, n):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
            last_lines = lines[-n:]  # Get the last n lines
            print(f"\nLast {n} line(s) of the file:")
            for line in last_lines:
                print(line.strip())
    except FileNotFoundError:
        print("File not found. Please check the file name.")
    except UnicodeDecodeError:
        print("Encoding error while reading the file.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage
file_name = input("Enter the file name: ")
n = int(input("Enter the number of lines to read from the end: "))
read_last_n_lines(file_name, n)


#15
#a)

try:
    filename = input("Enter the file name to read: ")

    # Open the file in read mode with UTF-8 encoding
    with open(filename, 'r', encoding='utf-8') as file:
        lines_list = [line.strip() for line in file]

    print("Lines stored in the list:")
    print(lines_list)

except FileNotFoundError:
    print("FileNotFoundError: The file does not exist.")

except PermissionError:
    print("PermissionError: You don't have permission to read this file.")

except UnicodeDecodeError:
    print("UnicodeDecodeError: Could not decode file with UTF-8 encoding.")

except Exception as e:
    print("An unexpected error occurred:", e)




#b)-----------------------------------------------------

def read_file_into_list(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file]  # Read and clean each line
            return lines
    except FileNotFoundError:
        print("File not found. Please check the file name.")
        return []
    except UnicodeDecodeError:
        print("Encoding error while reading the file.")
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []

# Example usage
file_name = input("Enter the file name: ")
lines_list = read_file_into_list(file_name)

# Print the list
print("\nLines stored in the list:")
for line in lines_list:
    print(line)


#16
#a)
try:
    filename = input("Enter the file name to read: ")

    with open(filename, 'r', encoding='utf-8') as file:
        # Read lines one by one and store in a list variable
        lines = file.readlines()

    print("File content stored in variable:")
    for line in lines:
        print(line, end='')  # end='' prevents extra newlines

except FileNotFoundError:
    print("FileNotFoundError: The file does not exist.")

except PermissionError:
    print("PermissionError: You don't have permission to read this file.")

except UnicodeDecodeError:
    print("UnicodeDecodeError: Could not decode file with UTF-8 encoding.")

except Exception as e:
    print("An unexpected error occurred:", e)



#b)------------------------------------------------------------------
def read_file_to_variable(file_path):
    # Initialize an empty list to store lines
    lines = []
    
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read each line and store it in the list
        for line in file:
            lines.append(line.strip())  # .strip() removes leading/trailing whitespace
    
    return lines

file_path = 'your_file.txt'  # Replace with the path to your file
lines = read_file_to_variable(file_path)

for line in lines:
    print(line)


#17
#a)
try:
    fayl_nomi = input("Fayl nomini kiriting: ")

    # Faylni o'qish va har bir satrni massiv (ro'yxat) sifatida saqlash
    with open(fayl_nomi, 'r', encoding='utf-8') as fayl:
        satrlar = [satr.strip() for satr in fayl]  # .strip() qator oxiridagi \n ni olib tashlaydi

    print("Fayl satrlari ro'yxatga saqlandi:")
    print(satrlar)

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi. Fayl nomini tekshiring.")

except PermissionError:
    print("Xatolik: Faylga ruxsat yo‘q.")

except UnicodeDecodeError:
    print("Xatolik: Faylni UTF-8 kodlashda o‘qib bo‘lmadi.")

except Exception as e:
    print("Noma'lum xatolik yuz berdi:", e)


#b)-------------------------------------------------------------------------------------------
def read_file_to_array(file_name):
    # Initialize an empty list to store the lines
    lines_array = []
    
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Strip the newline characters and append to the list
                lines_array.append(line.strip())
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return lines_array

file_name = "example.txt"  # Replace with your file name
lines = read_file_to_array(file_name)

print(lines)


#18
#a)
def eng_uzun_sozlar_top(matn):
    sozlar = matn.split()  # matnni so‘zlarga bo‘lamiz
    maksimal_uzunlik = max(len(soz) for soz in sozlar)  # eng uzun so‘z uzunligini topamiz
    eng_uzunlar = [soz for soz in sozlar if len(soz) == maksimal_uzunlik]  # shunday uzunlikdagi barcha so‘zlar
    return eng_uzunlar

# Foydalanuvchidan matn olish
matn = input("Iltimos, matn kiriting: ")
natija = eng_uzun_sozlar_top(matn)

print("Eng uzun so'z(lar):", natija)

#19
#a)
try:
    fayl_nomi = input("Fayl nomini kiriting: ")

    with open(fayl_nomi, 'r', encoding='utf-8') as fayl:
        qatorlar_soni = sum(1 for qator in fayl)

    print(f"Fayldagi qatorlar soni: {qatorlar_soni}")

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")

except PermissionError:
    print("Xatolik: Faylga kirish ruxsati yo'q.")

except UnicodeDecodeError:
    print("Xatolik: Faylni UTF-8 formatida o‘qib bo‘lmadi.")

except Exception as e:
    print("Boshqa xatolik yuz berdi:", e)
#20
from collections import Counter

try:
    fayl_nomi = input("Fayl nomini kiriting: ")

    with open(fayl_nomi, 'r', encoding='utf-8') as fayl:
        matn = fayl.read().lower()  # Faylni o'qib, kichik harflarga o'tkazamiz
        sozlar = matn.split()       # Bo‘sh joy bo‘yicha so‘zlarga ajratamiz

        # So'z chastotalarini hisoblash
        chastota = Counter(sozlar)

    print("So‘zlar chastotasi:")
    for soz, soni in chastota.items():
        print(f"{soz}: {soni} marta")

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")

except PermissionError:
    print("Xatolik: Faylga kirish ruxsati yo‘q.")

except UnicodeDecodeError:
    print("Xatolik: Fayl UTF-8 kodlashda o‘qib bo‘lmadi.")

except Exception as e:
    print("Boshqa xatolik yuz berdi:", e)


#21
import os

try:
    fayl_nomi = input("Fayl nomini kiriting: ")

    if os.path.isfile(fayl_nomi):
        hajm = os.path.getsize(fayl_nomi)
        print(f"Fayl hajmi: {hajm} bayt")
    else:
        print("Xatolik: Bu fayl mavjud emas yoki bu oddiy fayl emas.")

except PermissionError:
    print("Xatolik: Faylga kirishga ruxsat yo'q.")

except Exception as e:
    print("Boshqa xatolik yuz berdi:", e)


#22
try:
    # Ro'yxatdagi ma'lumotlar
    malumotlar = ['olma', 'banan', 'gilos', 'shaftoli']

    fayl_nomi = input("Yoziladigan fayl nomini kiriting (masalan: mevalar.txt): ")

    # Faylni yozish rejimida ochamiz
    with open(fayl_nomi, 'w', encoding='utf-8') as fayl:
        for element in malumotlar:
            fayl.write(element + '\n')  # Har bir elementni yangi qatorga yozamiz

    print(f"Ro'yxatdagi ma'lumotlar '{fayl_nomi}' fayliga muvaffaqiyatli yozildi.")

except PermissionError:
    print("Xatolik: Faylga yozishga ruxsat yo'q.")

except Exception as e:
    print("Noma'lum xatolik yuz berdi:", e)


#23
# Manba fayl nomi (nusxa olinadigan fayl)
manba_fayl = 'manba.txt'

# Yangi fayl nomi (nusxa yoziladigan fayl)
yangi_fayl = 'nusxa.txt'

try:
    # Manba faylni o'qish rejimida ochamiz
    with open(manba_fayl, 'r', encoding='utf-8') as manba:
        mazmun = manba.read()  # Fayldagi barcha matnni o'qish

    # Yangi faylni yozish rejimida ochamiz
    with open(yangi_fayl, 'w', encoding='utf-8') as nusxa:
        nusxa.write(mazmun)  # Matnni yangi faylga yozish

    print("Fayl muvaffaqiyatli nusxalandi.")
except FileNotFoundError:
    print("Manba fayl topilmadi.")
except Exception as e:
    print("Xatolik yuz berdi:", e)


#24
# Fayl nomlarini belgilang
fayl1 = 'fayl1.txt'
fayl2 = 'fayl2.txt'
chiqish_fayl = 'birlashtirilgan.txt'

try:
    # Har ikki faylni o'qib chiqamiz
    with open(fayl1, 'r', encoding='utf-8') as f1, open(fayl2, 'r', encoding='utf-8') as f2:
        qatorlar1 = f1.readlines()
        qatorlar2 = f2.readlines()

    # Har bir satrni mos satr bilan birlashtiramiz
    birlashtirilgan = []
    maksimal = max(len(qatorlar1), len(qatorlar2))
    for i in range(maksimal):
        satr1 = qatorlar1[i].strip() if i < len(qatorlar1) else ''
        satr2 = qatorlar2[i].strip() if i < len(qatorlar2) else ''
        birlashtirilgan.append(satr1 + ' ' + satr2)

    # Natijani yangi faylga yozamiz
    with open(chiqish_fayl, 'w', encoding='utf-8') as chiqish:
        for satr in birlashtirilgan:
            chiqish.write(satr + '\n')

    print("Satrlar muvaffaqiyatli birlashtirildi va saqlandi.")
except FileNotFoundError:
    print("Fayllardan biri topilmadi.")
except Exception as e:
    print("Xatolik yuz berdi:", e)
#25
import random

# Fayl nomi
fayl_nomi = 'matn.txt'

try:
    # Faylni o'qish
    with open(fayl_nomi, 'r', encoding='utf-8') as fayl:
        qatorlar = fayl.readlines()  # Barcha satrlarni o'qish

    # Agar fayl bo'sh bo'lmasa, tasodifiy qatorni tanlash
    if qatorlar:
        tasodifiy_qator = random.choice(qatorlar).strip()
        print("Tasodifiy qator:", tasodifiy_qator)
    else:
        print("Fayl bo‘sh.")
except FileNotFoundError:
    print("Fayl topilmadi.")
except Exception as e:
    print("Xatolik yuz berdi:", e)

# 26.
# Fayl nomi
fayl_nomi = 'test.txt'

try:
    # Faylni ochamiz
    fayl = open(fayl_nomi, 'r', encoding='utf-8')

    # Fayl yopilgan yoki yo‘qligini tekshirish
    if fayl.closed:
        print("Fayl yopilgan.")
    else:
        print("Fayl ochiq (yopilmagan).")

    # Endi faylni yopamiz
    fayl.close()

    # Yana tekshiramiz
    if fayl.closed:
        print("Fayl endi yopildi.")
    else:
        print("Fayl hali ham ochiq.")
except FileNotFoundError:
    print("Fayl topilmadi.")
except Exception as e:
    print("Xatolik yuz berdi:", e)


#27
def remove_newlines_from_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        # Har bir qatorning oxiridagi yangi qator belgisini olib tashlaymiz
        cleaned_lines = [line.strip() for line in lines]

        print("Yangi qator belgilarisiz matn:")
        for line in cleaned_lines:
            print(line)

        return cleaned_lines  # Agar kerak bo‘lsa, ro‘yxatni qaytaradi

    except FileNotFoundError:
        print("Fayl topilmadi.")
    except UnicodeDecodeError:
        print("Kodlash (encoding) bilan bog‘liq xatolik.")
    except Exception as e:
        print("Xatolik yuz berdi:", e)

# Misol uchun ishlatish:
file_name = input("Fayl nomini kiriting: ")
remove_newlines_from_file(file_name)


#28
import re

def hisobla_sozlar_soni(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            text = file.read()

        # So'zlarni ajratamiz: har qanday bo'sh joy yoki vergul(,) bo'yicha
        words = re.split(r"[,\s]+", text.strip())

        # Bo'sh elementlarni olib tashlaymiz (agar mavjud bo‘lsa)
        words = [word for word in words if word]

        print(f"So'zlar soni: {len(words)}")
        return len(words)

    except FileNotFoundError:
        print("Fayl topilmadi.")
    except UnicodeDecodeError:
        print("Kodlash bilan bog'liq xatolik yuz berdi.")
    except Exception as e:
        print("Xatolik yuz berdi:", e)

# Misol uchun foydalanish:
file_name = input("Fayl nomini kiriting: ")
hisobla_sozlar_soni(file_name)


#29
# Belgilarni saqlash uchun bo‘sh ro‘yxat
barcha_belgilar = []

# Tekshiriladigan fayllar ro'yxati
fayllar = ['fayl1.txt', 'fayl2.txt', 'fayl3.txt']  # Fayl nomlarini o'zingiz kiriting

for fayl_nomi in fayllar:
    try:
        with open(fayl_nomi, 'r', encoding='utf-8') as fayl:
            mazmun = fayl.read()  # Butun fayl matnini o‘qish
            for belgi in mazmun:
                barcha_belgilar.append(belgi)  # Har bir belgini ro'yxatga qo'shish
    except FileNotFoundError:
        print(f"{fayl_nomi} topilmadi.")
    except Exception as e:
        print(f"{fayl_nomi} faylni o'qishda xatolik yuz berdi:", e)

# Natijani chiqarish
print("Topilgan barcha belgilar ro'yxati:")
print(barcha_belgilar)


# 30.

import string

# Alfavitdagi barcha bosh harflar (A-Z)
harflar = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Har bir harf uchun alohida fayl yaratish
for harf in harflar:
    fayl_nomi = f"{harf}.txt"
    try:
        with open(fayl_nomi, 'w', encoding='utf-8') as fayl:
            fayl.write(f"Bu {harf}.txt fayli.\n")  # Fayl ichiga matn yoziladi
        print(f"{fayl_nomi} yaratildi.")
    except Exception as e:
        print(f"{fayl_nomi} yaratishda xatolik yuz berdi:", e)


#31
import string

# Harflar ro'yxati: A dan Z gacha
harflar = list(string.ascii_uppercase)  # ['A', 'B', ..., 'Z']

# Har bir satrda nechta harf bo'lishi kerak (o'zingiz belgilaysiz)
harflar_soni_har_satrda = 5

# Yangi fayl nomi
fayl_nomi = 'alifbo.txt'

try:
    with open(fayl_nomi, 'w', encoding='utf-8') as fayl:
        for i in range(0, len(harflar), harflar_soni_har_satrda):
            satr = harflar[i:i + harflar_soni_har_satrda]
            fayl.write(' '.join(satr) + '\n')

    print(f"{fayl_nomi} fayli muvaffaqiyatli yaratildi.")
except Exception as e:
    print("Xatolik yuz berdi:", e)
