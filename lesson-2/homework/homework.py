1.
Name=input("Ismingizni kiriting: ")
Year=int(input("Tug'ilgan yilingizni kiriting: "))
Joriy_yil=2025
# fuqoroni yoshini aniqlash
Age=Joriy_yil-Year
print(f" Salom {Name}, siz {Age} yoshdasiz")

2.
text = 'LMaasleitbtui'
Malibu=text[1:12:2]
print(Malibu)
Lassetti = text[0:13:2]
print(Lassetti)

3.
text= 'MsaatmiazD'
Matiz=text[0:9:2]
print(Matiz)

4.
txt = "I'am John. I am from London"
london=txt[20:27]
print(london)

5.
text=input("Ma'lum bir satrni kiriting: ")
result=text[::-1]
print(result)

6.
text_kiriting=(input("Matn kiriting:  "))
unlilar = "aeiouAEIOU"
count=0
for i in text_kiriting:
    if i in unlilar:
        count+=1
print('Kiritilgan matnda unli harflar soni: ',count, ' ta harfni tashkil qiladi!')

7.
Sonlarni_kiriting = input("Sonlarni shoshmasdan kiriting: ")
raqamlar = list(map(float, Sonlarni_kiriting.split()))
eng_kattasi = max(raqamlar)
print("Eng katta raqam: ", eng_kattasi)

8.
text=input("Xoxlagan bitta matnni kiriting: ")

result= text[::-1]
if text==result:
    print(text, "Kiritgan so'zingiz palindrom ekan!")
else:
    print(text, "Kiritgan so'zingiz polindrom emas.")

9.
email = input(" Pochtangizni kiriting: ")
if "@" in email:
    domain = email.split("@")[1]
    print(f"Pochtangizni domini: {domain}")
else:
    print("Siz elektron pochta kiritmadingiz. Iltimos elektron pochpangizni kiriting.")

10.
import random
import string
def generate_password(length=12):    
    letters = string.ascii_letters     
    password = ''.join(random.choice(letters) for _ in range(length))    
    return password
password = generate_password(12)
print("Generated Password:", password)








